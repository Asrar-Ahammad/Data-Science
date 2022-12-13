from fastapi import FastAPI

app = FastAPI() # creating a instinct of the library imported

@app.get('/hello')
async def hello():
    return 'welcome'