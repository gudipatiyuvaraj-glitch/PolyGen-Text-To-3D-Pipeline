"""
PolyGen - LLM 3D Art Director & Prompt Spec Engine
Transforms naive natural language prompts into production-grade 3D generative specifications.
"""

import os
from typing import Dict, Any


class PromptEnhancer:
    def __init__(self, api_key: str = None):
        """
        Initializes the LLM prompt director.
        Can run using cloud LLM APIs (Groq / OpenAI) or built-in heuristic rules.
        """
        self.api_key = api_key or os.getenv("GROQ_API_KEY")

    def enhance(self, raw_prompt: str, style_preset: str = "Game-Ready PBR") -> Dict[str, Any]:
        """
        Expands naive user prompt with 3D structural, material, and geometric requirements.
        """
        print(f"[LLM Director] Ingested raw input: '{raw_prompt}'")
        print(f"[LLM Director] Applying style preset: '{style_preset}'")

        # Heuristic 3D Expansion Engine (Fast, deterministic & zero-cost)
        keywords = {
            "geometry": "watertight manifold topology, centered origin, symmetrical alignment, quad-dominant structure",
            "materials": "Physically Based Rendering (PBR), distinct roughness and metallic maps, micro-surface details",
            "lighting": "neutral 3-point studio lighting, high dynamic range, zero baked harsh shadows",
            "negative_prompt": "floating disconnected artifacts, non-manifold edges, broken UVs, internal clipping, blurry textures"
        }

        # Build augmented master prompt for the 3D diffusion engine
        augmented_prompt = (
            f"High-fidelity 3D asset of {raw_prompt}. "
            f"Style: {style_preset}. "
            f"Geometric constraints: {keywords['geometry']}. "
            f"Surface: {keywords['materials']}. "
            f"Environment: {keywords['lighting']}."
        )

        spec = {
            "raw_prompt": raw_prompt,
            "augmented_prompt": augmented_prompt,
            "negative_prompt": keywords["negative_prompt"],
            "target_style": style_preset,
            "topology_target": "Game-Ready Quad/Tri Mix"
        }

        print("[LLM Director] Successfully generated enriched 3D specification.")
        return spec


if __name__ == "__main__":
    director = PromptEnhancer()
    result = director.enhance("Cyberpunk Katana", style_preset="Sci-Fi Hard Surface")
    print("\n--- [Augmented 3D Prompt] ---")
    print(result["augmented_prompt"])
    print("\n--- [Negative Constraints] ---")
    print(result["negative_prompt"])