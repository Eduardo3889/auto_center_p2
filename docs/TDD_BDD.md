# TDD e BDD

## TDD - Test Driven Development

TDD e uma tecnica em que o desenvolvimento segue o ciclo:

1. escrever um teste que falha;
2. implementar o minimo necessario para passar;
3. refatorar mantendo os testes verdes.

No projeto, os testes unitarios focam nas regras de negocio antes da API HTTP.

## Exemplos de testes TDD

### Cadastro de cliente e veiculo

Arquivo:

```text
services/customer-vehicle-service/tests/test_register_customer_with_vehicle.py
```

Cenario testado:

- dado um cliente com nome, telefone e veiculo;
- quando o caso de uso e executado;
- entao o cliente e salvo;
- e a placa e normalizada para maiusculo.

### Criacao de ordem de servico

Arquivo:

```text
services/work-order-service/tests/test_create_work_order.py
```

Cenario testado:

- dado uma reclamacao urgente;
- quando a ordem de servico e aberta;
- entao a prioridade deve ser alta;
- e um evento de ordem criada deve ser publicado.

## BDD - Behavior Driven Development

BDD descreve comportamento em linguagem proxima do negocio, usando o formato Gherkin:

```gherkin
Funcionalidade: Abertura de ordem de servico
  Cenario: Cliente relata problema urgente no freio
    Dado um cliente com veiculo cadastrado
    Quando o atendente abre uma ordem com urgencia alta
    Entao a ordem deve ser criada com prioridade alta
```

## Arquivos BDD

| Arquivo | Objetivo |
| --- | --- |
| `services/work-order-service/features/work_order.feature` | Descrever comportamentos esperados da abertura de ordem |
| `services/work-order-service/features/steps/test_work_order_steps.py` | Automatizar os cenarios em pytest-bdd |

## Cenarios BDD implementados

1. Cliente relata problema urgente no freio e a ordem recebe prioridade alta.
2. Cliente solicita atendimento preventivo de baixa urgencia e a ordem recebe prioridade baixa.
3. Cliente relata vazamento mesmo com urgencia baixa e a ordem recebe prioridade alta.

## Integracao continua

O projeto possui workflow em:

```text
.github/workflows/ci.yml
```

Esse workflow instala as dependencias dos servicos e executa os testes automaticamente em push ou pull request para a branch `main`.

## Justificativa

TDD foi usado para garantir regras de negocio testaveis sem depender do servidor HTTP. BDD foi usado para comunicar o comportamento esperado em uma linguagem compreensivel para usuarios de negocio, professores e desenvolvedores.
