from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: dict


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event: DomainEvent) -> None:
        raise NotImplementedError

