from abc import ABC, abstractmethod

from app.domain.entities import Notification


class NotificationRepository(ABC):
    @abstractmethod
    def save(self, notification: Notification) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Notification]:
        raise NotImplementedError

