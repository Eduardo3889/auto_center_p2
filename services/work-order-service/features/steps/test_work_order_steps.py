import pytest
from pytest_bdd import given, parsers, scenario, then, when

from app.application.use_cases import CreateWorkOrder
from app.domain.priority import DefaultPriorityStrategy
from app.infrastructure.memory_event_publisher import InMemoryEventPublisher
from app.infrastructure.memory_repository import InMemoryWorkOrderRepository


@scenario("../work_order.feature", "Cliente relata problema urgente no freio")
def test_customer_reports_urgent_brake_problem() -> None:
    pass


@scenario("../work_order.feature", "Cliente solicita atendimento preventivo de baixa urgencia")
def test_customer_requests_low_urgency_preventive_service() -> None:
    pass


@scenario("../work_order.feature", "Cliente relata vazamento mesmo com urgencia baixa")
def test_customer_reports_leak_with_low_urgency() -> None:
    pass


@pytest.fixture
def context() -> dict:
    return {}


def normalize_urgency(urgency: str) -> str:
    urgency_by_language = {
        "alta": "high",
        "media": "medium",
        "média": "medium",
        "baixa": "low",
    }
    normalized = urgency.strip().lower()
    return urgency_by_language.get(normalized, normalized)


@given("um cliente com veiculo cadastrado")
def customer_with_vehicle(context: dict) -> None:
    context["customer_id"] = "customer-001"
    context["vehicle_plate"] = "ABC1D23"


@when(parsers.parse("o atendente abre uma ordem com urgencia {urgency}"))
def create_order(context: dict, urgency: str) -> None:
    repository = InMemoryWorkOrderRepository()
    event_publisher = InMemoryEventPublisher()
    use_case = CreateWorkOrder(
        repository=repository,
        priority_strategy=DefaultPriorityStrategy(),
        event_publisher=event_publisher,
    )

    context["event_publisher"] = event_publisher
    context["work_order"] = use_case.execute(
        customer_id=context["customer_id"],
        vehicle_plate=context["vehicle_plate"],
        complaint="Barulho ao frear",
        urgency=normalize_urgency(urgency),
    )


@when(parsers.parse('o atendente abre uma ordem com urgencia {urgency} e reclamacao "{complaint}"'))
def create_order_with_complaint(context: dict, urgency: str, complaint: str) -> None:
    repository = InMemoryWorkOrderRepository()
    event_publisher = InMemoryEventPublisher()
    use_case = CreateWorkOrder(
        repository=repository,
        priority_strategy=DefaultPriorityStrategy(),
        event_publisher=event_publisher,
    )

    context["event_publisher"] = event_publisher
    context["work_order"] = use_case.execute(
        customer_id=context["customer_id"],
        vehicle_plate=context["vehicle_plate"],
        complaint=complaint,
        urgency=normalize_urgency(urgency),
    )


@then("a ordem deve ser criada com prioridade alta")
def order_should_have_high_priority(context: dict) -> None:
    assert context["work_order"].priority == "high"
    assert context["work_order"].status == "opened"


@then("a ordem deve ser criada com prioridade baixa")
def order_should_have_low_priority(context: dict) -> None:
    assert context["work_order"].priority == "low"
    assert context["work_order"].status == "opened"


@then("um evento de ordem criada deve ser publicado")
def event_should_be_published(context: dict) -> None:
    published_events = context["event_publisher"].events
    assert published_events[0].name == "work_order.created"
