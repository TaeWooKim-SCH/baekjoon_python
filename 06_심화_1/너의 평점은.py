gradeTable = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0
};

gradeInfo = {};

for _ in range(20):
  className, credit, grade = input().split(' ');
  gradeInfo[className] = [float(credit), grade];

def gradeCalculate(gradeInfoDict: dict):
  creditSum = 0;
  gradeSum = 0;
  for credit, grade in gradeInfoDict.values():
    if (grade == 'P'):
      continue;
    creditSum += credit;
    gradeSum += credit * gradeTable[grade];
  return gradeSum / creditSum;

print(gradeCalculate(gradeInfo));