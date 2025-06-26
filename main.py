from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

class LoginRequest(BaseModel):
    password: str
  
@app.post("/api/answer")
async def login(req: LoginRequest):
    if req.password == "417":
        return {"message": "クリア！写真撮って送りましょう(無理そうならなんか恥ずかしいセリフを言おう(？)"}
    else:
        return {"message": "パスワードが違います、当てずっぽうの場合はやめましょう"}
