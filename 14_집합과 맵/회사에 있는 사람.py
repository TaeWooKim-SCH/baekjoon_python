# 로그에서 어떤 사람이 회사에 들어왔는지, 나갔는지 기록됨
# 현재 회사에 있는 모든 사람은?
# 첫째 줄: 출입 기록 수 n
# 다음 n개의 줄: 출입 기록
# 출력: 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력

n = int(input());
logs = dict();
result = [];

for _ in range(n):
  name, status = input().split(' ');

  # 출입 상태 형식 변환
  if (status == 'enter'):
    status = True;
  else:
    status = False;
  
  # 출입 기록에 따라 데이터 변경
  if (name in logs):
    if (status):
      logs[name] = True;
    else:
      logs[name] = False;
  else:
    logs[name] = status;

for name in logs.keys():
  if (logs[name]):
    result.append(name);

result.sort();
result.reverse();

print('\n'.join(result));



