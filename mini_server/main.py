from fastapi import FastAPI, Request
import uvicorn

fast_app = FastAPI()

@fast_app.get("/")
async def maxi_server(request : Request):
    return {"status": "norm, niche tak"}

if __name__ == "__main__":
    uvicorn.run(fast_app, host="0.0.0.0", port=5000)