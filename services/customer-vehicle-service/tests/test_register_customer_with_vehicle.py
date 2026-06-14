import pytest

from app.application.use_cases import RegisterCustomerWithVehicle
from app.domain.entities import Vehicle
from app.infrastructure.memory_repository import InMemoryCustomerRepository


def test_register_customer_with_vehicle_normalizes_plate_and_saves_customer() -> None:
    repository = InMemoryCustomerRepository()
    use_case = RegisterCustomerWithVehicle(repository)
    vehicle = Vehicle(plate="abc1d23", model="Fiat Argo", year=2020)

    customer = use_case.execute(
        name="Joao Silva",
        phone="21999990000",
        vehicle=vehicle,
    )

    saved_customer = repository.find_by_id(customer.id)
    assert saved_customer is not None
    assert saved_customer.name == "Joao Silva"
    assert saved_customer.vehicle.plate == "ABC1D23"


def test_register_customer_rejects_vehicle_with_invalid_year() -> None:
    with pytest.raises(ValueError, match="Vehicle year is invalid"):
        Vehicle(plate="ABC1D23", model="Fiat Argo", year=1940)

