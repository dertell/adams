from fastapi import FastAPI
from fastapi.responses import StreamingResponse, RedirectResponse
from packages.one import streaming
from pydantic import BaseModel
import time

class Request(BaseModel):
    query: str
    student: str
    topic: str

class Response(BaseModel):
    answer: str
    messageID: int


app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@app.post("/stream")
def stream(question: Request):
    return StreamingResponse(streaming(question.query))


@app.post("/quiz")
def quiz(topic: Request) -> Response:
    return

def fake_video_streamer():
    for i in range(10):
        time.sleep(.5)
        yield b"test"


@app.get("/test")
def main():
    return StreamingResponse(fake_video_streamer())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
