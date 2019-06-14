import sys

x = object()
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))

# 레퍼런스 값이 줄어든다
del x
print(sys.getrefcount(y))

# 레퍼런스 카운트 = 더 이상 사용하지 않는 객체 = 가비지 컬렉션 실행

