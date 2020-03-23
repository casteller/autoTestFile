*** Settings ***
Library    SeleniumLibrary
Library    pylib.userlib

*** Test Cases ***
添加用户-tc001
     ${yzm} =   getyzm   17358983751
     adduser   17358983751   3    内部测试1227   内部测试1227   666666   666666  ${yzm}












