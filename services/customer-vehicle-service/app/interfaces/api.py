from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.application.use_cases import GetCustomer, ListCustomers, RegisterCustomerWithVehicle
from app.domain.entities import Customer, Vehicle
from app.infrastructure.memory_repository import InMemoryCustomerRepository


class VehicleInput(BaseModel):
    plate: str = Field(..., examples=["ABC1D23"])
    model: str = Field(..., examples=["Fiat Argo"])
    year: int = Field(..., examples=[2020])


class CustomerInput(BaseModel):
    name: str = Field(..., examples=["Joao Silva"])
    phone: str = Field(..., examples=["21999990000"])
    vehicle: VehicleInput


router = APIRouter()
repository = InMemoryCustomerRepository()
register_customer = RegisterCustomerWithVehicle(repository)
get_customer = GetCustomer(repository)
list_customers = ListCustomers(repository)


def serialize_customer(customer: Customer) -> dict:
    return {
        "id": customer.id,
        "name": customer.name,
        "phone": customer.phone,
        "vehicle": {
            "plate": customer.vehicle.plate,
            "model": customer.vehicle.model,
            "year": customer.vehicle.year,
        },
    }


@router.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "customer-vehicle-service"}


@router.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer(payload: CustomerInput) -> dict:
    try:
        vehicle = Vehicle(
            plate=payload.vehicle.plate,
            model=payload.vehicle.model,
            year=payload.vehicle.year,
        )
        customer = register_customer.execute(
            name=payload.name,
            phone=payload.phone,
            vehicle=vehicle,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return serialize_customer(customer)


@router.get("/customers")
def get_customers() -> list[dict]:
    return [serialize_customer(customer) for customer in list_customers.execute()]


@router.get("/customers/{customer_id}")
def get_customer_by_id(customer_id: str) -> dict:
    customer = get_customer.execute(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found.")

    return serialize_customer(customer)

