#virtual env starter
#.\venv\Scripts\python.exe -m uvicorn clan_api.main:app



from fastapi import FastAPI

app = FastAPI(title="Vertigo Games Clan API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
