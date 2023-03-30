# class WizCoin:
#     def __init__(self, galleons, sickles, knuts):
#         """galleons, sickless, knuts로 새로운 WizCoin 객체를 생성한다."""
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts
#         # 참고: __init__() 메소드에는 return 문이 존재해서는 안 된다
#
#
#     def value(self):
#         """이 WizCoin 객체에 포함된 모든 동전으 가치(크넛 단위)"""
#         return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
#
#     def weightInGrams(self):
#         """그램 단위로 동전의 무게를 반환한다."""
#         return (self.galleons * 31.130) + (self.sickles * 11.34) + (self.knuts * 5.0)
import collections, operator

class WizCoinException(Exception):
    """WizCoin 모듈이 잘못 사용될 경우 이 예외를 발생시킨다."""
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """새로운 WizCoin 객체를 galleons, sickles, knuts로 생성한다."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # 주의: __init__() 메소드에는 절대 반환문이 없다.

    @property
    def galleons(self):
        """이 객체의 galleon 동전 숫자를 반환한다."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException('galleons attr must be set to an int, not a' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons attr must be a positive int, not' + value.__class__.__qualname__)
        self._galleons = value
