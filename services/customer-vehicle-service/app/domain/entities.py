from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class Vehicle:
    plate: str
    model: str
    year: int

    def __post_init__(self) -> None:
        normalized_plate = self.plate.strip().upper()
        if not normalized_plate:
            raise ValueError("Vehicle plate is required.")
        if not self.model.strip():
            raise ValueError("Vehicle model is required.")
        if self.year < 1950:
            raise ValueError("Vehicle year is invalid.")

        object.__setattr__(self, "plate", normalized_plate)
        object.__setattr__(self, "model", self.model.strip())


@dataclass(frozen=True)
class Customer:
    id: str
    name: str
    phone: str
    vehicle: Vehicle

    @classmethod
    def create(cls, name: str, phone: str, vehicle: Vehicle) -> "Customer":
        clean_name = name.strip()
        clean_phone = phone.strip()

        if not clean_name:
            raise ValueError("Customer name is required.")
        if not clean_phone:
            raise ValueError("Customer phone is required.")

        return cls(
            id=f"customer-{uuid4().hex[:8]}",
            name=clean_name,
            phone=clean_phone,
            vehicle=vehicle,
        )

