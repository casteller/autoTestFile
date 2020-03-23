*** Settings ***
Library  SeleniumLibrary
Library  Collections
Library  deletecourse.py

*** Test Cases ***
用例1
    [Setup]     deletecourse
    open browser    http://localhost/mgr/login/login.html   chrome
    Set Selenium Implicit Wait   10
    input text       id = username    auto
    input text       id = password    sdfsdfsdf
    click element    css = button
    #添加课程按钮
    click element    xpath = //div[@class='ng-scope']//button//span
    #输入课程名称
    input text      xpath = //div[@ng-if='showAddOne']//input[1]    python
    #详情描述
    input text      xpath = //div[@ng-if='showAddOne']//textarea    一门编程语言
    #展示次序
    input text      xpath = //div[@ng-if='showAddOne']//input[2]    1
    #点击创建课程按钮
    click element   xpath = //button[@ng-click='addOne()']

    ${ele} =     Get Webelement    xpath = //tr[@total-items]//td[2]
    ${lesson} =     create list
    log to console  ${ele.text}
    append to list  ${lesson}  ${ele.text}
    ${expected} =   create list    python
    Lists Should Be Equal    ${lesson}     ${expected}
    close browser
    [Teardown]     deletecourse








