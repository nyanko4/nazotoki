from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
@app.get("/")
async def root():
    return FileResponse("static/index.html")

class LoginRequest(BaseModel):
    password: int
  
@app.post("/api/answer")
async def login(req: LoginRequest):
    if req.password == 417:
        return {"message": "クリア！写真撮って送りましょう(無理そうならなんか恥ずかしいセリフを言おう(？)"}
    else:
        return {"message": "パスワードが違います、当てずっぽうの場合はやめましょう"}
