






if __name__ =="__main__":
    numbers = range(100)
    volume = ['홀수' if num%2!=0 else '짝수' for num in numbers]
    # print(volume)

    subjects = ['국어','수학','영어']
    scores = [80, 1000, 5000000000]

    john = {key: 'A' if value > 100 else 'F' for key, value in zip(subjects, scores)}
    print(john)


