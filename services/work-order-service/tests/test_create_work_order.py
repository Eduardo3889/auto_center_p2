from app.application.use_cases import CreateWorkOrder
from app.domain.priority import DefaultPriorityStrategy
from app.infrastructure.memory_event_publisher import InMemoryEventPublisher
from app.infrastructure.memory_repository import InMemoryWorkOrderRepository


def test_create_work_order_with_high_urgency_sets_high_priority() -> None:
    repository = InMemoryWorkOrderRepository()
    event_publisher = InMemoryEventPublisher()
    use_case = CreateWorkOrder(
        repository=repository,
        priority_strategy=DefaultPriorityStrategy(),
        event_publisher=event_publisher,
    )

    work_order = use_case.execute(
        customer_id="customer-001",
        vehicle_plate="abc1d23",
        complaint="Barulho ao frear",
        urgency="high",
    )

    assert work_order.status == "opened"
    assert work_order.priority == "high"
    assert work_order.vehicle_plate == "ABC1D23"
    assert repository.find_by_id(work_order.id) == work_order
    assert event_publisher.events[0].name == "work_order.created"


def test_default_priority_strategy_prioritizes_brake_complaints() -> None:
    strategy = DefaultPriorityStrategy()

    priority = strategy.calculate(
        complaint="Pedal de freio baixo",
        urgency="low",
    )

    assert priority == "high"


def test_default_priority_strategy_keeps_low_priority_for_preventive_service() -> None:
    strategy = DefaultPriorityStrategy()

    priority = strategy.calculate(
        complaint="Troca de oleo",
        urgency="low",
    )

    assert priority == "low"


def test_default_priority_strategy_prioritizes_leak_even_with_low_urgency() -> None:
    strategy = DefaultPriorityStrategy()

    priority = strategy.calculate(
        complaint="Vazamento de oleo",
        urgency="low",
    )

    assert priority == "high"
