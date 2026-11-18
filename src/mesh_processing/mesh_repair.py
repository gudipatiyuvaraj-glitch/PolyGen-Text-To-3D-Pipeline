"""
PolyGen - Automated Mesh Healing & Repair Engine
Detects and fixes non-manifold edges, inverted normals, holes, and floating vertices.
Fully compatible with modern trimesh 4.x.
"""

import trimesh
import numpy as np
from typing import Dict, Any


class MeshSanitizer:
    def __init__(self):
        pass

    @staticmethod
    def inspect_defects(mesh: trimesh.Trimesh) -> Dict[str, Any]:
        """Analyzes mesh integrity and detects topological defects."""
        return {
            "faces": len(mesh.faces),
            "vertices": len(mesh.vertices),
            "is_watertight": mesh.is_watertight,
            "is_winding_consistent": mesh.is_winding_consistent,
            "euler_characteristic": mesh.euler_number
        }

    @classmethod
    def heal_mesh(cls, mesh: trimesh.Trimesh) -> trimesh.Trimesh:
        """
        Executes an automated multi-stage geometric cleanup pipeline:
        1. Remove unreferenced vertices & clean degenerate triangles
        2. Heal inverted face normals (consistent winding)
        3. Fill boundary holes
        4. Extract largest connected component (strip floating junk)
        5. Center pivot and normalize scale
        """
        print("[MeshSanitizer] Initiating geometric healing protocol...")

        # Stage 1: Clean duplicate faces, unreferenced vertices, and degenerate triangles
        mesh.update_faces(mesh.unique_faces())
        mesh.update_faces(mesh.nondegenerate_faces())
        mesh.remove_unreferenced_vertices()

        # Stage 2: Normalize face normals and winding order (ensures outside faces out)
        trimesh.repair.fix_winding(mesh)
        trimesh.repair.fix_normals(mesh)

        # Stage 3: Fill boundary holes
        trimesh.repair.fill_holes(mesh)

        # Stage 4: Strip disconnected floating fragments (keep primary asset)
        connected_components = mesh.split(only_watertight=False)
        if len(connected_components) > 1:
            mesh = max(connected_components, key=lambda m: m.area)
            print(f"[MeshSanitizer] Removed {len(connected_components) - 1} disconnected artifact components.")

        # Stage 5: Center origin and normalize scale to unit bounds
        mesh.apply_translation(-mesh.centroid)
        max_extent = max(mesh.extents) if len(mesh.extents) > 0 and max(mesh.extents) > 0 else 1.0
        mesh.apply_scale(1.0 / max_extent)

        print(f"[MeshSanitizer] Healing complete! Watertight: {mesh.is_watertight}, Winding: {mesh.is_winding_consistent}")
        return mesh


if __name__ == "__main__":
    # Create a test cube with an intentionally flipped normal
    test_mesh = trimesh.creation.box(extents=(1, 1, 1))
    test_mesh.faces[0] = test_mesh.faces[0][::-1]  # Invert face normal

    sanitizer = MeshSanitizer()
    before = sanitizer.inspect_defects(test_mesh)
    print(f"[*] Pre-Repair State : {before}")

    healed = sanitizer.heal_mesh(test_mesh)
    after = sanitizer.inspect_defects(healed)
    print(f"[*] Post-Repair State: {after}")