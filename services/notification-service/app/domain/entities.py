from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class Notification:
    id: str
    customer_name: str
    phone: str
    message: str
    status: str

    @classmethod
    def create(cls, customer_name: str, phone: str, message: str) -> "Notification":
        if not customer_name.strip():
            raise ValueError("Customer name is required.")
        if not phone.strip():
            raise ValueError("Phone is required.")
        if not message.strip():
            raise ValueError("Message is required.")

        return cls(
            id=f"notification-{uuid4().hex[:8]}",
            customer_name=customer_name.strip(),
            phone=phone.strip(),
            message=message.strip(),
            status="sent",
        )

