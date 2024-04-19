# BioMistral 7B RAG chatbot

This is a RAG implementation using Open Source stack.

BioMistral 7B has been used to build this app along with PubMedBert as an embedding model, Qdrant as a self hosted Vector DB, and Langchain & Llama CPP as the orchestration frameworks.

BioMistral 7B is a specialized LLM tailored for the biomedical domain. It is derived from Mistral 7B Instruct v0.1 and further pre-trained on PubMed Central. Kindly refer to the research paper below for the training details.

## Installation steps

1. Download a Biomistral model (gguf format) to the directory `/data/models/`. In this example I used `MaziyarPanahi/BioMistral-7B-GGUF BioMistral-7B.Q4_K_M.gguf`. Download any medical pdfs that you wish to query to the directory `/data/`.

2. Install the following python packages

    - torch
    - ipywidgets
    - transformers
    - langchain
    - llama-index
    - llama-cpp-python
    - sentence-transformers
    - "unstructured[pdf]"
    - "fastapi[all]"
    - qdrant-client

3. Install the following dependencies

    - libmagic-dev
    - poppler-utils
    - tesseract-ocr

4. Install docker and start Qdrant container. Go to http://localhost:6333/dashboard to verify if it has started.

    - docker pull qdrant/qdrant
    - docker run -p 6333:6333 qdrant/qdrant

5. Ingest the pdf files and load into the Qdrant db. Go to http://localhost:6333/dashboard to verify `vector_db` has been created in Collections.

    - python ingest.py

6. Run fastapi and go to http://127.0.0.1:8000 to start querying

    - uvicorn app:app

References
1. [BioMistral: A Collection of Open-Source Pretrained Large Language Models for Medical Domains](https://arxiv.org/abs/2402.10373)