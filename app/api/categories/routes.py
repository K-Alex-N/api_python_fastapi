from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.api.categories.models import Category
from app.api.categories.schemas import CategoryCreate, CategoryOut

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryOut])
async def get_categories() -> List[CategoryOut]:
    cats = await Category.find_all(fetch_links=True).to_list()
    return cats  # type: ignore


@router.get("/{id}", response_model=CategoryOut)
async def get_category(id: UUID) -> CategoryOut:
    cat = await Category.get(id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat  # type: ignore


@router.post("/", response_model=CategoryOut)
async def create_category(category: CategoryCreate) -> CategoryOut:
    cat = Category(**category.model_dump())
    await cat.insert()
    return cat  # type: ignore


