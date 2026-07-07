# Coltex Product Licensing

## License model

The Coltex **Dataset** (knowledge base content, vector chunks, embeddings, graph edges, benchmarks, and product artifacts) is licensed under the **Coltex End User License Agreement (EULA)** — a commercial license, not an open-source license.

| Document | Purpose |
|----------|---------|
| [EULA.md](../EULA.md) | Full End User License Agreement |
| [knowledge-base/EULA.md](../knowledge-base/EULA.md) | Dataset scope summary |
| [knowledge-base/LICENSE](../knowledge-base/LICENSE) | Purchaser rights summary |
| [PROVENANCE.md](../knowledge-base/PROVENANCE.md) | Content origin and compliance |
| [NOTICE](../NOTICE) | Third-party open-source dependencies (engine tooling only) |

---

## What the EULA covers

| Content | License | Included in product? |
|---------|---------|---------------------|
| Distributable `CHUNK-*.md` files | Coltex EULA | Yes |
| Product artifacts (`data/product/`) | Coltex EULA | Yes |
| Benchmark datasets (`benchmarks/`) | Coltex EULA | Yes |
| `knowledge-base/_excluded_from_distribution/` | — | **No** — quarantined stubs |
| `knowledge-base/generated/` | — | **No** — stress-test corpus only |

All distributible content is **original synthetic documentation** authored for Coltex. It was not copied from third-party documentation, web scraping, or proprietary sources.

See `knowledge-base/PROVENANCE.md` for full content origin documentation.

---

## Permitted use (summary)

Under the EULA you may:

- Use the Dataset internally for RAG systems, AI agents, and related applications
- Build and sell commercial software and services powered by the Dataset
- Load chunks and embeddings into vector databases you operate
- Create derivative products that do not redistribute raw Dataset content
- Make backup copies for disaster recovery

---

## Restrictions (summary)

You may **not** (without written consent):

- Resell, sublicense, or redistribute the Dataset as a standalone data product
- Publish substantial portions to public repos, model hubs, or file-sharing sites
- Remove provenance metadata, EULA notices, or manifest checksums
- Exceed your purchased tier scope (Enterprise, Premium, Hyper)

See [EULA.md](../EULA.md) for complete terms.

---

## Third-party dependencies (runtime)

The Coltex **engine** uses open-source libraries listed in [NOTICE](../NOTICE). Those components remain under their respective licenses (Apache-2.0, MIT, BSD, etc.).

| Dependency | License | Notes |
|------------|---------|-------|
| sentence-transformers | Apache-2.0 | Embedding library |
| `all-MiniLM-L6-v2` model | Apache-2.0 | Downloaded from Hugging Face |
| chromadb | Apache-2.0 | Vector store |
| PyTorch | BSD-style | ML framework |

Runtime dependencies are **not bundled** in the Dataset package. You are responsible for their license compliance when used.

This package is a **RAG dataset** — no LLM weights are included.

---

## Commercial distribution checklist

Before deploying or offering services built on the Dataset:

```bash
make product-enterprise       # Build with compliance gates
make audit-distribution       # Verify EULA + provenance compliance
```

The audit checks for:

- Required `EULA.md`, `NOTICE`, and `PROVENANCE.md` files
- No excluded paths in product artifacts
- No forbidden third-party source patterns in content
- No placeholder boilerplate in distributable documents

---

## Disclaimer

This document summarizes the licensing approach. It is not legal advice. Consult qualified counsel before commercial use.

For enterprise agreements, custom tiers, or redistribution consent: contact the repository maintainer.
