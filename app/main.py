"""最小 FastAPI 应用。"""

from fastapi import FastAPI

app = FastAPI(title="fenjitu-backend", description="最小健康检查服务", version="0.1.0")


@app.get("/health", tags=["健康检查"])
def health() -> dict[str, str]:
    """返回服务的明确健康状态。"""
    return {"status": "healthy", "service": "fenjitu-backend"}
