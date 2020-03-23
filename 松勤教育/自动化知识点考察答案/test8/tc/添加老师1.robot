*** Settings ***
Library    pylib.webapizy

*** Test Cases ***
添加老师1 - tc000001
    [Setup]     deleteallteacher
    ${ret0}=    login   auto    sdfsdfsdf
    ${sessionid} =  evaluate  $ret0[1]
    ${ret1}=    addteacher      lirui  李睿  天文老师    1  ${sessionid}  sq888
    should be true     $ret1['retcode']==0
#列出老师，检验一下
    ${ret2}=    listteacher     ${sessionid}
    ${fc}=   evaluate   $ret2['retlist'][0]
    should be true    $fc['id']==$ret1['id']
    [Teardown]    deleteteacher   &{ret1}[id]  ${sessionid}