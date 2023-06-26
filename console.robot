documentation 
*** Settings ***
Library            SeleniumLibrary
Library            collections
Library            Process
Library            String
# Library            Screenshot
Library            AutoRecorder                  embed_width=400px 
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
    Wait Until Page Contains                    Price update notice                5seconds
    Sleep                                       2seconds
    Click Button                                Got it 
    Wait Until Page Contains Element            ${HOME_PAGE}

Instance create    
    # Element Should Contain                      ${REGION_SELECTOR}              ${REGION_NAME} 
    Click Element                               ${SERVICE_DROPDOWN}
    Wait Until Page Contains Element            ${DROPDOWN_DESCRIPTION}
    Click Element                               ${CLOUD_COMPUTING}
    Wait Until Page Contains Element            ${INS_LIST_PG}                  5seconds
    Click Element                               ${ADD_INS}
    # Page Should Contain Element                 ${CREATE_STEP_ONE}
    # Click Element                               ${IMAGE_TYPE_UBUNTU}
    # Click Element                               ${INS_TYPE}
    # Click Element                               ${CONFIRM_BTN}
    Sleep                                       5second
    Click Element                               ${CREATE_SMP_INS}
    # Page Should Contain Element                 ${ADVANCE_STNG}
    # Click Element                               ${CONFIRM_BTN}
    Input Text                                  ${INS_NAME_INPUT}                 ${INS_NAME}
    # Page Should Contain                         ${IMAGE_TYPE_UBUNTU}    
    # Page Should Contain                         ${INS_TYPE}
    # Page Should Contain                         ${INS_NAME}
    Click Element                               ${CREATE_BTN}

    Wait Until Page Contains Element            ${CREATING_STATE}                 10seconds

Check Instance Details
    Click element                               ${INS_NAME} 


Delete Instance



Show Instance List

