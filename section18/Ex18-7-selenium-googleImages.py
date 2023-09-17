'''
Ex18-7-selenium-googleImages.py

seleninum 패키지
    어플리케이션 테스트하기위한 프레임웍 입니다.
    웹어플리케이션 다양한 브라우저 동작 테스트용
    웹 크롤링으로 많이 사용된다.
    java, python, c#, ruby 등 다양한 언어 지원

https://chromedriver.chromium.org/downloads

크롬 우측상단 ... -> 도움말 -> 크롬정보 -> 버전확인
                -> 해당 버전 chromedriver 다운로드 
                -> chrome 실행파일 있는 폴더에 복사 붙여넣기
'''

import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service

import traceback

def download_images(keyword, num_images=10, output_dir='images'):
    # Chrome 드라이버 경로
    chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    
    service = Service(executable_path=chrome_driver_path)
    
    # Chrome 드라이버 인스턴스 생성
    driver = webdriver.Chrome(service=service)
    
    # Google 이미지 검색 페이지 접속
    driver.get('https://www.google.co.kr/imghp')
    
    # 검색어 입력
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys(keyword)    # 키워드 입력
    search_bar.send_keys(Keys.RETURN)

    # 페이지 로딩 대기
    time.sleep(2)
    
    # 출력 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 썸네일 요소 선택
    thumbnails = driver.find_element(By.CSS_SELECTOR, '.rg_i')
    
    # 썸내일 클릭 및 이미지 다운로드
    for index, thumbnail in enumerate(thumbnails[:num_images]):
        try:
            thumbnail.click()
            time.sleep(2)
            
            # 이미지 요소 대기 및 선택
            image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.r48jcc.pT0Scc.iPVvYb')
                )
            )

            # 이미지 URL 가져오기
            image_url = image.get_attribute('src')

            if image_url.startwith('data:'):
                continue

            headers = {'User-Agent': 'Mozilla/5.0'}
            request = urllib.request.Request(image_url, headers=headers)
            with urllib.request.urlopen(request) as response:
                with open(f'{output_dir}/{keyword}_{index}.jpg', 'wb') as out_file:
                    out_file.write(response.read())

        except Exception as e:
            print(f'Error downloading image {index}: {e}')
            traceback.print_exc()


    # 드라이버 종료
    driver.quit()

# 실행코드
keyword = '투바투'
num_images = 10
output_dir = 'images'

# 이미지 다운로드 함수 호출
download_images(keyword, num_images, output_dir)



    
    

