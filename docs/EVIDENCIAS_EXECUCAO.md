# Evidencias de Execucao e Publicacao

Este arquivo serve como checklist para demonstrar a aplicacao durante a apresentacao da prova.

## 1. Execucao local com Docker

Comando:

```bash
docker compose up --build
```

Evidencias esperadas:

- containers `api-gateway`, `customer-vehicle-service`, `work-order-service` e `notification-service` iniciados;
- healthchecks marcados como saudaveis;
- Swagger do Gateway em `http://localhost:8000/docs`;
- Swagger dos microsservicos nas portas `8001`, `8002` e `8003`.

## 2. Testes TDD

Executar:

```bash
cd services/customer-vehicle-service
pytest

cd ../work-order-service
pytest

cd ../notification-service
pytest
```

Evidencias esperadas:

- testes unitarios passando;
- regra de normalizacao de placa validada;
- prioridade alta para freio e vazamento validada;
- prioridade baixa para atendimento preventivo validada;
- notificacao registrada com status `sent`.

## 3. Testes BDD

Executar:

```bash
cd services/work-order-service
pytest features
```

Cenarios cobertos:

- problema urgente no freio gera prioridade alta;
- atendimento preventivo de baixa urgencia gera prioridade baixa;
- vazamento gera prioridade alta mesmo com urgencia baixa.

## 4. Deploy em servidor

Arquivo preparado:

```text
render.yaml
```

Passos:

1. enviar o projeto para o GitHub;
2. criar Blueprint no Render;
3. selecionar `render.yaml`;
4. aguardar a publicacao dos quatro servicos;
5. copiar o link publico do Gateway;
6. substituir o placeholder no `README.md`.

Campo a preencher apos publicacao:

```text
Link publicado: https://auto-center-marica-gateway.onrender.com
```

## 5. Evidencias para anexar na entrega

Recomenda-se anexar:

- print do Swagger do Gateway;
- print do `docker compose ps`;
- print dos testes `pytest` passando;
- print do Blueprint publicado no Render;
- link publico ativo do Gateway.

