from google_play_scraper import Sort, reviews

def get_reviews(app_id, lang="ko", country="kr", count=5, score=None):
    # 첫 호출
    result, continuation_token = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=count,
        filter_score_with=score
    )

    print("=== 첫 번째 가져온 리뷰 ===")
    for r in result:
        print(f"[{r['score']}⭐] {r['userName']} : {r['content'][:50]}...")

    # continuation_token 있으면 추가 리뷰도 가져오기
    if continuation_token:
        result2, _ = reviews(app_id, continuation_token=continuation_token)
        print("\n=== 이어서 가져온 리뷰 ===")
        for r in result2:
            print(f"[{r['score']}⭐] {r['userName']} : {r['content'][:50]}...")

def main():
    app_id = "io.phloxcorp.pickin"  # 앱 패키지명
    get_reviews(app_id, count=78, score=5)

if __name__ == "__main__":
    main()
