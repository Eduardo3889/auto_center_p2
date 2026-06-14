from fastapi import FastAPI

from app.facade import WorkshopGatewayFacade


app = FastAPI(
    title="Auto Center Marica - API Gateway",
    version="1.0.0",
)
gateway = WorkshopGatewayFacade()


@app.get("/")
def root() -> dict:
    return {
        "name": "Auto Center Marica OS",
        "description": "Gateway da plataforma de atendimento da oficina.",
        "docs": "/docs",
    }


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "api-gateway",
        "workshop": "Auto Center Marica",
    }


@app.get("/services/health")
async def services_health() -> dict:
    return await gateway.health()
