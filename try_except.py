i=0
while (i<5):
 try:
    beichushu=int(input("请输入被除数："))
    chushu=int(input("请输入除数："))
    print('\n',beichushu,'/',chushu,'=',beichushu/chushu)
#  except (ValueError,ZeroDivisionError):
#     print(" \n请输入整数或者除数不能为零")
#  except ZeroDivisionError:
#    print("\n除数不能为零，请重新输入！")
 except(ZeroDivisionError,ValueError) as e:
   print("输入错误:",e)
 i=i+1
    