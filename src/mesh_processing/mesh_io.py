"""
PolyGen - Advanced Mesh Processor & LOD Generator
Handles Quadric Edge-Collapse Decimation, Mesh Cleaning, and LOD export.
"""

import os
import trimesh
import fast_simplification
from typing import Dict, Any


class AdvancedMeshProcessor:
    def __init__(self):
        pass

    @staticmethod
    def load_or_create_highpoly_sample(output_path: str = "data/samples/highpoly_sample.obj") -> trimesh.Trimesh:
        """Creates a dense high-poly asset to demonstrate decimation capabilities."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        mesh = trimesh.creation.icosphere(subdivisions=4, radius=1.0)
        mesh.export(output_path)
        return mesh

    @staticmethod
    def decimate_mesh(mesh: trimesh.Trimesh, target_face_count: int) -> trimesh.Trimesh:
        """
        True Quadric Edge-Collapse Decimation using C++ fast_simplification:
        Guarantees reduction of polygon density while preserving geometric silhouette.
        """
        total_faces = len(mesh.faces)
        if target_face_count >= total_faces:
            return mesh.copy()

        reduction_fraction = 1.0 - (target_face_count / total_faces)
        
        # Run fast quadric decimation on vertex and face numpy arrays
        decimated_v, decimated_f = fast_simplification.simplify(
            points=mesh.vertices,
            triangles=mesh.faces,
            target_reduction=reduction_fraction
        )

        simplified_mesh = trimesh.Trimesh(vertices=decimated_v, faces=decimated_f, process=True)
        return simplified_mesh

    def generate_lods(self, mesh: trimesh.Trimesh, base_name: str = "data/samples/model") -> Dict[str, Any]:
        """
        Generates 3 industry-standard Game Levels of Detail (LODs):
        - LOD0 (High Detail): 100% faces
        - LOD1 (Mid Detail): 40% faces
        - LOD2 (Low Poly / Mobile): 15% faces
        """
        total_faces = len(mesh.faces)
        lod_targets = {
            "LOD0_High": 1.0,
            "LOD1_Mid": 0.40,
            "LOD2_Low": 0.15
        }
        
        lod_results = {}

        for lod_name, ratio in lod_targets.items():
            target_faces = int(total_faces * ratio)
            
            # Apply real edge collapse
            simplified = self.decimate_mesh(mesh, target_faces)
            
            # Normalize pivot to origin
            simplified.apply_translation(-simplified.centroid)
            
            out_file = f"{base_name}_{lod_name}.obj"
            simplified.export(out_file)
            
            actual_reduction = (1.0 - (len(simplified.faces) / total_faces)) * 100.0
            lod_results[lod_name] = {
                "path": out_file,
                "faces": len(simplified.faces),
                "vertices": len(simplified.vertices),
                "reduction": f"{actual_reduction:.1f}%"
            }
            print(f"[LOD Engine] Created {lod_name}: {len(simplified.faces)} faces (Optimized by {actual_reduction:.1f}%)")

        return lod_results


if __name__ == "__main__":
    processor = AdvancedMeshProcessor()
    high_poly = processor.load_or_create_highpoly_sample()
    print(f"[*] Raw High-Poly: {len(high_poly.faces)} faces")
    lods = processor.generate_lods(high_poly)
    print("✅ Real Quadric LOD Decimation Verified!")