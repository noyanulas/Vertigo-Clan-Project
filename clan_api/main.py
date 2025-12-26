#virtual env starter
#.\venv\Scripts\python.exe -m uvicorn clan_api.main:app

from fastapi import FastAPI
from clan_api.routers import clans

app = FastAPI(title="Vertigo Games Clan API")

app.include_router(clans.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
