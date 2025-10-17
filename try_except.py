i=0
while (i<2):
 try:
    beichushu=int(input("请输入被除数："))
    chushu=int(input("请输入除数："))
    print('\n',beichushu,'/',chushu,'=',beichushu/chushu)
 except ValueError:
   print(" \n请输入整数")
 except ZeroDivisionError:
    print("\n除数不能为零，请重新输入！")
 i=i+1
    