from selenium import webdriver
import getpass

# 헤드리스모드로 실행
# https://edu.ssafy.com이 반응형, 윈도우 창 크기 설정 필요
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('C:\\Users\\student\\Downloads\\chrome\\chromedriver_win32\\chromedriver', chrome_options=options)

driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')
driver.implicitly_wait(3)

# 사용자 로그인정보 받아와 로그인하기
userID = input('ID: ')
userPWD = getpass.getpass(prompt='PASSWORD: ')

driver.find_element_by_name('userId').send_keys(userID)
driver.find_element_by_name('userPwd').send_keys(userPWD)

driver.find_element_by_css_selector('a.btn-lg').click()

# 로그인 확인 필요

# 로그인 완료시, 버튼 사라짐을 이용한 로그인/로그아웃 분류
try :
    # 출석체크
    driver.find_element_by_id('checkIn').click()
    driver.get('https://edu.ssafy.com/edu/main/index.do')
    checkin_time = driver.find_element_by_css_selector('div.state > span > span').text
    print('입실시간 : '+checkin_time)
    driver.quit()
except :
    # 퇴실체크
    driver.find_element_by_id('checkOut').click()
    driver.get('https://edu.ssafy.com/edu/main/index.do')
    checkout_time = driver.find_element_by_css_selector('div.state2 > a > span').text
    print('퇴실시간 : '+checkout_time)
    driver.quit()

