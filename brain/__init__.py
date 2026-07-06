"""Zypher — Mega RAG Database engine."""

from brain.brain import Zypher
from brain.types import Document, RetrievalResult, ScoredDocument

__version__ = "3.0.0"
__all__ = [
    "Zypher",
    "Document",
    "RetrievalResult",
    "ScoredDocument",
]
