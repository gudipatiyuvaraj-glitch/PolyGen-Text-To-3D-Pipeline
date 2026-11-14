"""
PolyGen: Generative Text-to-3D Asset Pipeline
Main entry point for pipeline orchestration.
"""

def run_pipeline(prompt: str):
    print("=" * 60)
    print("🔷 PolyGen: Generative Text-to-3D Asset Pipeline")
    print("=" * 60)
    print(f"[*] Input User Prompt: '{prompt}'")
    print("[*] Status: Skeleton initialized successfully.")
    print("[*] Ready for Day 2: Environment setup & model integration.")
    print("=" * 60)

if __name__ == "__main__":
    sample_prompt = "A low-poly medieval wooden shield"
    run_pipeline(sample_prompt)