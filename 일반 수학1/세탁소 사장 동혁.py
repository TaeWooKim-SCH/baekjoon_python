T = int(input());

quarter = 25;
dime = 10;
nickel = 5;
penny = 1;

for _ in range(T):
  C = int(input());
  quarter_c = 0;
  dime_c = 0;
  nickel_c = 0;
  penny_c = 0;

  if (C // quarter > 0):
    quarter_c = C // quarter;
    C -= quarter * quarter_c;
  if (C // dime > 0):
    dime_c = C // dime;
    C -= dime * dime_c;
  if (C // nickel > 0):
    nickel_c = C // nickel;
    C -= nickel * nickel_c;
  if (C // penny > 0):
    penny_c = C // penny;
    C -= penny * penny_c;
  print(C);
  print(quarter_c, dime_c, nickel_c, penny_c);

