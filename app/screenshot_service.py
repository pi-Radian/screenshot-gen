from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#from selenium_stealth import stealth
import platform
import random
import string
import os
from storage_service import save_img_to_bucket

def get_screenshot_from_url(url: str):
    start_time = time.time()

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver_name = 'chromedriver_mac64' if platform.system() == 'Darwin' else 'chromedriver_linux64'
    driver_executable = f"/drivers/{driver_name}/chromedriver"
    driver_executable = os.getcwd() + driver_executable
    driver_executable = driver_executable if platform.system() == 'Darwin' else '/usr/bin/chromedriver'
    print(driver_executable)
    driver = webdriver.Chrome(
        options=options, executable_path=driver_executable)

    # stealth(driver,
    #         languages=["en-US", "en"],
    #         vendor="Google Inc.",
    #         platform="Win32",
    #         webgl_vendor="Intel Inc.",
    #         renderer="Intel Iris OpenGL Engine",
    #         fix_hairline=True,
    #         )

    #url = "https://youtube.com"  # change the url
    driver.get(url)
    random_path = "./tmp/" + ''.join(random.choices(string.ascii_letters, k=7)) + ".png"
    driver.save_screenshot(random_path)
    print(random_path)
    
    img_uri = save_img_to_bucket(random_path)
    os.remove(random_path) 
    
    elapsed = "%s seconds" % (time.time() - start_time)
    print("Done in " + elapsed)
    return img_uri
