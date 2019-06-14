# 심볼 테이블 확인
g_a = 1
g_b = 'symbol'

def f():
    l_a = 2
    l_b = 'table'
    print(locals())

for i in range(10):
    g_c = 3
    g_d = 'python'
    print(locals())

f()
print(globals())

print(f.__dict__)

class MyClass:
    x = 10
    y = 20

print(MyClass.__dict__)
