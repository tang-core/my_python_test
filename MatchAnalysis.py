from random import random
def printIntro():
           print("这个程序模拟两个选手比赛的可能结果")
           print("程序运行需要A和B选手的能力值（0-1小数表示）")

def getInputs():
           n=int (input("请输入模拟比赛的次数:"))
           a=eval(input("请输入选手A的能力值："))
           b=eval(input("请输入选手B的能力值："))
           return a,b,n

def simNGames(n,probA,probB):
           winsa=winsb=0
           for i in range(n):
                      scoreA,scoreB=simOneGame(probA,probB)
                      if scoreA > scoreB:
                                 winsa+=1
                      else:
                                 winsb+=1
           return winsa,winsb

def simOneGame(probA,probB):
           scoreA,scoreB=0,0
           sim="A"
           while not gameover(scoreA,scoreB):
                      if sim=="A":
                                 if random()<probA:
                                            scoreA+=1
                                 else:
                                            sim="B"
                      else:
                                 if random()<probB:
                                            scoreB+=1
                                 else:
                                            sim="A"
           return scoreA,scoreB
                                
                      

def gameover(a,b):
           if a==15 or b==15:
                      return True
           else:
                      return False

def printSummary(winsa,winsb):
           n=winsa+winsb
           print("竞技分析开始，共模拟{}场比赛".format(n))
           print("选手A获胜{}场，胜率为{:.2f}".format(winsa,winsa/n))
           print("选手B获胜{}场，胜率为{:.2f}".format(winsb,winsb/n))

def main():
           printIntro()
           probA,probB,n=getInputs()
           winsA,winsB=simNGames(n,probA,probB)
           printSummary(winsA,winsB)

main()
