from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.application.use_cases import ListNotifications, SendNotification
from app.domain.entities import Notification
from app.infrastructure.memory_repository import InMemoryNotificationRepository


class NotificationInput(BaseModel):
    customer_name: str = Field(..., examples=["Joao Silva"])
    phone: str = Field(..., examples=["21999990000"])
    message: str = Field(..., examples=["Seu veiculo entrou em diagnostico."])


router = APIRouter()
repository = InMemoryNotificationRepository()
send_notification = SendNotification(repository)
list_notifications = ListNotifications(repository)


def serialize_notification(notification: Notification) -> dict:
    return {
        "id": notification.id,
        "customer_name": notification.customer_name,
        "phone": notification.phone,
        "message": notification.message,
        "status": notification.status,
    }


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "notification-service"}


@router.post("/notifications", status_code=status.HTTP_201_CREATED)
def create_notification(payload: NotificationInput) -> dict:
    try:
        notification = send_notification.execute(
            customer_name=payload.customer_name,
            phone=payload.phone,
            message=payload.message,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return serialize_notification(notification)


@router.get("/notifications")
def get_notifications() -> list[dict]:
    return [
        serialize_notification(notification)
        for notification in list_notifications.execute()
    ]

