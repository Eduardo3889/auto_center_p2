from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.application.use_cases import CreateWorkOrder, ListWorkOrders
from app.domain.entities import WorkOrder
from app.domain.priority import DefaultPriorityStrategy
from app.infrastructure.memory_event_publisher import InMemoryEventPublisher
from app.infrastructure.memory_repository import InMemoryWorkOrderRepository


class WorkOrderInput(BaseModel):
    customer_id: str = Field(..., examples=["customer-001"])
    vehicle_plate: str = Field(..., examples=["ABC1D23"])
    complaint: str = Field(..., examples=["Barulho ao frear"])
    urgency: str = Field(..., examples=["high"])


router = APIRouter()
repository = InMemoryWorkOrderRepository()
event_publisher = InMemoryEventPublisher()
create_work_order = CreateWorkOrder(
    repository=repository,
    priority_strategy=DefaultPriorityStrategy(),
    event_publisher=event_publisher,
)
list_work_orders = ListWorkOrders(repository)


def serialize_work_order(work_order: WorkOrder) -> dict:
    return {
        "id": work_order.id,
        "customer_id": work_order.customer_id,
        "vehicle_plate": work_order.vehicle_plate,
        "complaint": work_order.complaint,
        "urgency": work_order.urgency,
        "priority": work_order.priority,
        "status": work_order.status,
        "created_at": work_order.created_at.isoformat(),
    }


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "work-order-service"}


@router.post("/work-orders", status_code=status.HTTP_201_CREATED)
def create_order(payload: WorkOrderInput) -> dict:
    try:
        work_order = create_work_order.execute(
            customer_id=payload.customer_id,
            vehicle_plate=payload.vehicle_plate,
            complaint=payload.complaint,
            urgency=payload.urgency,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return serialize_work_order(work_order)


@router.get("/work-orders")
def get_orders() -> list[dict]:
    return [serialize_work_order(order) for order in list_work_orders.execute()]

@router.get("/events")
def get_events() -> list[dict]:
    return [
        {"name": event.name, "payload": event.payload}
        for event in event_publisher.events
    ]

