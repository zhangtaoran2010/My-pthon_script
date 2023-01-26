import easygui
answer = easygui.enterbox("梗晋休不休和呦?: ")
mes = easygui.buttonbox("厚！迪南塞莱！",
                        choices = ['欸汪','套日安','浩king'])
if answer == "休":
    easygui.msgbox("休！提狄伯侯，堂自从么,畜晋平安孙！")
elif answer == "牟烧":
    easygui.msgbox("牟？了迈卡提！叻旦丢瓦帕！")
if mes == '欸汪':
    easygui.msgbox("厚！欸汪先来！")
elif mes == '套日安':
    easygui.msgbox("厚！套日安先来")
elif mes == '浩king':
    easygui.msgbox('浩king，了但丢瓦帕！')




