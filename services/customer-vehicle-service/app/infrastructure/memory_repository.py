from app.domain.entities import Customer
from app.domain.repositories import CustomerRepository


class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self) -> None:
        self._customers: dict[str, Customer] = {}

    def save(self, customer: Customer) -> None:
        self._customers[customer.id] = customer

    def find_by_id(self, customer_id: str) -> Customer | None:
        return self._customers.get(customer_id)

    def list_all(self) -> list[Customer]:
        return list(self._customers.values())

