from collections.abc import Iterable
from typing import TypeVar

from pydantic import BaseModel, ConfigDict

# import logging
#
## Минималистичный логгер
# logger = logging.getLogger("out_model")
# logger.setLevel(logging.INFO)
# if not logger.handlers:
#     logger.addHandler(logging.StreamHandler())

T = TypeVar("T", bound="BaseOutModel")


class BaseOutModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_model(cls: type[T], model: object) -> T:
        instance = cls.model_validate(model)
        # logger.info(f"{cls.__name__}: created object")
        return instance

    @classmethod
    def from_model_list(cls: type[T], models: Iterable[object]) -> list[T]:
        result = [cls.from_model(m) for m in models]
        # logger.info(f"{cls.__name__}: created {len(result)} objects")
        return result
