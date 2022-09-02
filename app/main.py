from typing import Union

from fastapi import FastAPI
import uvicorn
import asyncio
from screenshot_service import get_screenshot_from_url

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/hello/{name}")
def hello_world(name: str):
    return {"msg": f"hakuna matata {name}"}



@app.get("/ss")
async def get_screenshot(q: Union[str, None] = None):
    res = await asyncio.gather(get_screenshot_from_url(q))
    return {"uri": res}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
