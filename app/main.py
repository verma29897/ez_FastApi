from fastapi import FastAPI
import ops,client


app = FastAPI()

app.include_router(ops.router, prefix="/ops", tags=["Ops User"])
app.include_router(client.router, prefix="/client", tags=["Client User"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app,host='192.168.1.9' ,port=8000)
