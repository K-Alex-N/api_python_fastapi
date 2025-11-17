import logging
from collections.abc import Iterable
from typing import Any, TypeVar

from pydantic import BaseModel, ConfigDict

logger = logging.getLogger(__name__)

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
