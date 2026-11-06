import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# 1. Добавляем импорт логгера
from source.logger import setup_logger
from source.routers import snippets
from source.db import init_db

# 2. Вызываем настройку логгера ДО создания приложения
setup_logger()

app = FastAPI(title="Snippet Storage API")

# Инициализация БД при старте
@app.on_event("startup")
def startup():
    init_db()

# Подключаем роутеры
app.include_router(snippets.router)

# Простой HTML на главную
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body style="font-family: monospace; padding: 20px;">
            <h1>Snippet Storage</h1>
            <p>Документация API доступна по адресу <a href="/docs">/docs</a> (Swagger UI)</p>
            <p>Метрики доступны по адресу <a href="/metrics">/metrics</a></p>
        </body>
    </html>
    """

@app.get("/health")
def health():
    # Эта переменная будет передаваться при сборке Docker-образа
    version = os.getenv("APP_VERSION", "dev")
    return {"status": "ok", "version": version}
