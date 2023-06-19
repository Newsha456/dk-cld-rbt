*** Settings ***
Library           SeleniumLibrary
*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.digikala.com
*** Test Cases ***
Digikala Website
    Open Digikala Website


*** Keywords ***   
Open Digikala Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    6s