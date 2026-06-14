from abc import ABC, abstractmethod

from app.domain.entities import WorkOrder


class WorkOrderRepository(ABC):
    @abstractmethod
    def save(self, work_order: WorkOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, work_order_id: str) -> WorkOrder | None:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[WorkOrder]:
        raise NotImplementedError

