import requests, pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

if __name__ == "__main__":
    # # 피클 파일을 읽어와서 CSV로 저장
    # df.to_csv("hollys_store.csv", index=False)
    # print("Data saved as CSV.")



    exit()
    all_data, num, skip_count = [], 1, 0
    with tqdm(total=100) as pbar:
        while num <= 100 and skip_count < 10:
            url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={num}"
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            table = soup.find('table')
            if not table or len(table.find_all('th')) != len([td.text.strip() for td in table.find_all('tr')[1].find_all('td')]):
                skip_count += 1; num += 1; continue
            all_data.append(pd.DataFrame([[td.text.strip() for td in tr.find_all('td')] for tr in table.find_all('tr')[1:]], columns=[th.text.strip() for th in table.find_all('th')]))
            num += 1
            pbar.update(1)
    pd.concat(all_data).to_pickle("hollys_store.pkl")
    print("Data saved.")
