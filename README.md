# 🚀 KeaBuilder AI Assignment Submission

## Candidate
**Harsh Tripathi**

## Project Title
AI Workflow System for KeaBuilder Platform

---

# 📌 Overview

This project demonstrates practical AI features that can be integrated inside **KeaBuilder**, a SaaS platform focused on funnels, lead capture, automation, and content generation.

The goal was to build lightweight but working AI systems that improve:

- Lead qualification
- Personalized responses
- AI content generation workflows
- Similarity search
- Reliability with fallback systems
- High-volume request handling

Built using:

- Python
- Streamlit
- Groq API
- FAISS
- NumPy

---

# ✅ Implemented Features

---

## 1. AI Lead Processing

### Features:
- Captures form lead inputs
- Scores leads based on:
  - Budget
  - Urgency
  - Intent keywords
- Classifies into:
  - Hot
  - Warm
  - Cold

### AI Responses:
Uses Groq LLM to generate personalized human responses.

### Example Output:

```json
{
  "name": "Rahul",
  "score": 88,
  "tier": "Hot",
  "next_action": "Immediate callback"
}