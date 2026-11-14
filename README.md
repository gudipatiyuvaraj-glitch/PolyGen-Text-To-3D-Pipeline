# PolyGen-Text-To-3D-Pipeline
Generative Text-to-3D Asset Pipeline with LLM Prompt Augmentation and Automated Mesh Decimation (Infotact Solutions Internship)
# 🔷 PolyGen: Generative Text-to-3D Asset Pipeline

**Organization:** Infotact Solutions  
**Role:** Associate L1 Intern (Generative AI)  
**Project Ref:** ITS/GAI/1304  
**Author:** Gudipati Yuvaraj  

---

## 📌 Project Overview
PolyGen is an intelligent Text-to-3D asset pipeline designed to generate clean, optimized 3D models from simple natural language prompts.

### 🌟 Key Innovations
1. **LLM Prompt Augmentation:** Enriches raw prompts with 3D-specific geometry and texture descriptors.
2. **Automated Mesh Optimization:** Decimation and manifold cleaning for game-engine-ready assets.
3. **Interactive 3D Previewer:** Built-in web UI for live 3D inspection and export.

---

## 📁 Repository Structure

PolyGen-Text-To-3D-Pipeline/
├── data/samples/ # Output 3D assets (.obj, .glb)
├── docs/ # Documentation & reports
├── notebooks/ # Research and Colab notebooks
├── src/
│ ├── llm/ # Prompt augmentation logic
│ ├── generation/ # Text-to-3D model wrappers
│ ├── mesh_processing/ # Decimation and clean-up
│ ├── ui/ # Interactive UI
│ └── pipeline.py # Main orchestration script
├── requirements.txt # Dependencies
└── README.md

## 🚀 Quickstart
```bash
python src/pipeline.py

