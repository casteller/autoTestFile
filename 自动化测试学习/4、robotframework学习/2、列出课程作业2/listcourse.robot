*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    coursemgr.py
*** Test Cases ***
用例1
    ${courselist} =  listCourse
     :FOR  ${course}   IN   @{courselist}
        \  log to console  ${course}

    ${expected} =   create list  python  selenium
    lists should be equal   ${courselist}   ${expected}
用例2
    open browser  https://www.vmall.com/index.html  chrome
    set selenium implicit wait  5
    ${eles} =   Get Webelements  xpath = //div[@class='b clearfix']//div[2]//div
    :FOR   ${ele}  IN  @{eles}
           \   log to console   ${ele.text}
    close browser




