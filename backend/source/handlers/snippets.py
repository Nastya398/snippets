import time

from fastapi import APIRouter, HTTPException

from source import handlers
from source.db import get_db
from source.schemas.snippet import SnippetCreate, SnippetResponse

router = APIRouter()

@router.post("/snippets", response_model=SnippetResponse, tags=["Snippets"])
def create(snippet: SnippetCreate):
    """Создать новый сниппет"""
    return handlers.snippets.create_snippet(snippet)

@router.get("/snippets", response_model=list[SnippetResponse], tags=["Snippets"])
def list_all():
    """Получить список всех сниппетов"""
    return handlers.snippets.get_snippets()

@router.get("/snippets/{snippet_id}", response_model=SnippetResponse, tags=["Snippets"])
def get_one(snippet_id: int):
    """Получить сниппет по ID"""
    res = handlers.snippets.get_snippet(snippet_id)
    if not res:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return res

@router.get("/metrics", tags=["DevOps"])
def metrics():
    """Метрики для DevOps (Размер таблицы, время обработки)"""
    start = time.time()
    with get_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT pg_total_relation_size('snippets');")
        size = cur.fetchone()['pg_total_relation_size']
        cur.execute("SELECT count(*) FROM snippets;")
        count = cur.fetchone()['count']
    return {
        "table_size_bytes": size,
        "snippets_count": count,
        "processing_time_seconds": round(time.time() - start, 4)
    }
