#변수 
a = 1
b = 2
c = a + b
print(c)

#삼항연산자
d = 'true' if c > 3 else 'false'
print(d)

#문자열과 숫자 연결
# print("anser = " + 100) int 타입을 더할 시 에러
print("anser = " + str(100))

#문자 부분 추출
text = "문자열 자르기"
print(text[0:3])

#내포 표기법
list = [x * 2 for x in range(10)]
print(list)

#람다
lambdaTest = (lambda x: x * 3)
print(lambdaTest(4))

#클래스
class TestClass:
  def __init__(self, title):
    self.title = title

  def output(self):
    print(self.title)    

instance = TestClass('테스트')
instance.output()