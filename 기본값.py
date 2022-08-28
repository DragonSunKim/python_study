# def profile(name, age, main_lang):
#     print("이름: {}\t나이: {}\t주 사용 언어: {}".format(name, age, main_lang))

# print("유재석", 20, "파이썬")
# print("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age= 17, main_lang= "파이썬"):
    print("이름: {}\t나이: {}\t주 사용 언어: {}".format(name, age, main_lang))

profile("유재석")
profile("김태호")


# 키워드로 데이터 삽입

profile(name= "조세호", main_lang= "C")
profile(age=18, name= "지석진")