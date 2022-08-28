# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1: 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)

# 조건 2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):

    height = height / 100

    if gender == "남자":
        weight = height * height * 22
    elif gender == "여자":
        weight = height * height * 21


    print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height*100, gender, round(weight, 2)))

std_weight(175, "남자")