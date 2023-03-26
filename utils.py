from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from typing import Union


def get_webdriver(
    options:Union[list,tuple,None] = None
) -> webdriver.Chrome:
 
    if options:
        chrome_opt = webdriver.ChromeOptions()
        for option in options:
            chrome_opt.add_argument(option)

        chrome_driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=chrome_opt
        )

    else:
        chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    
    return chrome_driver

