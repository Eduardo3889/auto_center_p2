# SOLID, Clean Code e Design Patterns

## Clean Code

O projeto aplica Clean Code por meio de:

- nomes claros: `CreateWorkOrder`, `RegisterCustomerWithVehicle`, `PriorityStrategy`;
- funcoes pequenas e com objetivo unico;
- separacao entre regra de negocio e API HTTP;
- validacoes no ponto certo;
- contratos explicitos por meio de classes abstratas;
- retorno de dados estruturados;
- ausencia de regra de negocio dentro dos controllers.

Exemplo de boa pratica:

```python
class RegisterCustomerWithVehicle:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def execute(self, name: str, phone: str, vehicle: Vehicle) -> Customer:
        customer = Customer.create(name=name, phone=phone, vehicle=vehicle)
        self._repository.save(customer)
        return customer
```

O caso de uso acima possui uma responsabilidade clara: registrar um cliente com veiculo.

## SOLID

### S - Single Responsibility Principle

Cada classe possui apenas um motivo para mudar.

Exemplos:

- `Vehicle` representa dados e regras do veiculo;
- `RegisterCustomerWithVehicle` executa o cadastro;
- `InMemoryCustomerRepository` armazena clientes;
- `CustomerRepository` define o contrato de persistencia.

### O - Open/Closed Principle

O sistema permite extensao sem alterar regras existentes.

Exemplo:

- a prioridade da ordem de servico usa `PriorityStrategy`;
- novas estrategias podem ser criadas sem alterar `CreateWorkOrder`.

### L - Liskov Substitution Principle

Implementacoes concretas podem substituir contratos sem quebrar o comportamento.

Exemplo:

- `InMemoryCustomerRepository` pode ser trocado por `PostgresCustomerRepository` desde que respeite `CustomerRepository`.

### I - Interface Segregation Principle

Interfaces sao pequenas e especificas.

Exemplo:

- `CustomerRepository` define apenas `save` e `find_by_id`;
- `WorkOrderRepository` define apenas operacoes de ordem de servico.

### D - Dependency Inversion Principle

Casos de uso dependem de abstracoes, nao de implementacoes.

Exemplo:

```python
class CreateWorkOrder:
    def __init__(
        self,
        repository: WorkOrderRepository,
        priority_strategy: PriorityStrategy,
        event_publisher: EventPublisher,
    ) -> None:
        self._repository = repository
        self._priority_strategy = priority_strategy
        self._event_publisher = event_publisher
```

## Design Patterns aplicados

### 1. Repository

Usado para isolar a persistencia.

Arquivos:

- `services/customer-vehicle-service/app/domain/repositories.py`
- `services/work-order-service/app/domain/repositories.py`

Beneficio:

- a regra de negocio nao depende de banco de dados;
- facilita testes com repositorio em memoria.

### 2. Factory Method

Usado para criar entidades validas.

Exemplo:

- `Customer.create(...)`
- `WorkOrder.open(...)`

Beneficio:

- centraliza regras de criacao;
- evita objetos invalidos espalhados pelo sistema.

### 3. Strategy

Usado para calcular prioridade da ordem de servico.

Exemplo:

- `PriorityStrategy`
- `DefaultPriorityStrategy`

Beneficio:

- permite mudar ou adicionar regras de prioridade sem alterar o caso de uso principal.

### 4. Facade

Usado no API Gateway.

Exemplo:

- `WorkshopGatewayFacade`

Beneficio:

- consumidores externos chamam uma interface simples;
- o Gateway esconde a complexidade dos microsservicos internos.

### 5. Observer / Event Publisher

Usado quando uma ordem de servico e criada.

Exemplo:

- `EventPublisher`
- `InMemoryEventPublisher`

Beneficio:

- permite reagir a eventos de negocio sem acoplar o caso de uso a notificacoes, logs ou auditoria.

## Evidencias de Clean Code nos arquivos

| Evidencia | Exemplo |
| --- | --- |
| Nomes expressivos | `RegisterCustomerWithVehicle`, `CreateWorkOrder` |
| Baixo acoplamento | casos de uso dependem de interfaces |
| Alta coesao | cada classe possui responsabilidade unica |
| Testabilidade | repositorios em memoria e interfaces pequenas |
| Organizacao | camadas separadas por Clean Architecture |

