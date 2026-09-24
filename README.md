# fenjitu-backend

这是一个用于验证 PI WEB 与 dev-loops 本地工作流的最小 FastAPI 后端样板。当前只提供健康检查接口，不包含数据库或业务功能。

## 本地安装

在项目目录打开 PowerShell，运行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

先确认 `python --version` 显示 Python 3.11 或更高版本。依赖只安装到项目目录下的 `.venv`，不会修改全局 Python 环境。

## 启动与访问

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

- 健康检查：<http://127.0.0.1:8000/health>
- Swagger 页面：<http://127.0.0.1:8000/docs>
- OpenAPI 文档：<http://127.0.0.1:8000/openapi.json>

服务仅监听本机 `127.0.0.1`。关闭启动服务的终端即可停止服务。

## 运行测试

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

这是连通性样板，并非最终后端技术选型；开始业务开发前应先确定框架、数据库、认证方式和部署方案。
