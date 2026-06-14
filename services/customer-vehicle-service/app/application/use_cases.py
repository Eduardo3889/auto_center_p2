from app.domain.entities import Customer, Vehicle
from app.domain.repositories import CustomerRepository


class RegisterCustomerWithVehicle:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def execute(self, name: str, phone: str, vehicle: Vehicle) -> Customer:
        customer = Customer.create(name=name, phone=phone, vehicle=vehicle)
        self._repository.save(customer)
        return customer


class GetCustomer:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def execute(self, customer_id: str) -> Customer | None:
        return self._repository.find_by_id(customer_id)


class ListCustomers:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def execute(self) -> list[Customer]:
        return self._repository.list_all()

