import pytest

from app.application.use_cases import SendNotification
from app.infrastructure.memory_repository import InMemoryNotificationRepository


def test_send_notification_registers_sent_notification() -> None:
    repository = InMemoryNotificationRepository()
    use_case = SendNotification(repository)

    notification = use_case.execute(
        customer_name="Joao Silva",
        phone="21999990000",
        message="Seu veiculo entrou em diagnostico.",
    )

    assert notification.status == "sent"
    assert repository.list_all() == [notification]


def test_send_notification_requires_message() -> None:
    repository = InMemoryNotificationRepository()
    use_case = SendNotification(repository)

    with pytest.raises(ValueError, match="Message is required"):
        use_case.execute(
            customer_name="Joao Silva",
            phone="21999990000",
            message="",
        )

