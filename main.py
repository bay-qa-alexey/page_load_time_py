# pip3 install selenium
# pip3 install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

''' setting up chromedriver & Chrome '''
service = Service()
service.executable_path = '/usr/local/bin/chromedriver'
# service.executable_path = ChromeDriverManager().install()

options = Options()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
''' end setting up '''

driver = webdriver.Chrome(service=service, options=options)
driver.get('http://www.yahoo.com')

requestStart = driver.execute_script("return window.performance.timing.requestStart")
responseEnd = driver.execute_script("return window.performance.timing.responseEnd")
fetchStart = driver.execute_script("return window.performance.timing.fetchStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

print(f'{(responseEnd - requestStart) / 1000} : API perfomance')
print(f'{(domComplete - fetchStart) / 1000} : Total perfomance')

driver.quit()
