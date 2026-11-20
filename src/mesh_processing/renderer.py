"""
PolyGen - Multi-Angle Asset Renderer & Snapshot Generator
Captures orthographic and isometric previews of 3D meshes for reports and presentations.
"""

import os
import trimesh
import numpy as np
from typing import List, Dict


class AssetRenderer:
    def __init__(self, output_dir: str = "data/samples/renders"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_inspection_sheet(self, mesh_path: str, asset_name: str = "asset") -> Dict[str, str]:
        """
        Inspects mesh bounds and generates descriptive camera angles 
        and asset portfolio metadata for reports and slides.
        """
        mesh = trimesh.load(mesh_path, force='mesh')
        
        # Calculate bounding box dimensions & geometric center
        extents = mesh.extents.tolist()
        centroid = mesh.centroid.tolist()
        
        angles = {
            "isometric": {"camera_pos": [1.5, 1.5, 1.5], "look_at": centroid},
            "front_view": {"camera_pos": [0.0, 2.0, 0.0], "look_at": centroid},
            "side_view":  {"camera_pos": [2.0, 0.0, 0.0], "look_at": centroid},
            "top_view":   {"camera_pos": [0.0, 0.0, 2.0], "look_at": centroid}
        }
        
        manifest_file = os.path.join(self.output_dir, f"{asset_name}_manifest.txt")
        with open(manifest_file, "w") as f:
            f.write(f"PolyGen 3D Asset Portfolio Sheet: {asset_name}\n")
            f.write("=" * 50 + "\n")
            f.write(f"Source Mesh: {mesh_path}\n")
            f.write(f"Faces: {len(mesh.faces):,}\n")
            f.write(f"Vertices: {len(mesh.vertices):,}\n")
            f.write(f"Dimensions (X, Y, Z): {[round(x, 3) for x in extents]}\n")
            f.write(f"Watertight Status: {mesh.is_watertight}\n")
            f.write("\nRender Camera Angles Defined:\n")
            for name, cam in angles.items():
                f.write(f"  - {name.upper()}: Camera at {cam['camera_pos']}\n")

        print(f"[AssetRenderer] Portfolio inspection sheet generated: {manifest_file}")
        return {
            "manifest": manifest_file,
            "faces": len(mesh.faces),
            "vertices": len(mesh.vertices),
            "angles": list(angles.keys())
        }


if __name__ == "__main__":
    renderer = AssetRenderer()
    sample_path = "data/samples/asset_LOD1_Mid.obj"
    
    # Ensure sample exists before rendering
    if not os.path.exists(sample_path):
        from src.mesh_processing.mesh_io import AdvancedMeshProcessor
        p = AdvancedMeshProcessor()
        sample = p.load_or_create_highpoly_sample()
        p.generate_lods(sample, base_name="data/samples/asset")

    res = renderer.generate_inspection_sheet(sample_path, asset_name="cyberpunk_katana")
    print(f"✅ Render Inspection Sheet Ready: {res['manifest']}")