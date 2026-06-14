from app.domain.entities import Notification
from app.domain.repositories import NotificationRepository


class SendNotification:
    def __init__(self, repository: NotificationRepository) -> None:
        self._repository = repository

    def execute(self, customer_name: str, phone: str, message: str) -> Notification:
        notification = Notification.create(
            customer_name=customer_name,
            phone=phone,
            message=message,
        )
        self._repository.save(notification)
        return notification


class ListNotifications:
    def __init__(self, repository: NotificationRepository) -> None:
        self._repository = repository

    def execute(self) -> list[Notification]:
        return self._repository.list_all()

