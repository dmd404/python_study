import copy
import sys

TOTAL_DISKS = 5

SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """하노이 탑 게임 실행"""
    print(
        """하노이 탑, 작성자: dmd
탑에 쌓인 원판을 하나씩 다른 탑으로 이동한다.
큰 원판은 작은 원판 위에 놓일 수 없다.

추가 정보는 https://en.wikipedia.org/wiki/Tower_of_hanoi 참고
"""
    )

    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # 이 루프문이 한 번 순회할 때마다 한 턴을 진행
        # 탑과 원판 표시
        displayTowers(towers)

        # 사용자에게 이동 명령 요청
        fromTower, toTower = getPlayerMove(towers)

        # 맨 위 원판을 fromTower에서 toTower로 이동
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # 사용자가 퍼즐을 풀었는지 확인
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)  # 마지막으로 탑 표시
            print("퍼즐을 풀었습니다!")
            sys.exit()


def getPlayerMove(towers):
    """플레이어에게 이동 명령 요청. (fromTower, toTower) 반환."""

    while True:  # 플레이어가 유효한 이동 명령 입력할 때까지 계속 요청
        print('탑의 "시작"과 "끝"의 글자 또는 QUIT를 입력하시오.')
        print("(예: 탑 A에서 탑 B로 원판을 이동하려면 AB를 입력합니다.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("즐겁게 퍼즐 풀어줘서 감사")
            sys.exit()

        # 사용자가 유효한 탑 문자 입력했는지 확인
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("AB, AC, BA, BC, CA, CB 중 하나를 입력하십시오.")
            continue  # 플레이어에게 이동 명령 다시 요청

        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # fromtower는 비어 있을 수 없다
            print("원판이 없는 탑을 선택했음")
            continue  # 플레이어에게 이동 명령 다시 요청
        elif len(towers[toTower]) == 0:
            # 어떤 원판이라도 빈 "toTower"로 이동 가능
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("더 작은 원판에 더 큰 원판을 올릴 수 없음.")
            continue  # 이동 명령 재요청
        else:
            # 유효한 움직임이므로 선택된 탑 반환
            return fromTower, toTower


def displayTowers(towers):
    """세 탑에 배치된 원판 표시"""

    # 세 탑 표시
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0)  # 원판이 없는 빈 기둥 표시
            else:
                displayDisk(tower[level])  # 원판 표시
        print()

    # 탑 이름 A, B, C 표시
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))


def displayDisk(width):
    """주어진 width로 원판을 표시. width가 0이면 원판이 없음을 의미."""
    emptySpace = " " * (TOTAL_DISKS - width)

    if width == 0:
        # 원판이 없는 기둥 표시
        print(f'{emptySpace}||{emptySpace}', end="")
    else:
        # 원판 표시
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f'{emptySpace}{disk}{numLabel}{disk}{emptySpace}', end="")


# 이 프로그램이 (임포트되지 않고) 단독으로 실행되면, 게임 시작
if __name__ == '__main__':
    main()
