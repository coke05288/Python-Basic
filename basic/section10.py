# Section10
# 파이썬 예외 처리의 이해

# 예외의 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test)

# if True
#     pass

# x=>y

# NameError : 참조변수 없음

a = 10
b = 20
# print(c)

# ZeroDivisionError : 0 나누기 에러

# print(10/0)

# indexError : 인덱스 범위 오류

x = [10, 20, 30]

print(x[0])
# print(x[4])

# KeyError

dic = {'name': 'Kim', 'city': 'Incheon'}
# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 에러
import time
print(time.time())
# print(time.month())

# ValueError : 참조값이 없을때

x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError <= 시벌것 ******

# f = open('test.txt', 'r')

# TypeError

x = [1, 2]
y = (3, 4)
z = 'test'
# print(x+y)
print(x + list(y))


# 런타임 에러 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except1 : 에러명 1
# except2 : 에러명 2
# else : 에러가 발생하지 않았을 때 실행
# finally : 항상 실행되는 구문

# 예제 1 / ValueError에 대한 예외처리

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except ValueError:
    print('Not found it - Occured ValueError!')
else:
    print('okay! else')


# 예제 2 / 모든 에러에 대한 예외처리

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except:
    print('Not found it - Occured Error!')
else:
    print('okay! else')
finally:
    print('finally okay!')


# 예제 3 / 예외 처리는 하지 않지만, 무조건 수행되는 코딩

try :
    print('Try!')
finally:
    print('Okey!')


# 예제 4 

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except ValueError as l:
    print(l)
except IndexError:
    print('Not found it - Occured IndexError!')
except Exception:
    print('Not found it - Occured Error!')
else:
    print('okay! else')
finally:
    print('finally okay!')

# 예제 5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

print("-----------------")

try:
    a = 'Kim'
    if a=='Cho':
        print("okay")
    else:
        raise ValueError
except ValueError:
    print("문제발생")
except Exception as f:
    print(f)
else:
    print("ok")