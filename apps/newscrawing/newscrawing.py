import pickle
import random
import time
from tqdm import tqdm  # ✅ tqdm 추가
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.chrome_driver import chromeDriver

news_data = []


def extract_data(driver, page, progress_bar):
    """현재 페이지에서 뉴스 데이터 추출 후 다음 페이지 이동"""
    print(f"\n==== 페이지 {page} 데이터 수집 ====")
    li_xpath = '//*[@id="container"]/div[2]/div[2]/div[1]/section/div/ul/li'
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, li_xpath)))
    li_elements = driver.find_elements(By.XPATH, li_xpath)
    print(f"LI 개수: {len(li_elements)}")

    for li in li_elements:
        try:
            datacid = li.get_attribute("data-cid")
            if not datacid:
                continue

            a_tag = li.find_element(By.TAG_NAME, "a")
            a_href = a_tag.get_attribute("href")
            driver.execute_script("arguments[0].click();", a_tag)
            time.sleep(random.uniform(2, 4))

            extract_detail_page(driver, a_href, progress_bar)
            driver.back()
            time.sleep(random.uniform(2, 4))

        except Exception as e:
            print(f"상세 페이지 수집 중 에러 발생: {e}")

    return move_to_next_page(driver, page)


def extract_detail_page(driver, url, progress_bar):
    """상세 페이지에서 뉴스 제목, 본문, 작성 시간 추출"""
    progress_bar.update(1)
    progress_bar.set_description(f"상세 페이지 수집 중 ({progress_bar.n}번째)")

    title = driver.find_element(By.XPATH, '//*[@id="container"]//h1').text.strip()
    body = "\n".join(
        [p.text.strip() for p in driver.find_elements(By.XPATH, '//*[@id="container"]//p') if p.text.strip()])
    published_at = driver.find_elements(By.XPATH, '//*[@id="container"]//span[contains(@class, "date")]')
    published_at = published_at[0].text.strip() if published_at else "작성 시간 없음"

    news_data.append({"title": title, "body": body, "url": url, "published_at": published_at})


def move_to_next_page(driver, page):
    """다음 페이지로 이동"""
    print(f"\n==== 페이지 {page} → 다음 페이지 이동 ====")

    try:
        current_page = int(
            driver.find_element(By.XPATH, '//*[@id="container"]//strong[contains(@class, "num on")]').text.strip())
        next_page_xpath = f'//*[@id="container"]//a[@class="num" and text()="{current_page + 1}"]'
        next_page = driver.find_elements(By.XPATH, next_page_xpath)

        if not next_page:
            print("마지막 페이지 도달.")
            return False

        ActionChains(driver).move_to_element(next_page[0]).perform()
        driver.execute_script("arguments[0].click();", next_page[0])
        time.sleep(random.uniform(2, 4))
        return True

    except Exception as e:
        print(f"페이지 이동 실패: {e}")
        return False


def save_data():
    """데이터를 pickle 파일로 저장"""
    with open("news_data.pkl", "wb") as f:
        pickle.dump(news_data, f)
    print(f"\n✅ {len(news_data)}개 뉴스 저장 완료!")


if __name__ == "__main__":
    driver = chromeDriver()
    driver.get("https://www.yna.co.kr/industry/all/1")

    page = 1
    total_news_estimate = 1000  # 뉴스 예상 개수 임의 설정, 반복횟수에 영향 X
    with tqdm(total=total_news_estimate, desc="상세 페이지 수집 중") as progress_bar:
        while extract_data(driver, page, progress_bar):
            page += 1

    save_data()
