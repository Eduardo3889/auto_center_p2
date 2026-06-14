from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(frozen=True)
class WorkOrder:
    id: str
    customer_id: str
    vehicle_plate: str
    complaint: str
    urgency: str
    priority: str
    status: str
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    @classmethod
    def open(
        cls,
        customer_id: str,
        vehicle_plate: str,
        complaint: str,
        urgency: str,
        priority: str,
    ) -> "WorkOrder":
        if not customer_id.strip():
            raise ValueError("Customer id is required.")
        if not vehicle_plate.strip():
            raise ValueError("Vehicle plate is required.")
        if not complaint.strip():
            raise ValueError("Complaint is required.")

        return cls(
            id=f"order-{uuid4().hex[:8]}",
            customer_id=customer_id.strip(),
            vehicle_plate=vehicle_plate.strip().upper(),
            complaint=complaint.strip(),
            urgency=urgency.strip().lower(),
            priority=priority,
            status="opened",
        )

