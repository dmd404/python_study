class ClassWithRegularAttributes:
    def __init__(self, someParameter):
        self.someAttribute = someParameter
        
obj = ClassWithRegularAttributes('some initial value')
print(obj.someAttribute)  # 'some initial value'를 출력
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # 'changed value'를 출력
del obj.someAttribute  # someAttribute 속성을 삭제
