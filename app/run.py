import uvicorn

if __name__ == 'main':
    uvicorn.run('app.main:app', reload=True)