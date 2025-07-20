from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Type, List, Iterable
import logging

# Минималистичный логгер
logger = logging.getLogger("out_model")
logger.setLevel(logging.INFO)
if not logger.handlers:
    logger.addHandler(logging.StreamHandler())

T = TypeVar("T", bound="BaseOutModel")


class BaseOutModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, # Позволяет строить схему из объекта (например, Beanie Document)
        arbitrary_types_allowed=True # Разрешает сложные типы (Link, ObjectId, UUID)
    )

    @classmethod
    def from_model(cls: Type[T], model: object) -> T:
        instance = cls.model_validate(model)
        logger.info(f"{cls.__name__}: created object")
        return instance

    @classmethod
    def from_model_list(cls: Type[T], models: Iterable[object]) -> List[T]:
        result = [cls.from_model(m) for m in models]
        logger.info(f"{cls.__name__}: created {len(result)} objects")
        return result
