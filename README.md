# Auto Center Marica - Solucao de Software para Oficina Mecanica

Tudo para demonstrar Clean Code, SOLID, Design Patterns, TDD, BDD, Arquitetura Limpa, Microsservicos, Docker e Deploy em servidor.

## 1. Problema escolhido

A oficina mecanica ficticia **Auto Center Marica** atende clientes por telefone, WhatsApp e presencialmente. O controle de clientes, veiculos, orcamentos e ordens de servico ainda e feito em planilhas e anotacoes manuais.

Esse processo gera alguns problemas que sao comuns:

- perda de historico dos veiculos;
- dificuldade para consultar servicos anteriores;
- atrasos na comunicacao com clientes;
- falhas no acompanhamento de orcamentos;
- dificuldade para priorizar ordens de servico;
- ausencia de indicadores para gestao da oficina.

## 2. Solucao proposta

Foi proposta uma plataforma chamada **Auto Center Marica OS**, composta por microsservicos para cadastro de clientes e veiculos, abertura e acompanhamento de ordens de servico e envio de notificacoes para uma execucao e organizacao mais fluida da oficina.

A solucao permite:

- cadastrar clientes e seus veiculos;
- abrir ordens de servico;
- calcular prioridade de atendimento;
- registrar diagnosticos, itens de servico e status;
- enviar notificacoes para o cliente;
- consultar informacoes por meio de um API Gateway;
- executar tudo localmente com Docker Compose;
- publicar em Render, Railway, AWS, Azure ou Google Cloud.

## 3. Divisao em microsservicos

| Microsservico | Responsabilidade | Porta |
| --- | --- | --- |
| `api-gateway` | Entrada unica para consumidores externos | `8000` |
| `customer-vehicle-service` | Cadastro de clientes e veiculos | `8001` |
| `work-order-service` | Criacao e acompanhamento de ordens de servico | `8002` |
| `notification-service` | Envio simulado de notificacoes | `8003` |

## 4. Estrutura do projeto

```text
auto-center-marica-prova/
  README.md
  docker-compose.yml
  .env.example
  render.yaml
  docs/
    ARQUITETURA.md
    DEPLOY.md
    EVIDENCIAS_EXECUCAO.md
    SOLID_CLEAN_CODE_PATTERNS.md
    TDD_BDD.md
  .github/
    workflows/
      ci.yml
  services/
    api-gateway/
    customer-vehicle-service/
    work-order-service/
    notification-service/
```

Cada servico foi organizado com base em Arquitetura Limpa e estruturada:

```text
app/
  domain/          Regras de negocio puras
  application/     Casos de uso
  infrastructure/  Implementacoes externas, como repositorios
  interfaces/      API HTTP, DTOs e controllers
  main.py          Inicializacao do servico
```

## 5. Conceitos obrigatorios demonstrados

| Conceito | Onde aparece |
| --- | --- |
| Clean Code | nomes claros, funcoes pequenas, validacoes explicitas, separacao por responsabilidade |
| SOLID | entidades, casos de uso, interfaces de repositorio e estrategias de prioridade |
| Design Patterns | Repository, Factory Method, Strategy, Facade, Observer/Event Publisher |
| TDD | testes unitarios em `tests/` para regras de negocio antes dos endpoints |
| BDD | cenarios Gherkin em `features/` |
| Arquitetura Limpa | separacao `domain`, `application`, `infrastructure`, `interfaces` |
| Microsservicos | quatro servicos independentes |
| Docker | `Dockerfile` por servico, healthchecks e `docker-compose.yml` |
| Deploy | `render.yaml`, CI e roteiro em `docs/DEPLOY.md` |

## 6. Como executar localmente

Requisitos:

- Docker
- Docker Compose

Comandos:

```bash
docker compose up --build
```

URLs locais:

- API Gateway: <http://localhost:8000/docs>
- Clientes e veiculos: <http://localhost:8001/docs>
- Ordens de servico: <http://localhost:8002/docs>
- Notificacoes: <http://localhost:8003/docs>

## 7. Exemplos de uso

Criar cliente e veiculo:

```bash
curl -X POST http://localhost:8001/customers \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Joao Silva\",\"phone\":\"21999990000\",\"vehicle\":{\"plate\":\"ABC1D23\",\"model\":\"Fiat Argo\",\"year\":2020}}"
```

Criar ordem de servico:

```bash
curl -X POST http://localhost:8002/work-orders \
  -H "Content-Type: application/json" \
  -d "{\"customer_id\":\"customer-001\",\"vehicle_plate\":\"ABC1D23\",\"complaint\":\"Barulho ao frear\",\"urgency\":\"high\"}"
```

Enviar notificacao:

```bash
curl -X POST http://localhost:8003/notifications \
  -H "Content-Type: application/json" \
  -d "{\"customer_name\":\"Joao Silva\",\"phone\":\"21999990000\",\"message\":\"Seu veiculo entrou em diagnostico.\"}"
```

## 8. Testes

Exemplo para rodar os testes de um servico:

```bash
cd services/customer-vehicle-service
pytest
```

Exemplo para BDD:

```bash
cd services/work-order-service
pytest features
```

O projeto tambem possui workflow de CI em `.github/workflows/ci.yml` para executar testes automaticamente no GitHub Actions.

## 9. Link de acesso publicado

Campo para entrega final apos deploy real:

```text
https://auto-center-marica-gateway.onrender.com
```

Observacao: o arquivo `render.yaml` ja esta preparado para publicacao. Para que o link fique ativo, e necessario conectar este projeto a uma conta Render, Railway, AWS, Azure, Google Cloud ou similar. O roteiro completo esta em `docs/DEPLOY.md`.

## 10. Evidencias de execucao

O arquivo `docs/EVIDENCIAS_EXECUCAO.md` lista os comandos e prints recomendados para comprovar:

- containers rodando;
- healthchecks saudaveis;
- testes unitarios e BDD passando;
- Swagger aberto;
- deploy publicado.

## 11. Justificativa tecnica resumida

A arquitetura foi escolhida para separar regras de negocio da tecnologia utilizada. A oficina pode mudar banco de dados, provedor de deploy, mensageria ou framework HTTP sem reescrever o nucleo do sistema. A divisao em microsservicos permite evoluir cadastro, ordens de servico e notificacoes de forma independente, reduzindo acoplamento e facilitando manutencao.
