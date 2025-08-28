from fastapi import APIRouter, Query
from typing import Dict, Any
from .db import get_db

router = APIRouter()

@router.get("/")
def get_recipes(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1)
) -> Dict[str, Any]:
    offset = (page - 1) * limit
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM recipes")
    total = cur.fetchone()[0]
    cur.execute(
        "SELECT id, title, cuisine, rating, prep_time, cook_time, total_time, description, nutrients, serves "
        "FROM recipes ORDER BY rating DESC NULLS LAST LIMIT %s OFFSET %s",
        (limit, offset)
    )
    results = cur.fetchall()
    cur.close()
    conn.close()
    data = [
        {
            "id": r[0],
            "title": r[1],
            "cuisine": r[2],
            "rating": r[3],
            "prep_time": r[4],
            "cook_time": r[5],
            "total_time": r[6],
            "description": r[7],
            "nutrients": r[8],
            "serves": r[9]
        }
        for r in results
    ]
    return {"page": page, "limit": limit, "total": total, "recipes": data}
