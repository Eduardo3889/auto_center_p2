from app.domain.entities import WorkOrder
from app.domain.events import DomainEvent, EventPublisher
from app.domain.priority import PriorityStrategy
from app.domain.repositories import WorkOrderRepository


class CreateWorkOrder:
    def __init__(
        self,
        repository: WorkOrderRepository,
        priority_strategy: PriorityStrategy,
        event_publisher: EventPublisher,
    ) -> None:
        self._repository = repository
        self._priority_strategy = priority_strategy
        self._event_publisher = event_publisher

    def execute(
        self,
        customer_id: str,
        vehicle_plate: str,
        complaint: str,
        urgency: str,
    ) -> WorkOrder:
        priority = self._priority_strategy.calculate(
            complaint=complaint,
            urgency=urgency,
        )
        work_order = WorkOrder.open(
            customer_id=customer_id,
            vehicle_plate=vehicle_plate,
            complaint=complaint,
            urgency=urgency,
            priority=priority,
        )

        self._repository.save(work_order)
        self._event_publisher.publish(
            DomainEvent(
                name="work_order.created",
                payload={
                    "work_order_id": work_order.id,
                    "customer_id": work_order.customer_id,
                    "priority": work_order.priority,
                },
            )
        )
        return work_order


class ListWorkOrders:
    def __init__(self, repository: WorkOrderRepository) -> None:
        self._repository = repository

    def execute(self) -> list[WorkOrder]:
        return self._repository.list_all()

