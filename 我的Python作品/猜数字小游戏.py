#自制猜数字小游戏（easygui自制升级版）
# 灵感来自于修电脑的师傅
# Filename:猜数字小游戏
import random,easygui
secret = random.randint(1,1000)
guess = 0
tries = 0
answer = easygui.buttonbox("老总，你想玩猜数字游戏吗？",
                           choices = ['不玩','玩'])
if answer == '玩':
    easygui.msgbox("好的老总，准备开始游戏，游戏，走你！")
if answer == '不玩':
    easygui.msgbox("对不起老总，不玩也得玩哦！游戏，走你！")
while guess != secret and tries < 3:
    guess = easygui.integerbox("猜猜数字是几？",upperbound = 1000)
    if not guess:break
    if guess > secret:
        easygui.msgbox(str(guess) + "这也高了吧！老总！")
    elif guess < secret:
        easygui.msgbox(str(guess) + "低了老总！")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("老总666！今晚我请客！")
else:
    easygui.msgbox("对不起老总，没机会了哦！请点击Run Module或F5重新开始吧！")
    easygui.msgbox("对了，记得今晚请我哦！谢谢老总！老总666！")
    easygui.msgbox("Game over!")
