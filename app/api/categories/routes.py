from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from .models import Category
from .schemas import CategoryCreate, CategoryOut, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryOut])
async def get_categories() -> List[CategoryOut]:
    cats = await Category.find_all(fetch_links=True).to_list()
    return CategoryOut.from_model_list(cats)


@router.post("/", response_model=CategoryOut)
async def create_category(category: CategoryCreate) -> CategoryOut:
    cat = Category(**category.model_dump())
    await cat.insert()  # type: ignore
    return CategoryOut.from_model(cat)


@router.get("/{category_id}", response_model=CategoryOut)
async def get_category(category_id: UUID) -> CategoryOut:
    cat = await Category.get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return CategoryOut.from_model(cat)


@router.patch("/{category_id}", response_model=CategoryOut)
async def update_category(category_id: UUID, category: CategoryUpdate) -> CategoryOut:
    cat = await Category.get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")

    if category.name is not None:
        cat.name = category.name
    if category.type is not None:
        cat.type = category.type

    await cat.save()  # type: ignore
    return CategoryOut.from_model(cat)


@router.delete("/{category_id}", response_model=dict)
async def delete_category(category_id: UUID) -> dict:
    cat = await Category.get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")

    await cat.delete()  # type: ignore
    return {"message": "Category deleted successfully"}
