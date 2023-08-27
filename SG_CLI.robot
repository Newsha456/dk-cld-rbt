*** Settings ***
Library            Collections
Library            Process
Library            String
Library            Screenshot
Library            OperatingSystem
Library            SeleniumLibrary
Library            json
Library            ./Variables/cli_var.py
Test Setup         Set Log Level    TRACE   
Variables          ./Variables/cli_var.py


*** Test Cases ***
SG Cli Test Case
    Digicloud login
    # Multi Server Group Create
    Create Instances With Single Server Group    
    # Delete Instance
    # Show Instance List


*** Keywords ***
    
Digicloud login
    Set Environment Variable      API_BASE_URL                        https://api.digicloud.dev
    Run Process                   ${LOGOUT}                           shell=True
    ${output}=                    Run Process                         ${LOGIN}                                shell=True
    Should Contain                ${output.stdout}                    ir-vanak-plaza
Multi Server Group Create
    ${SG_NAMEs}=    Create List 
    ${SG_CREATE_RESULT}=     Set Variable        ${None}
    FOR        ${counter}     IN RANGE    0    11    1

        Log To Console    ${counter}
        ${chosen_sg_t}=  Evaluate  random.choice($SERVER_GROUPS_TYPE)  random      
        ${values}=    Run Keyword    SG_CREATEs   ${chosen_sg_t}
        ${SG_CREATE} =  Set Variable   ${values}[0]
        ${SG_NAME} =   Set Variable  ${values}[1]
        Append To List    ${SG_NAMEs}       ${SG_NAME}
        Log To Console    ${SG_NAME}
        IF         '${chosen_sg_t}' == '${ANTI_AFFINITY}'
            ${SG_CREATE_A}=    Set Variable    ${SG_CREATE} --rules max_server_per_host=1
            Log To Console    ${SG_CREATE_A}
            ${SG_CREATE_RESULT}=    Run Process       ${SG_CREATE_A}          shell=True

            Log To Console    ${SG_CREATE_RESULT.stdout}  
        ELSE
            ${SG_CREATE_RESULT}=           Run Process        ${SG_CREATE}                        shell=True

            
            Log To Console    ${SG_CREATE_RESULT.stdout}  
                              
        END
        ${contains}        Run Keyword And Return Status    Should Contain    ${SG_CREATE_RESULT.stdout}    ${SG_QOUTA_ERROR}
        Run Keyword If     ${contains}  Exit For Loop

        
    END    
    Log To Console         print${contains}
    ${output}=             Run Process                         ${SG_SHOW}                              shell=True
    Sleep    30s
    FOR    ${i}    IN    @{SG_NAMEs}
        ${sg_del_command}=    Run Keyword    SG_DEL   ${i}
        Run Process    ${sg_del_command}     shell=True        
    END


Create Instances With Single Server Group
    ${values}=    Run Keyword    SG_CREATEs   ${ANTI_AFFINITY}
    ${SG_CREATE} =  Set Variable   ${values}[0]
    ${SG_NAME} =   Set Variable  ${values}[1]
    ${output} =  Run Process           ${SG_CREATE}     shell=True
    Log To Console    ${output}

    FOR        ${counter}     IN RANGE    0    6    1
        ${chosen_ins_type}=  Evaluate  random.choice($INSTANCE_TYPES)  random
        ${values}=    Run Keyword    INS_CREATEs   ${chosen_ins_type}
        ${INS_CREATE}=  Set Variable  ${values}[0]
        ${INS_NAME}=   Set Variable  ${values}[1]
        ${INS_CREATE_RESULT}=                    Run Process                 ${INS_CREATE} --server-group ${SG_NAME}                      shell=True
        Sleep                         5seconds
        Log To Console    ${INS_CREATE_RESULT.stdout}
        Log To Console    ${counter}
        # Should Contain                ${INS_CREATE_RESULT.stdout}            ${INS_NAME}
        ${ins_qouta}        Run Keyword And Return Status    Should Contain    ${INS_CREATE_RESULT.stdout}    ${INS_SG_QOUTA_ERROR}
        Run Keyword If     ${ins_qouta}  Exit For Loop
    END
    ${SG_RESULT}=         Run Process        ${SG_SHOW}                shell=True
    Log To Console        ${SG_RESULT.stdout}