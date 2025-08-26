import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from util import generate_user_agent, parse


def chromeDriver():
    # ChromeDriver 자동 설치 및 최신 버전 유지
    chrome_driver_path = chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()

    # User-Agent 설정
    userAgent = generate_user_agent()
    user_agent = parse(userAgent)

    # Chrome 옵션 추가
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    options.page_load_strategy = 'normal'
    options.add_argument('--enable-automation')
    options.add_argument('disable-infobars')
    options.add_argument('disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--lang=ko_KR')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--mute-audio')

    # ChromeDriver 실행
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    driver.implicitly_wait(3)
    return driver


if __name__ == "__main__":
    driver = chromeDriver()
