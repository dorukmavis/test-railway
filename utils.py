from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from typing import Union
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import codecs,string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import PIL.Image as Img
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re


PATH = os.getcwd()







def check_hindi(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return True
    else:
      return False



def get_webdriver(
    options:Union[list,tuple,None] = None
) -> webdriver.Chrome:
 
    if options:
        chrome_opt = webdriver.ChromeOptions()
        for option in options:
            chrome_opt.add_argument(option)
        chrome_opt.add_experimental_option('excludeSwitches', ['enable-logging'])

        chrome_driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=chrome_opt
        )

    else:
        chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    
    return chrome_driver




def checking_for_hindi(link:str)->list:
    driver=get_webdriver(options=["--headless","--no-sandbox",
        '--disable-dev-shm-usage'])
    try:
        driver.get(link)
        all_texts =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body"))).text
        all_texts = re.sub(r'[~^0-9]', '', all_texts)
        print(all_texts)
        # all_texts = driver.find_element(By.XPATH, "/html/body").text
        not_hindi_words = [text for text in all_texts.split('\n') if not check_hindi(text)]
        
        driver.implicitly_wait(1)
        return not_hindi_words
    except:
        return None


    
        

def checking_for_high_res(link:str)->bool:
    driver=get_webdriver(options=["--headless","--no-sandbox",
        '--disable-dev-shm-usage'])
    driver.get(link)
    all_images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME,"img")))
    all_images = [image for image in all_images if not ((image.size["width"] ==0) or (image.size['height']==0))]
    presented_resolutions = [image.size for image in all_images]
    actual_resolutions = [{"height":image.get_attribute('naturalHeight'),"width":image.get_attribute('naturalWidth')} for image in all_images]
    checker = []
    for presented,actual in zip(presented_resolutions,actual_resolutions):
        w_d = float(int(actual['width']) - int(presented['width']) )
        h_d = float(int(actual['height']) - int(presented['height']))
        if w_d>0 and h_d>0:
            checker.append(True)
        elif (int(presented['width'])<int(actual['width']*6)) and (int(presented['height'])<int(actual['height'])*6):
            checker.append(True)
        else:
            checker.append(False)

    return all(checker)
    # list_of_image_urls = [image.get_attribute('src') for image in all_images]





def checking_for_js_hovers(link:str)->bool:
    driver=get_webdriver(options=["--headless","--no-sandbox",
    '--disable-dev-shm-usage'])
    driver.get(link)
    try:
        elements_to_hover= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.hidden.weight-semi.large-up-block")))
        hover = ActionChains(driver).move_to_element(elements_to_hover)
        hover.perform()
        # main-nav-dropdown js-main-nav-dropdown
        hovered_nav = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'nav.main-nav-dropdown.js-main-nav-dropdown.is-open')))
        if hovered_nav:
            # new_elements = driver.find_elements_by_css_selector('li.main-nav-dropdown__item')
            # for new_element in new_elements:
            #     hover.move_to_element(new_element).perform()
            driver.close()
            return True
        else:
            driver.close()
            return False
    except:
        driver.close()
        return False






if __name__ == "__main__":
    checking_for_js_hovers()
