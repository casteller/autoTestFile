*** Settings ***
Library    SeleniumLibrary
Resource   rc.robot

*** Test Cases ***
用例1
    [Setup]  DeleteAllCourse
    Loginwebsite
    Addcourse  python  一门编程语言  2
    ${lessons} =  GetcourseList
    should be true  $lessons == [u"python"]
    TearDown WebTest
    [Teardown]  DeleteAllCourse
用例2
    [Setup]  DeleteAllCourse
    Loginwebsite
    Addcourse  java  另一门编程语言  1
    ${lessons} =  GetcourseList
    should be true  $lessons == [u"java"]
    TearDown WebTest








