# GIBC V2 field scan: who else is entering, and where

Scanned Wed Sep 23 2026, ~10:45 PM ET, via web search for public GitHub repos that name GIBC V2 (then cloned and read). This is a sample, not a census: only entrants with public, indexed repos show up.

## Track 01: TECH (≤ 50M-parameter LM from scratch): crowded, and GPU-armed

| Repo | Params | Compute | Headline result | Angle |
|---|---|---|---|---|
| [AryaErgin/gibc-v2-foundational-llm](https://github.com/AryaErgin/gibc-v2-foundational-llm) | 49,860,480 | RTX 5090 laptop, 37.9 h, 7.2 B tokens (≈2.15e18 FLOPs) | WikiText-103 PPL **31.78**; HellaSwag 30.2 %, ARC-E 39.1 %, PIQA 60.4 %, WinoGrande 48.8 % (lm-eval 0.4.9.1) | Preregistered experiments, retained negative results, hashes, a paper-style repo |
| [1234620/parsimony](https://github.com/1234620/parsimony) | 48,872,576 | Kaggle T4, ~14.4 h, 295 M tokens | 0.9416 bits/byte; "reasoning 99 %" on its own probe | Vocabulary size as a capacity-allocation decision; live GitHub Pages demo; 22 s video |
| [Yuser00123/sievellm-50m](https://github.com/Yuser00123/sievellm-50m) | 49,295,872 | Kaggle T4, 11 h, 492 M tokens | WikiText-103 PPL 82.4 | Quality filtering of FineWeb-Edu |
| Goofturtles/embedding-tax (search index) | 49.3 M | one RTX 4090 | n/a | "Runs in your browser"; also the vocabulary/embedding budget angle |
| liisheng/solid-train (search index) | 49.66 M | n/a | n/a | n/a |

Track 01 evidence also shows the de-facto **required reporting set**: held-out WikiText-103 perplexity plus HellaSwag, ARC-Easy, PIQA and WinoGrande, hardware, duration and approximate FLOPs (from AryaErgin's compliance audit of the official rules).

**Implication for us.** This session's VM is CPU-only (4 vCPU), and Hugging Face (FineWeb, TinyStories, WikiText, lm-eval tasks) is blocked by the network policy. A CPU-trained model would land far behind at least five GPU-trained 49M entries on the two criteria that are pure numbers (perplexity & accuracy, reasoning). The obvious innovation angles (vocabulary budget ×2, data filtering, rigour, in-browser) are already taken.

## Track 02: Applied (Med / Finance): thin on the finance side

| Repo | Sub-track | What it is |
|---|---|---|
| [zhuang768/ForeSure-Global](https://github.com/zhuang768/ForeSure-Global) | Finance | "The Actuary's AI Decision Co-Pilot for Catastrophic & Climate Risks": Taiwan National Fire Agency records 1958–2025, dashboard + an Ethereum Sepolia smart contract |
| [kamau-David/Vetra](https://github.com/kamau-David/Vetra) | Finance | Real-time DeFi rug-pull / scam-token flags from on-chain behaviour |
| [SAHIL-m4/MedPulse-AI](https://github.com/SAHIL-m4/MedPulse-AI) | Medical | ICU telemetry + billing indicators → decompensation prediction |

Track 02 requirements from the event page (search index): "build a system around empirical, real-world data science, predictive machine learning, or automated financial or medical pipelines. **Datasets must be public or de-identified.**" The judging line for MED/FINANCE: "**Rigor & Validation** (quality of research, experimental design, data collection, and validation)" and "Presentation (clarity of demo and communication)".

**Implication for us.** No visible entry touches consumer or household finance, student loans, or calibrated uncertainty. "Rigor & validation" is an explicit criterion, and it's where Rishik's standard (held-out tests, baselines, honest limitations) is strongest.

## Track 03: Open
Only one indexed repo ([varssha-tp/ai-workbench](https://github.com/varssha-tp/ai-workbench), "turns uploaded files into useful results", a general AI wrapper). Open tracks usually draw the most entries overall; the index just doesn't show them.
