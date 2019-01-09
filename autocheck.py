from selenium import webdriver

# 헤드리스모드로 실행
# https://edu.ssafy.comrk 반응형, 윈도우 창 크기 설정 필요
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('C:\\Users\\student\\Downloads\\chrome\\chromedriver_win32\\chromedriver', chrome_options=options)

driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')
driver.implicitly_wait(3)