from fastapi import FastAPI
from utils import get_webdriver
from typing import Union

app = FastAPI()
driver = get_webdriver(
    [
        "--headless"
    ]
)



@app.get('/')
async def main_page() ->dict[str,str]:
    return {
        "message":"Hello from fastapi"
    }

