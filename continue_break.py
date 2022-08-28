absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴

for student in range(1, 11): # 1 ~ 10
    if student in absent:
        continue # 다음 반복으로 넘어감
    elif student in no_book:
        print("오늘 수업 여기까지. {}는 교무실로 따라와".format(student))
        break # 반복문 탈출
    print("{}, 책을 읽어봐".format(student))
