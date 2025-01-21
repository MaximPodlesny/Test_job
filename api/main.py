from fastapi import FastApi

app = Fastapi()

@app.get('/')
async def root():
    return 'Hello World'