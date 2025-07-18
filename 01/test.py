print("테스트입니다.")
print('"테스트입니다"')
print("파이썬", "웰컴", "python")
print("파이썬 \n", "웰컴\n")
print('파이썬 "매우" 웰컴')
print(""" 
[도움말]
-h : 파이썬 도움말
굉장히 긴 문자열입니다.........
파이썬 화이팅
파이썬자동화
      """)

name = input("이름을 입력하세요.")

phone = input(f"{name} 번호를 입력하세요.")
age = input("나이를 입력하세요.")
#print(name)
#print(phone)
#print(age)
print(name, "의 전화번호는", phone, "입니다.", "나이는", age)

print(name, "의 전화번호는", phone, "입니다.", "나이는", age)
print("내 이름은 {}이고 나이는 {}살입니다.".format(name,age))
print(f"내 이름은 {name}이고 나이는 {age}살입니다.")