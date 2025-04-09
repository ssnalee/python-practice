from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# 크롬 드라이버 자동 설치
chromedriver_autoinstaller.install()

# URL 설정
url = 'http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20240103'

# Selenium WebDriver 초기화
driver = webdriver.Chrome()

try:
    # 대상 웹 페이지로 이동
    driver.get(url)

    # iframe의 XPath를 찾아서 해당 iframe으로 전환
    iframe_xpath = '//iframe[@id="ifrm_movie_time_table"]'
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, iframe_xpath))
    )
    driver.switch_to.frame(iframe)

    # iframe 내용이 로드될 때까지 대기
    iframe_content_xpath = '//div[@class="showtimes-wrap"]'
    iframe_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, iframe_content_xpath))
    ).get_attribute("outerHTML")

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(iframe_content, 'html.parser')
    title_list = soup.select('div.info-movie')
    for i in title_list :
        print(i.select_one('a > strong').text.strip())
    

finally:
    # iframe에서 벗어나 원래의 상위 레벨로 돌아감
    driver.switch_to.default_content()
    # WebDriver 종료
    driver.quit()