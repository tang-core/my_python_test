#pythontext.py
import time
scale=10
print("输入开始".center(scale//2),'-')
for i in range(scale+1):
           a=i/10*100
           b='*'*i
           c='-'*(scale-i)
           if i in[10]:
                      c= b+"**"
                      print("{:^3.0f}% [{} ]".format(a,c) )
           else:
                      print("{:^3.0f}% [{}->{}]".format(a,b,c))
           time.sleep(0.1)
           
print("\n"+"执行结束".center(scale//2))
