from fastapi import FastAPI

app = FastAPI()


@app.get('/test')
async def hallo(value: float = None):
    return {'value': value}
