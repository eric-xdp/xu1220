from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, json,traceback,os,sys
import timer
from jdlogger import logger


# with open(os.getcwd()+'\settings.txt', 'r', encoding='utf-8-sig') as f:
#     settings = json.load(f)
#     print(settings)
chrome_options = webdriver.ChromeOptions()
# prefs = {"download.default_directory": settings['download_folder']}
# chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('chromedriver.exe')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()
t = timer.Timer()

def get_url():
    browser.get('https://bonfida.com/dex')
    time.sleep(10)
    # 等待到时间
    # t.start()
    # 获取价格控件元素
    browser.switch_to.default_content()

    price = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/div[1]/div/div[1]')
    print(price.text)
    # price.send_keys(0.5)
    # while True:
    #     try:
    #         # 输入价格
    #         pass
    #         break
    #     except Exception as e:
    #         logger.error('预约失败正在重试...')

get_url()