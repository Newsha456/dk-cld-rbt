documentation 
*** Settings ***
Library            SeleniumLibrary
Library            collections
Library            Process
Library            String
Library            Screenshot
Library            OperatingSystem
Test Setup         Set Log Level                TRACE 
Variables         ./Variables/cons_var.py
# Test Teardown      Close Browser

*** Test Cases ***

Cloud Test Case

    Digicloud login
    Instance create
    Check Instance Details
    Delete Instance
    Show Instance List

*** Keywords ***


Digicloud login      
    Open Browser                                ${DIGI_CLOUD_URL}               Chrome
    Wait Until Page Contains Element            ${LOGIN_PG}
    Input Text                                  ${MAIL_INPUT_BOX}               ${MAIL_VALUE}
    # Wait Until Element Contains                 ${MAIL_INPUT_BOX}               ${MAIL_VALUE}
    Input Text                                  ${PASS_INPUT_BOX}               ${PASS_VALUE}
    Click Element                               ${LOGIN_BUTTON}
    Sleep                                       5seconds
    Wait Until Page Contains                    Price update notice                5seconds
    Click Element                               ${GOT_IT_BTN}
    Wait Until Page Contains Element            ${HOME_PAGE}
Instance create    
    Element Should Contain                      ${REGION_SELECTOR}              ${REGION_NAME} 
    Click Element                               ${SERVICE_DROPDOWN}
    Wait Until Page Contains Element            ${DROPDOWN_DESCRIPTION}
    Click Element                               ${CLOUD_COMPUTING}
    Sleep    5second
    

Check Instance Details



Delete Instance



Show Instance List

