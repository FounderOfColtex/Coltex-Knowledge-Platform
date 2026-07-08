# Coltex

**The AI Knowledge Platform for Modern Organizations**

Turn scattered business knowledge into AI-ready intelligence in under 10 minutes — from your terminal.

## Install

```bash
git clone https://github.com/FounderOfColtex/Coltex-Knowledge-Platform.git
cd Coltex-Knowledge-Platform

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -e .
coltex --help
```

`pip install -e .` installs the `coltex` command into your virtualenv. After that, run `coltex` from **any directory**.

### Without installing (from repo root only)

```bash
pip install -r requirements.txt
./coltex --help
```

You must be inside the cloned repo when using `./coltex` or `python3 coltex`.

```bash
coltex new MyWorkspace
coltex upload document.pdf
coltex ask "What is our policy?"
```

Coltex is a **local CLI**. Your project is a **`.ctex` workspace** — like `.uproject` for Unreal or `.blend` for Blender.

---

## Workspace commands

| Command | Purpose |
|---------|---------|
| `coltex new <name>` | Create a new `.ctex` workspace |
| `coltex open <workspace>.ctex` | Open a workspace |
| `coltex build` | Process documents, embed, index, update manifest |
| `coltex status` | Workspace info, health, document counts |
| `coltex validate` | Check workspace integrity |
| `coltex export` | Portable workspace archive |
| `coltex import <archive>` | Restore a workspace |

## Knowledge commands

| Command | Purpose |
|---------|---------|
| `coltex upload file.pdf` | Upload and process a source |
| `coltex search "query"` | Universal search |
| `coltex ask "question"` | Ask Knowledge — answer with sources |
| `coltex sources` | List uploaded sources |
| `coltex knowledge` | Browse knowledge objects |
| `coltex settings` | View or update workspace settings |
| `coltex health` | Knowledge Health score |
| `coltex curator` | Proactive knowledge alerts |

Supported uploads: **PDF · DOCX · Markdown · TXT · HTML · JSON**

Also available after install: `coltex` (recommended) or `python3 -m runtime` (repo root only)

---

## Workspace layout

```
MyWorkspace/
├── MyWorkspace.ctex      ← workspace manifest (auto-managed)
├── knowledge/
├── documents/
├── embeddings/
├── graph/
├── metadata/
├── settings/
└── runtime/
```

The `.ctex` file stores metadata only — never embeddings or documents. The CLI updates it automatically.

---

## License

MIT — see [LICENSE](LICENSE).
