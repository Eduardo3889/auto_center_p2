# Deploy em Servidor

## Plataforma sugerida

Para a entrega academica, a plataforma recomendada e **Render**, pois aceita deploy via Docker, oferece plano gratuito e permite configurar multiplos servicos a partir de um repositocio Git.

Tambem seria possivel publicar em:

- Railway;
- Heroku;
- AWS ECS;
- Google Cloud Run;
- Azure Container Apps.

## Link esperado

Depois do deploy, o link publico do Gateway devera ter formato semelhante a:

```text
https://auto-center-marica-gateway.onrender.com
```

Esse link deve ser colocado no README no campo "Link de acesso publicado".

## Passo a passo no Render

1. Criar uma conta em <https://render.com>.
2. Enviar este projeto para um repositorio GitHub.
3. No Render, escolher **New > Blueprint**.
4. Conectar o repositorio.
5. Selecionar o arquivo `render.yaml`.
6. Confirmar a criacao dos quatro servicos.
7. Aguardar o build das imagens Docker.
8. Abrir a URL publica do `auto-center-marica-gateway`.

## Variaveis de ambiente

O Gateway precisa conhecer as URLs dos microsservicos:

```text
CUSTOMER_SERVICE_URL
WORK_ORDER_SERVICE_URL
NOTIFICATION_SERVICE_URL
```

No Docker Compose, essas variaveis ja apontam para os nomes internos dos containers.

## Deploy alternativo no Railway

1. Criar conta em <https://railway.app>.
2. Criar um projeto novo.
3. Adicionar um servico para cada pasta em `services/`.
4. Configurar Dockerfile de cada microsservico.
5. Definir as variaveis de ambiente do Gateway.
6. Publicar o dominio do Gateway.

## Limitacoes conhecidas

Este projeto usa repositorios em memoria para facilitar a avaliacao. Em producao real, os dados seriam perdidos ao reiniciar os containers.

Evolucoes recomendadas:

- PostgreSQL por servico;
- mensageria com RabbitMQ ou Kafka;
- autenticacao JWT;
- observabilidade com Prometheus e Grafana;
- pipeline CI/CD com GitHub Actions.

