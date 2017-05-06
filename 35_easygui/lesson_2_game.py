import easygui as g
import sys

while 1:
    g.msgbox("welcome to first fishC game")
    
    msg="what did you learn in fishC ?"
    title="choice box"
    choices=['love','programming','ooxx','draw picture']
    #choicebox
    choice=g.choicebox(msg,title,choices)
    #msgbox
    g.msgbox("your choice is [" + str(choice)+"].","result")
    msg="do you want play again?"
    title='please choice'
    #ccbox
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
    
    