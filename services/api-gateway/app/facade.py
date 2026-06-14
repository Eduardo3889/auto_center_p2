import os

import httpx


class WorkshopGatewayFacade:
    def __init__(self) -> None:
        self._customer_service_url = os.getenv(
            "CUSTOMER_SERVICE_URL",
            "http://localhost:8001",
        )
        self._work_order_service_url = os.getenv(
            "WORK_ORDER_SERVICE_URL",
            "http://localhost:8002",
        )
        self._notification_service_url = os.getenv(
            "NOTIFICATION_SERVICE_URL",
            "http://localhost:8003",
        )

    async def health(self) -> dict:
        async with httpx.AsyncClient(timeout=5.0) as client:
            responses = await self._get_health_responses(client)

        return {
            "status": "ok",
            "workshop": "Auto Center Marica",
            "services": responses,
        }

    async def _get_health_responses(self, client: httpx.AsyncClient) -> dict:
        service_urls = {
            "customers": self._customer_service_url,
            "work_orders": self._work_order_service_url,
            "notifications": self._notification_service_url,
        }
        result = {}

        for service_name, service_url in service_urls.items():
            try:
                response = await client.get(f"{service_url}/health")
                result[service_name] = response.json()
            except httpx.HTTPError:
                result[service_name] = {"status": "unavailable"}

        return result

