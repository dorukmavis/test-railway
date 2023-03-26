from fastapi import FastAPI
from utils import get_webdriver,checking_for_high_res,checking_for_hindi,checking_for_js_hovers
from typing import Union

app = FastAPI()

LINKS = [
    "https://graceful-sunburst-78f35d.netlify.app/www.classcentral.com/index.html",
    "https://ammardab3an99.github.io/",
    "https://heartfelt-lollipop-736861.netlify.app/",
    "https://radiant-hummingbird-697a83.netlify.app/",
    "http://trialserver.rf.gd/trial6/www.classcentral.com/index.html",
    "https://class-central.vercel.app/www.classcentral.com/index.html",
    "https://5dcookie.github.io/",
    "https://www.census2011.co.in/city.php#:~:text=Here%20are%20the%20details%20of,%2D%203%2C124%2C458%2C%20Jaipur%20%2D%203%2C046%2C163",
    "https://umair1814.github.io/",
    "https://na.co",
    "https://www.httrack.com/",
    "https://www.classcentral.com/",
    "https://sinistersup.github.io/classcentral-hindi/",
    "https://omarkhalifa97.github.io/khalifaaaz.github.io/",
    "https://df0a.github.io/",
    "http://miguel-hindi-classcentral.s3-website-us-east-1.amazonaws.com/",
    "https://classcentral-scrape-hindi.vercel.app/",
    "https://testclass01.000webhostapp.com/www.classcentral.com/index.html"
    "https://mike-brown5.github.io/AllStars-Scrapped-Site/",
    "https://ubadeakkad.github.io/",
    "https://www.dqlab.id/",
    "https://drive.google.com/drive/folders/1eLU2AQ80bn89gYNC2HEIbrKswVzdj0qC?usp=sharing",
    "https://www.mediafire.com/folder/ktcts50c9o1up/Class_Central_-Website_translation",
    "https://www.facebook.com/",
    "http://daniel1uno.byethost31.com/",
    "http://mihir.testing-phase.com/",
    "http://grsmuche.vh109.hosterby.com/",
    "https://a58-mohiuddin.github.io/developer_trial_task/web_translate.html"
    "https://datta07.github.io/classcentralclone/",
    "https://venerable-froyo-7f3b1e.netlify.app/university/cornell.html"
    "https://muhammederenaslan.github.io/codingallstars/",
    "https://exosmotic-bay.000webhostapp.com/",
    "https://interviewdeneme123.000webhostapp.com/",
    "http://classcent.infinityfreeapp.com/",
    "https://codingallstarttest0000.on.drv.tw/www.teeest.blog/"
]




@app.get('/')
async def main_page() ->dict[str,str]:
    driver = get_webdriver(
    [
        "--headless",
        "--no-sandbox",
        '--disable-dev-shm-usage'
    ]
)
    driver.get('"https://google.com')
    driver.close()
    return {
        "message":"Hello from fastapi"
    }



@app.get('/test_links')
async def testing_links() ->dict[str,dict]:
    results = []
    for link in LINKS:
        hover_test = checking_for_js_hovers(link)
        high_res_test = checking_for_high_res(link)
        non_hindi_list = checking_for_hindi(link)
        results.append({
            'url':link,
            'hover_test':hover_test,
            'high_res_test':high_res_test,
            'non_hindi_statements':non_hindi_list
        })
    
    return {
        'results':results
    }



