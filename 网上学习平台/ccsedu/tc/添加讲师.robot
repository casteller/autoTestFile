*** Settings ***
Library    pylib.webLib
Suite Setup    open browser
variables  cfg
*** Test Cases ***
添加讲师 - tc001
    login    zhangqingqin      1qaz@WSX
    addteacher
    addkejian


