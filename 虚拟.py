# 虚拟张浩钦
import easygui
mes = easygui.buttonbox("今天做了什么事？",
              choices = ['一事无成','1~2件','2件以上','有进步','发现了新大陆','学以致用','ctrl+c','ctrl+v'])
if mes == '一事无成':
    easygui.msgbox("滚滚滚！今天不能出去了！给我死在家里打代码！")
elif mes == '1~2件':
    easygui.msgbox("才做1，2件事就能混出去？有积累到什么吗？有进步吗？自己好好反省一下！")
elif mes == '2件以上':
    easygui.msgbox("可以，出去玩吧！")
elif mes == '有进步':
    easygui.msgbox("Ok! Very good!可以可以，必须奖励！yyds!")
elif mes == '发现了新大陆':
    easygui.msgbox("哇！好家伙！小家伙模仿能力可以啊！不错不错!继续加油哦！")
elif mes == '学以致用':
    easygui.msgbox("哇惨！知其然更知其所以然，举一反三，融会贯通！")
elif mes == 'ctrl+c':
    easygui.msgbox("你想干嘛？给我重新打！")
elif mes == 'ctrl+v':
    easygui.msgbox("别自己骗自己了，给我重新打！")
