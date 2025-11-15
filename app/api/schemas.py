from collections.abc import Iterable
from typing import TypeVar, Any

from pydantic import BaseModel, ConfigDict


T = TypeVar("T", bound="BaseOutModel")


class BaseOutModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_model(cls: type[T], model: Any) -> T:
        instance = cls.model_validate(model)
        return instance

    @classmethod
    def from_model_list(cls: type[T], models: Iterable[object]) -> list[T]:
        result = [cls.from_model(m) for m in models]
        return result
