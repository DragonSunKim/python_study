cabinet = {3: "유재석", 100:"김태호"}
print(cabinet[3]) # 유재석 출력
print(cabinet[100]) # 김태호 출력

print(cabinet.get(3))

print(cabinet[5]) # 오류 출력
print(cabinet.get(5)) # None 출력

print(cabinet.get(5, "사용가능")) # 값이 없으면 "사용가능" 출력

print(cabinet)
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}

print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 딕셔너리 데이터 추가

cabinet["A-3"] = "김종국" # 값 변경
cabinet["C-20"] = "조세호" # 값 추가
print(cabinet)

# 딕셔너리 데이터 삭제
del cabinet["A-3"]
print(cabinet)

# key 출력

print(cabinet.keys())

# value 출력

print(cabinet.values())

# key, value 출력

print(cabinet.items())

# 전체 데이터 삭제
cabinet.clear()
print(cabinet)