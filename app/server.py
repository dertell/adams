from fastapi import FastAPI
from fastapi.responses import StreamingResponse, RedirectResponse
from app.packages.one import streaming
from pydantic import BaseModel


class Request(BaseModel):
    query: str

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@app.post("/stream")
def stream(question: Request):
    return StreamingResponse(streaming(question.query))
