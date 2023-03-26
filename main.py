from fastapi import FastAPI
from utils import get_webdriver
from typing import Union

app = FastAPI()




@app.get('/')
async def main_page() ->dict[str,str]:
    driver = get_webdriver(
    [
        "--headless",
        "--no-sandbox",
        '--disable-dev-shm-usage'
    ]
)
    driver.get('https://google.com')
    driver.close()
    return {
        "message":"Hello from fastapi"
    }

