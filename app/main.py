from fastapi import FastAPI

app = FastAPI(
    title="Cloud Cost Optimizer",
    version="0.1"
)


@app.get("/")
def root():
    return {
        "message": "Cloud Cost Optimizer API is running"
    }