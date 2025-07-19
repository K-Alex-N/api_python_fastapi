from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.api.categories.models import Category
from app.api.categories.schemas import CategoryCreate, CategoryOut, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryOut])
async def get_categories() -> List[CategoryOut]:
    cats = await Category.find_all(fetch_links=True).to_list()
    return [CategoryOut.from_model(cat) for cat in cats]


@router.get("/{category_id}", response_model=CategoryOut)
async def get_category(category_id: UUID) -> CategoryOut:
    cat = await Category.get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return CategoryOut.from_model(cat)


@router.post("/", response_model=CategoryOut)
async def create_category(category: CategoryCreate) -> CategoryOut:
    cat = Category(**category.model_dump())
    await cat.insert()  # type: ignore
    return CategoryOut.from_model(cat)


# @router.patch("/{id}", response_model=CategoryOut)
# async def update_category(cat_id: UUID, category: CategoryCreate) -> CategoryOut:
#     cat = await Category.get(cat_id)
#     if not cat:
#         raise HTTPException(status_code=404, detail="Category not found")
#     await cat.update(category)
#     return CategoryOut.from_model(cat)


@router.patch("/{category_id}", response_model=CategoryOut)
async def update_category(category_id: UUID, data: CategoryUpdate) -> CategoryOut:
    cat = await Category.get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")

    if data.name is not None:
        cat.name = data.name
    if data.type is not None:
        cat.type = data.type

    await cat.save() # type: ignore
    # return CategoryOut.model_validate(cat)
    return CategoryOut.from_model(cat)
