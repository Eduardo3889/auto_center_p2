from app.domain.entities import Notification
from app.domain.repositories import NotificationRepository


class InMemoryNotificationRepository(NotificationRepository):
    def __init__(self) -> None:
        self._notifications: dict[str, Notification] = {}

    def save(self, notification: Notification) -> None:
        self._notifications[notification.id] = notification

    def list_all(self) -> list[Notification]:
        return list(self._notifications.values())

