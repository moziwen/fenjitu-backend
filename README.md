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

## 项目规范与 Pi Skill

长期工程约定见 [AGENTS.md](AGENTS.md)，四份详细规范位于 `docs/工程规范/`。对应的四个 Pi Skill 位于 `.pi/skills/`：后端变更交付、跨端数据诊断、媒体与历史数据修复、安全发布。它们按任务类型选择，不要求每次全部加载；开发子代理已固定加载后端变更交付 Skill。

在 PI WEB 中选择本项目工作区后，新建会话以加载新增的项目资源。给 dev-loops 一个 GitHub Issue 编号或链接，并在 Issue 中写清范围、非目标和可测试的验收条件；明确采用本地计划时则以该计划为准。Skill 规定如何实施与验证，不替代需求来源。验收结果应逐条标明通过、失败或未验证，并附可复查的测试证据。

普通任务不会自动发布生产或修复数据。只有明确授权相应操作后，才使用发布或数据修复 Skill 的写入步骤。
