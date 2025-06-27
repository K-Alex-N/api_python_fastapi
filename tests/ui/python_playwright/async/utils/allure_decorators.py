from typing import TypeVar, Type, Callable
import allure

T = TypeVar("T")

def epic(name: str) -> Callable[[Type[T]], Type[T]]:
    return allure.epic(name)

def feature(name: str) -> Callable[[Type[T]], Type[T]]:
    return allure.feature(name)

def story(name: str) -> Callable[[Type[T]], Type[T]]:
    return allure.story(name)

def tag(*tags: str) -> Callable[[Type[T]], Type[T]]:
    return allure.tag(*tags)

def severity(level: str) -> Callable[[Type[T]], Type[T]]:
    return allure.severity(level)

