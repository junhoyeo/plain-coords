class 문석쌤튜플(tuple):
    def __add__(self, other):
        # '+' 연산자를 오버로딩할(내가 정의하는 함수로 덮어씌울) 거예요
        assert len(self) == len(other) 
        # self랑 other(더하는 두 튜플)가 같은 길이를 가졌다고 가정
        return tuple([x + y for x, y in zip(self, other)])
        # 더해버려~

결과 = 문석쌤튜플((2, 3)) + 문석쌤튜플((4, -1))
print(결과) # (6, 2)
