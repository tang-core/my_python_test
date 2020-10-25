import turtle as t
def KochDraw(size,n):
           if n==0:
                      t.fd(size)
           else:
                      for angle in [0,60,-120,60]:
                                 t.left(angle)
                                 KochDraw(size/3,n-1)   #当前操作与上一步操作的关系
                                                                  #KochDraw(size/3,n-1)表示以二阶的形式，用1/3的线段画
                                                                  #无需考虑底层问题，只需要递归关系，即不同角度画线

def main ():
           t.setup(600,600)
           t.penup()
           t.goto(-200,100)
           t.pendown()
           t.pensize(2)
           level=3
           KochDraw(400,level)
           t.right(120)
           KochDraw(400,level)
           t.right(120)
           KochDraw(400,level)
           t.right(120)
           t.hideturtle()
           
main()

                      
