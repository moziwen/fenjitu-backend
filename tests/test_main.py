"""应用测试。"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_healthy_status() -> None:
    """健康检查应返回 HTTP 200 和明确状态。"""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "fenjitu-backend"}


def test_openapi_and_docs_are_available() -> None:
    """FastAPI 原生 OpenAPI 和 Swagger UI 应可访问。"""
    openapi_response = client.get("/openapi.json")
    docs_response = client.get("/docs")

    assert openapi_response.status_code == 200
    assert openapi_response.json()["info"]["title"] == "fenjitu-backend"
    assert "/health" in openapi_response.json()["paths"]
    assert docs_response.status_code == 200
    assert "Swagger UI" in docs_response.text
