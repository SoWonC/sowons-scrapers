import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # 크롤링할 URL
    url = 'https://example.com'  # 여기에 원하는 URL을 넣으세요.

    # 웹 페이지 요청
    response = requests.get(url)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        print("페이지 로딩 성공!")

        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # id가 'cppLargeCategoryBest'인 요소 찾기
        # class가 'container'인 div 요소 찾기
        container = soup.find('div', class_='container')

        if container:
            # container 안에서 class가 'best-classifieds'인 div 요소 찾기
            best_classifieds = container.find('div', class_='best-classifieds')

        if container:
            # 해당 요소 안의 텍스트 내용 추출
            print(container.text.strip())  # 텍스트 내용 출력
        else:
            print("해당 id를 가진 요소를 찾을 수 없습니다.")
    else:
        print(f"페이지 로딩 실패! 상태 코드: {response.status_code}")
