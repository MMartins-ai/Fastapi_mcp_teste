import uvicorn
from app import app


def start():
    uvicorn.run(app)

if __name__=='__main__':
    start()
