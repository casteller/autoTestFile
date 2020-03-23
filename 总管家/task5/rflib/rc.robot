*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
Setup WebTest
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

TearDown WebTest
    Close Browser














