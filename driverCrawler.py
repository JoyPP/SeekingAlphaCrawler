from selenium import webdriver
import time

def webdriver_links(symbol):
    url = 'https://seekingalpha.com/symbol/' + symbol + '/focus'
    hdr = {'User-Agent': 'Mozilla/5.0'}

    profile = webdriver.FirefoxProfile()
    profile.set_preference('app.update.auto', False)
    profile.set_preference('app.update.enabled', False)

    driver = webdriver.Firefox('/usr/local/bin', firefox_profile=profile)
    driver.get(url)


    js = "var q=document.documentElement.scrollTop=100000"
    for i in range(100):
        driver.execute_script(js)
        time.sleep(3)

    element = driver.find_elements_by_class_name("content_block_investment_views")[0]
    lis = element.find_elements_by_tag_name("li")

