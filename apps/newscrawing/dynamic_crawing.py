import requests
from bs4 import BeautifulSoup
from util import random, time, By, BeautifulSoup, pd
from util.chrome_driver import chromeDriver


if __name__ == "__main__":
    url = "https://www.hollys.co.kr/store/korea/korStore2.do"
    driver = chromeDriver()
    driver.get(url)
    time.sleep(random.uniform(2, 4))
    all_data=[]
    page = 1


    while True:

        try:
            if page % 10 == 1:
                if page == 1:
                    # driver.find_element(By.LINK_TEXT, str(page))
                    print(f"페이지 {page}로 이동 완료!")
                    time.sleep(random.uniform(1, 2))  # 랜덤 시간 지연
                    page += 1  # 페이지 증가

                elif  page ==11:
                    print(f"페이지 {page}로 이동 완료!")
                    driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[10]/img').click()
                    time.sleep(random.uniform(1, 2))  # 랜덤 시간 지연
                    page += 1  # 페이지 증가

                else :
                    print(f"페이지 {page}로 이동 완료!")
                    driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[11]/img').click()
                    time.sleep(random.uniform(1, 2))  # 랜덤 시간 지연
                    page += 1  # 페이지 증가
            else:
                print(f"페이지 {page}로 이동 완료!")
                driver.find_element(By.LINK_TEXT, str(page)).click()
                time.sleep(random.uniform(1, 2))  # 랜덤 시간 지연
                page += 1  # 페이지 증가
        except Exception as e:
            print(f"Error: {e}")
            break  # 오류 발생 시 루프 종료
