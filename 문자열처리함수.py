python = "Python is Amazing"

print(python.lower()) # 문자열 소문자로 변환

print(python.upper()) # 문자열 대문자로 변환

print(python[0].isupper()) # 대문자이면 True 출력

print(len(python)) # 문자열 길이 : 17

print(python.replace("Python", "Java")) # 문자열 교체

index = python.index("n") # "n"의 위치 저장: 5
print(index)

index = python.index("n", index+1) # 두 번째 "n"의 위치 저장: 15
print(index)

print(python.find("n")) # n의 위치 : 5

print(python.find("Java")) # "Java"의 위치 : -1
# print(python.index("Java")) # 오류출력 : substring not found

print(python.count("n")) # n의 갯수 : 2