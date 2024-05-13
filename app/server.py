from fastapi import FastAPI
from fastapi.responses import StreamingResponse, RedirectResponse
from packages.one import streaming
from pydantic import BaseModel
import time

class Request(BaseModel):
    query: str
    student: str
    topic: str

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@app.post("/stream")
def stream(question: Request):
    return StreamingResponse(streaming(question.query))

@app.get("/getstream")
def stream(question: str):
    headers = {"X-Content-Type-Options": "nosniff"}
    return StreamingResponse(streaming(question), headers=headers)


@app.post("/quiz")
def quiz(topic: Request):
    return

def fake_video_streamer():
    for i in range(10):
        time.sleep(.5)
        yield b"test"


@app.get("/test")
def main() -> StreamingResponse:
    headers = {"X-Content-Type-Options": "nosniff"}
    return StreamingResponse(fake_video_streamer(), headers=headers)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
