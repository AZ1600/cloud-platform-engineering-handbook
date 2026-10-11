# 02 — Ingestion, Chunking and Index Provenance

## What the checked-in implementation does

[`src/ingest.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/ingest.py) reads sorted Markdown files from `data/`, separates paragraphs, groups text up to a nominal **800 characters**, assigns global `chunk_number` values, and stores:

- `index/embeddings.npy` — normalized sentence-transformer vectors;
- `index/chunks.json` — the model name, chunk content, source names and chunk numbers.

The embedding model is `all-MiniLM-L6-v2`. The generated `index/` is excluded from Git and rebuilt as part of the RAG container build.

```text
Markdown files -> paragraph grouping -> numbered chunks
                                  -> embedding model
                                  -> NumPy embeddings + JSON metadata
```

## Inspect before building

```bash
# Run inside a clone of rag-ops-assistant, not the handbook.
find data -maxdepth 1 -type f -name '*.md' -print
sed -n '1,140p' src/ingest.py
sed -n '1,100p' src/rag_core.py
```

Running `python src/ingest.py` downloads/loads an embedding model and writes local index files; it is **not** required for the handbook build.

## Edge cases: what 800 characters does not guarantee

The current `chunk_text` groups whole paragraphs. If one paragraph exceeds 800 characters, it can be stored as a **single oversized chunk**. `max_chars` is therefore a grouping target, not a strict bound. The algorithm also does not currently store source commit SHA, per-document checksum or heading path.

For an index used across releases, extend each record with a stable key:

```text
source_document + document_revision + heading_path + local_chunk_index
```

Using only a global numeric chunk ID can make citations unstable after reindexing. Add deterministic hashes or persistent IDs before comparing citations across deployments.

## Source and freshness checklist

- [ ] Trust the document's origin and review who can modify it.
- [ ] Record the source revision, timestamp, ownership and classification.
- [ ] Keep access control metadata through chunking and retrieval.
- [ ] Deduplicate identical chunks without erasing original citations.
- [ ] Strip secrets and unnecessary personal information before embedding.
- [ ] Version embedding model, chunking policy and the generated index together.
- [ ] Test a single long paragraph, empty file, repeated heading and malformed UTF-8.

## Thought experiment

If the knowledge base gains a confidential runbook and the assistant is shared across teams, returning the highest-scoring chunk is not enough. **Filter by caller authorization before any chunk reaches the model**; post-hoc citation filtering cannot undo disclosure.

Next: [hybrid retrieval](03-hybrid-retrieval.md).
