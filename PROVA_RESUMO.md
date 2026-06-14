# RESUMO_GERAL_PROVA

## Tema

Sistema de gestao de atendimento para a oficina **Auto Center Marica**.

## Problema

A oficina tem bastante dificuldade para controlar clientes, veiculos, ordens de servico e comunicacao com clientes usando planilhas e anotacoes manuais,acaba atrapalhando e atrasando bastante o trabalho na oficina.

## Solucao

Uma plataforma baseada em microsservicos, com API Gateway, cadastro de clientes e veiculos, ordens de servico e notificacoes.

## Microsservicos

1. **API Gateway**: ponto unico de entrada.
2. **Customer Vehicle Service**: cadastro de clientes e veiculos.
3. **Work Order Service**: abertura e consulta de ordens de servico.
4. **Notification Service**: envio simulado de notificacoes.

## Arquitetura Limpa

Cada servico separa:

- `domain`: entidades, contratos e regras;
- `application`: casos de uso;
- `infrastructure`: implementacoes concretas;
- `interfaces`: API HTTP.

## SOLID

- SRP: cada classe possui responsabilidade unica.
- OCP: estrategias de prioridade podem ser trocadas sem alterar o caso de uso.
- LSP: repositorios concretos substituem contratos abstratos.
- ISP: interfaces pequenas e especificas.
- DIP: casos de uso dependem de abstracoes.

## Design Patterns

- Repository;
- Factory Method;
- Strategy;
- Facade;
- Observer / Event Publisher.

## TDD

Os testes unitarios validam regras de negocio sem depender da API HTTP.

Arquivos principais:

- `services/customer-vehicle-service/tests/test_register_customer_with_vehicle.py`
- `services/work-order-service/tests/test_create_work_order.py`
- `services/notification-service/tests/test_send_notification.py`

## BDD

Cenarios de comportamento:

- cliente com veiculo cadastrado e problema urgente no freio;
- atendimento preventivo de baixa urgencia;
- vazamento com urgencia baixa, mas prioridade alta por regra de negocio.

Arquivo:

- `services/work-order-service/features/work_order.feature`

## Docker

O arquivo `docker-compose.yml` sobe os quatro servicos.

Comando:

bash
docker compose up --build

O Compose tambem possui healthchecks para verificar se cada microsservico esta respondendo.


## CI

O workflow `.github/workflows/ci.yml` executa os testes automaticamente no GitHub Actions.
