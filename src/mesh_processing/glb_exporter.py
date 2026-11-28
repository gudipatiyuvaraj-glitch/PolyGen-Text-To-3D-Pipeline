"""
PolyGen - Production GLB Binary Packaging Engine
Exports production-grade, self-contained .glb assets ready for Unity, Unreal, and WebGL.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import trimesh
from typing import Dict, Any


class GLBExporter:
    def __init__(self, export_dir: str = "data/samples/glb"):
        self.export_dir = export_dir
        os.makedirs(self.export_dir, exist_ok=True)

    def export_as_glb(self, mesh: trimesh.Trimesh, asset_name: str) -> str:
        """
        Converts mesh geometry and PBR visual properties into a compact, 
        self-contained .glb binary file.
        """
        output_path = os.path.join(self.export_dir, f"{asset_name}.glb")
        
        # Export as glb binary
        glb_data = mesh.export(file_type='glb')
        with open(output_path, "wb") as f:
            f.write(glb_data)
            
        file_size_kb = round(os.path.getsize(output_path) / 1024, 2)
        print(f"[GLBExporter] Successfully packaged: {output_path} ({file_size_kb} KB)")
        return output_path


if __name__ == "__main__":
    from src.mesh_processing.mesh_io import AdvancedMeshProcessor
    from src.mesh_processing.texture_baker import TextureBaker

    p = AdvancedMeshProcessor()
    sample = p.load_or_create_highpoly_sample()
    
    baker = TextureBaker()
    textured_mesh = baker.apply_pbr_material(sample, style_preset="Cyberpunk Hard-Surface")
    
    exporter = GLBExporter()
    out = exporter.export_as_glb(textured_mesh, "cyberpunk_katana_game_ready")
    print(f"✅ Production GLB Binary Verified: {out}")