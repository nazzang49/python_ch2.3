import sys

i1 = 10
i2 = 10
print(hex(id(i1)),hex(id(i2)))

i1 = 11
i2 = 10 + 1
print(hex(id(i1)),hex(id(i2)))

# list는 mutable이므로 서로 다른 객체가 된다
l1 = [1,2]
l2 = [1,2]
print(hex(id(l1)),hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)),hex(id(s2)))

# is 동일성 레퍼런스 비교
print(i1 is i2)
print(l1 is l2)
print(s1 is s2)

# 리터럴 상수 지정 방식
t1 = (1,2,3)
t2 = (1,2,3)
print(sys.getrefcount(t1), sys.getrefcount(t2))
print(t1 is t2)

# 생성자 방식
t3 = tuple(range(1,4))
print(sys.getrefcount(t3))
print(t1 is t3)

# slicing 방식
t4 = (0,1,2,3)[1:]
print(t3 is t4)

# 직접 리터럴 상수를 지정하는 방식 / 생성자를 활용하는 방식 / slicing 방식의 동일성 결과는 서로 다름












