"""
PolyGen: Generative Text-to-3D Asset Pipeline
Main entry point for pipeline orchestration.
"""

import sys
import os

# Ensure the root project directory is on sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generation.model_loader import TextTo3DGenerator


def run_pipeline(prompt: str):
    print("=" * 60)
    print("🔷 PolyGen: Generative Text-to-3D Asset Pipeline")
    print("=" * 60)
    print(f"[*] Input User Prompt: '{prompt}'")

    # Initialize Generation Engine
    generator = TextTo3DGenerator()

    # Run Generation Step
    output_file = generator.generate_mesh(prompt)
    print(f"[*] Generation Phase Complete: {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    sample_prompt = "A low-poly medieval wooden shield"
    run_pipeline(sample_prompt)