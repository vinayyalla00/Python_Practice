

a = 20;
def vinay():
  globals()['a'] = 30
  a = 10;
  print("inside:",a);


vinay();
print("Outside:",a);