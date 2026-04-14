# 🌍 OmniHistoria

**The complete, unbiased, AI-powered World History Platform.**

---

## Mission

A single system that covers **all of human history** — from prehistory to the present — with zero omissions, zero propaganda, and strict neutrality across every civilization, region, and era.

---

## Core Principles

| Principle | What it means |
|-----------|---------------|
| **Completeness** | Every event, civilization, achievement, and atrocity. Nothing omitted. |
| **Conflict Protocol** | Disputed events always show both narratives, a third scholarly source, the most evidenced version, and why disagreements persist. |
| **Equal Depth** | No centrism of any kind — every region and era covered with the same rigor. |
| **Transparency** | Sources always cited. Gaps in evidence acknowledged honestly. |

---

## Architecture

```
                ┌───────────────────────┐
                │      AI  Brain        │
                │  Open LLM + QLoRA    │
                └──────────┬────────────┘
                           │
                   ┌───────▼───────┐
                   │   Graph RAG   │
                   └───┬───────┬───┘
                       │       │
             ┌─────────▼─┐ ┌───▼───────────┐
             │   Neo4j    │ │  PostgreSQL   │
             │  (graph)   │ │  + pgvector   │
             └────────────┘ └───────┬───────┘
                                    │
                             ┌──────▼──────┐
                             │   S3 / R2   │
                             │  (raw docs) │
                             └─────────────┘
```

| Layer | Stack | Role |
|-------|-------|------|
| Knowledge Graph | Neo4j + PostgreSQL (pgvector, TimescaleDB) | Source of truth — events, entities, sources, conflict clusters |
| Object Storage | S3 / Cloudflare R2 | Raw primary sources (PDFs, images, scans) |
| Retrieval | Graph RAG | Graph traversal for relationships + vector search for semantics |
| AI Brain | Qwen3-32B or DeepSeek V3.2 | Reasoning, response generation, conflict analysis |
| Pipeline | Python + LangChain / LlamaIndex | Ingestion, processing, dataset generation |

---

## Knowledge Graph

- **Nodes** — Events · People · Civilizations · Places · Sources  
- **Edges** — Relationships carrying evidence strength and time metadata  
- **Conflict Clusters** — Dedicated subgraphs linking disputed events to competing narratives and their provenance  

---

## Model Strategy

| Aspect | Approach |
|--------|----------|
| Base model | Qwen3-32B or DeepSeek V3.2 distilled (Apache 2.0) |
| Fine-tuning | QLoRA / LoRA for efficiency |
| Training data | KG-SFT — training examples generated directly from knowledge graph subgraphs |
| Dataset | 5k–20k high-quality examples (LIMA-style: quality over quantity) |
| Focus areas | Conflict resolution · cross-civ comparisons · timelines · unfiltered queries |
| Data sources | Seshat Databank · Wikidata · academic datasets |

---

## Rollout

| Phase | Goal | Key deliverables |
|-------|------|-------------------|
| **1 — MVP** | Working prototype | Knowledge graph + basic RAG + system-prompt-driven LLM (Gemini/GPT-4 interim) |
| **2 — Fine-tune** | Custom model | Training dataset from KG → QLoRA fine-tune → evaluation |
| **3 — Production** | Full platform | Hybrid Graph RAG · fine-tuned model serving · continuous ingestion |

---

## Build Checklist

- [ ] Database schema — PostgreSQL tables + Neo4j Cypher constraints  
- [ ] Ingestion pipeline — Python scripts for Seshat, Wikidata, academic sources  
- [ ] Graph RAG retrieval — hybrid graph + vector search  
- [ ] Training data prompts — KG-SFT / GraphGen templates  
- [ ] Fine-tuning config — Axolotl or Unsloth, ChatML format  
- [ ] Evaluation rubric — conflict adherence · neutrality · regional balance · hallucination rate  

---

## Historical Coverage Timeline

```
 3.3M BCE                                                              2026 CE
 ───●────────●──────────●────────●─────────●──────────●──────────●────────●───
    │        │          │        │         │          │          │        │
    ▼        ▼          ▼        ▼         ▼          ▼          ▼        ▼
  Stone    Farming    Bronze   Classical  Medieval   Colonial   World   Modern
  Tools    begins     Age      Empires    World      Era        Wars    Era
```

| Era | Period | Key Events |
|-----|--------|------------|
| **Prehistory** | 3.3M – 3500 BCE | First stone tools · control of fire · cave paintings · out-of-Africa migrations · Neolithic Revolution · first settlements |
| **Ancient** | 3500 BCE – 500 CE | Mesopotamia & Egypt rise · Indus Valley · Shang Dynasty · Greek city-states · Persian Empire · Maurya & Gupta · Roman Republic & Empire · Han Dynasty · spread of Buddhism & Christianity |
| **Medieval** | 500 – 1500 CE | Byzantine Empire · Islamic Golden Age · Tang & Song dynasties · Viking expansion · Crusades · Mongol Empire · Mali & Great Zimbabwe · Black Death · Ottoman rise |
| **Early Modern** | 1500 – 1800 | Renaissance · Atlantic slave trade · Mughal Empire · colonization of the Americas · Scientific Revolution · Qing Dynasty · Enlightenment · American & French Revolutions |
| **Modern** | 1800 – 1945 | Industrial Revolution · Latin American independence · Scramble for Africa · Meiji Restoration · World War I · Russian Revolution · rise of fascism · World War II · Holocaust |
| **Contemporary** | 1945 – Present | Cold War · decolonization · Chinese Revolution · space race · Vietnam War · fall of the USSR · digital revolution · War on Terror · climate crisis · AI era |

---

## Getting Started

Pick where to begin:

1. **Database schema** — define the data model  
2. **Ingestion pipeline** — start loading historical data  
3. **Fine-tuning config** — prepare model training  
4. **Training data prompts** — generate examples from the KG  
5. **Deployment plan** — end-to-end architecture setup  
6. **Demo** — try a specific historical topic  

## Local MVP Scaffold (Implemented)

This repository now includes a lightweight Python implementation to start Phase 1:

- `src/omnihistoria/schema.py` — typed entities for events, sources, and evidence edges.
- `src/omnihistoria/graph.py` — in-memory graph store with period/dispute retrieval and snapshot export.
- `src/omnihistoria/prompts.py` — KG-SFT prompt builders for conflict and timeline examples.
- `src/omnihistoria/cli.py` — command-line entry point with seeded demo data.
- `tests/test_graph.py` — baseline unit tests for graph behavior and prompt validation.

### Run

```bash
PYTHONPATH=src python -m unittest discover -s tests
PYTHONPATH=src python -m omnihistoria.cli snapshot
PYTHONPATH=src python -m omnihistoria.cli conflicts
```
