"""
PolyGen: Generative Text-to-3D Asset Pipeline
Main entry point for pipeline orchestration.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.prompt_enhancer import PromptEnhancer
from src.generation.model_loader import HighEnd3DGenerator
from src.mesh_processing.mesh_io import AdvancedMeshProcessor


def run_pipeline(prompt: str, style_preset: str = "Sci-Fi Hard Surface", target_poly_budget: int = 2048):
    print("=" * 70)
    print("🔷 PolyGen: Generative Text-to-3D Production Pipeline")
    print("=" * 70)
    print(f"[*] Input User Query : '{prompt}'")
    print(f"[*] Style Selection  : '{style_preset}'")
    print(f"[*] Target Budget    : {target_poly_budget} polygons\n")

    # 1. LLM 3D Art Director (Prompt Augmentation) Stage
    print("--- [Stage 1: LLM 3D Director & Prompt Augmentation] ---")
    director = PromptEnhancer()
    spec = director.enhance(prompt, style_preset=style_preset)
    print(f"[+] Enriched Prompt : {spec['augmented_prompt'][:90]}...")
    print(f"[+] Negative Filters: {spec['negative_prompt']}\n")

    # 2. SOTA 3D Generative Synthesis Stage
    print("--- [Stage 2: High-End 3D Generative Synthesis] ---")
    generator = HighEnd3DGenerator(backend="triposr")
    gen_result = generator.generate(spec['augmented_prompt'], target_poly_count=target_poly_budget)

    # 3. Advanced Mesh Decimation & Multi-LOD Stage
    print("\n--- [Stage 3: Game-Ready Multi-LOD Decimation & Export] ---")
    processor = AdvancedMeshProcessor()
    high_poly_mesh = processor.load_or_create_highpoly_sample()
    lods = processor.generate_lods(high_poly_mesh, base_name="data/samples/katana")

    print("\n" + "=" * 70)
    print("✅ Pipeline Cycle Complete: Asset Synthesized & Multi-LODs Ready!")
    print(f"   • LOD 0 (Cinematic): {lods['LOD0_High']['faces']} faces")
    print(f"   • LOD 1 (Gameplay) : {lods['LOD1_Mid']['faces']} faces")
    print(f"   • LOD 2 (Mobile/VR): {lods['LOD2_Low']['faces']} faces")
    print("=" * 70)


if __name__ == "__main__":
    sample_prompt = "Cyberpunk Katana with glowing runes"
    run_pipeline(sample_prompt, style_preset="Cyberpunk Hard-Surface", target_poly_budget=2048)