- 상수를 파일 맨 위쪽에 정의해 한데 묶고 전역 변수로 만든다.
- 전역 변수 이름은 대문자 SNAKE_CASE 형태로 만들어 상수로 표시
<br>

- SOLVED_TOWER 리스트는 새발에서 가장 간단한 데이터 구조인 stack을 이용한다.
  - 스택은 스택 상단에 값 push 또는 스택 상단에서 값 pop을 통해서만 변경되는, 순서가 보장되는 값들의 리스트다.
<br>

- SOLVED_TOWER에 있는 패턴을 towers["B"], towers["C"]와 비교
- A탑의 기둥은 이미 완성된 형태로 시작하기 때문에 towers["A"]와 비교하지는 않는다.
