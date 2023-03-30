# tictactoe_oop.py, 객체지향 틱택토 게임
import copy

ALL_SPACES = list('123456789')  # TTTBoard 딕셔너리를 위한 키
X, O, BLANK = 'X', 'O', ' '  # 문자열 값을 위한 상수

def main():
    """틱택토 게임을 실행한다."""
    print('틱택토 게임에 오신 당신을 환영합니다!')
#         if input('미니 보드를 사용하겠습니까? Y/N: ').lower().startswith('y'):
#         gameBoard = MiniBoard()
#     else:
#         gameBoard = TTTBoard()
    gameBoard = HintBoard()
    currentPlayer, nextPlayer = X, O  # X가 선공, O가 후공

    while True:
        print(gameBoard.getBoardStr())  # 화면에 말판을 표시한다

        # 플레이어가 1-9 사이 숫자를 입력할 때까지 계속해서 요청한다
        move = None
        while not gameBoard.isValidSpace(move):
            print(f'{currentPlayer}의 움직임은?(1-9)')
            move = input()
        gameBoard.updatedBoard(move, currentPlayer)  # 움직임을 만든다

        # 게임이 끝났는지 확인한다.
        if gameBoard.isWinner(currentPlayer):  # 먼저 승리를 확인한다
            print(gameBoard.getBoardStr())
            print(currentPlayer + '가 승리했습니다!')
            break
        elif gameBoard.isBoardFull():  # 다음으로 무승부인지 확인한다
            print(gameBoard.getBoardStr())
            print('무승부 게임입니다!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # 턴을 바꾼다
    print('즐겁게 퍼즐을 풀어주셔서 감사합니다!')

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """비어 있는 새 틱택토 말판을 생성한다."""
        self._spaces = {}  # 말판은 파이썬 딕셔너리로 표현된다
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # 모든 칸은 비어 있는 상태로 시작된다

    def GetBoardStr(self):
        """말판을 텍스트로 표현하는 문자열을 반환한다."""
        return f'''
            {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
            -+-+-
            {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
            -+-+-
            {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9
    '''
    def isValidSpace(self, space):
        """이 말판의 space가 칸을 가리키는 유효한 번호이며, 칸이 비어있을 경우 True를 반환"""
        return 0 < int(space) < 10 and (space in ALL_SPACES or self._spaces[space] == BLANK)

    def isWinner(self, player):
        """플레이어가 이 게임에서 승자인 경우 True를 반환"""
        s, p = self._spaces, player  # 편의 문법으로 더 짧은 이름을 사용한다
        return ((s['1'] == s['2'] == s['3'] == p) or  # 상단에 걸쳐서
                (s['4'] == s['5'] == s['6'] == p) or  # 중단에 걸쳐서)
                (s['7'] == s['8'] == s['9'] == p) or  # 하단에 걸쳐서
                (s['1'] == s['4'] == s['7'] == p) or  # 좌측 열 아래로
                (s['2'] == s['5'] == s['8'] == p) or  # 중앙 열 아래로
                (s['3'] == s['6'] == s['9'] == p) or  # 우측 열 아래로
                (s['3'] == s['5'] == s['7'] == p) or  # 대각선
                (s['1'] == s['5'] == s['9'] == p))  # 대각선

    def isBoardFull(self):
        """말판의 모든 칸이 차 있다면 True를 반환한다."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # 한 칸이라도 비어 있으면 False를 반환한다
        return True  # 어느 칸도 비어 있지 않으면, True를 반환한다

    def updateBoard(self, space, player):
        """말판의 space를 player로 설정한다"""
        self._spaces[space] = player

# class MiniBoard(TTTBoard):
#     def getBoardStr(self):
#         """말판의 텍스트 표현을 작게 하는 문자열을 반환한다."""
#         # 공백 한 칸을 '.'으로 치환한다
#         for space in ALL_SPACES:
#             if self._spaces[space] == BLANK:
#                 self._spaces[space] = '.'

#         boardStr = f'''
#             {self._spaces['1']}{self._spaces['2']}{self._spaces['3']} 123
#             {self._spaces['4']}{self._spaces['5']}{self._spaces['6']} 456
#             {self._spaces['7']}{self._spaces['8']}{self._spaces['9']} 789
#         '''

#         # 공백 한 칸을 '.'으로 치환한다
#         for space in ALL_SPACES:
#             if self._spaces[space] == '.':
#                 self._spaces[space] = BLANK
#         return boardSt


class HintBoard(TTTBoard):
    def getBoardStr(self):
        """힌트가 포함된 말판을 텍스트로 표현하는 문자열을 반환한다."""
        boardStr = super().getBoardStr()  # TTTBoard에 있는 getBoardStr()를 호출한다

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces  # _spaces를 백업한다
        for space in ALL_SPACES:  # 모든 칸을 확인한ㄷ
            # 이 칸에서 X 이동을 시뮬레이션한다
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            # 이 칸에서 O 이동을 시뮬레이션한다
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += '\nX는 한 번만 더 이동하면 승리할 수 있습니다.'
        if oCanWin:
            boardStr += '\nO는 한 번만 더 이동하면 승리할 수 있습니다.'
        self._spaces = originalSpaces
        return boardStr
    
if __name__ == '__main__':
    main()  # 임포트하지 않고 이 모듈이 실행되면 main()을 호출한다.
