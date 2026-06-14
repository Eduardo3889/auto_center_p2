from abc import ABC, abstractmethod

from app.domain.entities import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer: Customer) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, customer_id: str) -> Customer | None:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Customer]:
        raise NotImplementedError

