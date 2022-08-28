# if 조건:
#     실행 명령문
# elif 조건:
#     실행 명령문
# else:
#     실행 명령문

# weather = input("오늘 날씨는 어때요? ")

# if weather == "rain" or weather == "snow":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")


temp = int(input("기온은 어때요? "))

if 30 <= temp:
    print(" Too Hot")
elif 10 <= temp and temp < 30 :
    print("Good")
elif 0 <= temp and temp < 10:
    print("Cold")
else:
    print("Too Cold")