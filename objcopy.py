from copy import copy, deepcopy

a = 1
b = a

print(a is b)

# 단계적으로 주소 복사하는 방식
a = [1, 2, 3]
b = [4, 5, a]

print(a is b)

x = [a, b, 100]
y = x

print(x)
print(y)

# 얕은 복사
a = 1
b = a

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy(x)

print(x)
print(y)

print(x is y)
print(x[0] is y[0])

# 깊은 복사
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = deepcopy(x)

print(x)
print(y)

# 깊은 복사가 복합 객체만을 생성하므로
# 복합 객체가 하나만 있는 경우에는 얕은 복사와 결과 동일
# 트리를 통째로 복사하고자 할 때는 deepcopy 활용
a = ["hello", "world"]
b = copy(a)
print(a is b)
print(a[0] is b[0])

c = deepcopy(a)
print(a is c)
print(a[0] is c[0])
