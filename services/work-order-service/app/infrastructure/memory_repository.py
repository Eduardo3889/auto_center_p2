from app.domain.entities import WorkOrder
from app.domain.repositories import WorkOrderRepository


class InMemoryWorkOrderRepository(WorkOrderRepository):
    def __init__(self) -> None:
        self._orders: dict[str, WorkOrder] = {}

    def save(self, work_order: WorkOrder) -> None:
        self._orders[work_order.id] = work_order

    def find_by_id(self, work_order_id: str) -> WorkOrder | None:
        return self._orders.get(work_order_id)

    def list_all(self) -> list[WorkOrder]:
        return list(self._orders.values())

