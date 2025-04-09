from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import requests
from apscheduler.schedulers.background import BackgroundScheduler

TOKEN = '7906795471:AAHfbhlk7tLpWJ6-dalU74mbCl6D-E8MxN4'
CHAT_ID = 7540647235
url = 'http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20240103'

# 크롬 드라이버 자동 설치
chromedriver_autoinstaller.install()

def send_test_message(content):
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={
        'chat_id': CHAT_ID,
        'text': content
    })

def job_function():
    driver = webdriver.Chrome()
    try:
        driver.get(url)

        iframe_xpath = '//iframe[@id="ifrm_movie_time_table"]'
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, iframe_xpath))
        )
        driver.switch_to.frame(iframe)

        iframe_content_xpath = '//div[@class="showtimes-wrap"]'
        iframe_content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, iframe_content_xpath))
        ).get_attribute("outerHTML")

        soup = BeautifulSoup(iframe_content, 'html.parser')
        imax = soup.select_one('span.imax')

        if imax:
            imax = imax.find_parent('div', class_='col-times')
            title = imax.select_one('div.info-movie > a > strong').text.strip()
            send_test_message(title + ' imax 예매 열림')
            sched.pause()
        else:
            send_test_message('imax 예매 안 열림')

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

# BackgroundScheduler 생성
sched = BackgroundScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()

try:
    while True:
        pass  # 메인 스레드가 종료되지 않도록 무한 루프
except (KeyboardInterrupt, SystemExit):
    sched.shutdown()
    print("Scheduler has been shut down.")
