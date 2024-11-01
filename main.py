from fastapi import FastAPI
from routes import export_router, cstm_router, hexa_router

app = FastAPI()


app.include_router(export_router)
app.include_router(cstm_router)
app.include_router(hexa_router)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

