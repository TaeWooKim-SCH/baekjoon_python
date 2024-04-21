# 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 28명 제출 -> 제출 안 한 학생 2명의 출석번호를 구하는 프로그램

# 입력: 28줄, 출석 번호에 중복은 없음
# 출력: 2줄, 1번째 줄 -> 제출하지 않은 학생의 출석 번호 중 가장 작은 것
# 2번째 줄 -> 그 다음 출석 번호 출력

def assignment():
  attendance = [False] * 30;
  for i in range(28):
    attendance[int(input()) - 1] = True;
  return [j + 1 for j, value in enumerate(attendance) if value == False];

answerList = assignment()
print(answerList[0]);
print(answerList[1]);

