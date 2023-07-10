Documentation      This test case aims to automate the testing of CLI commands for the DigiCloud platform. 
           


*** Settings ***
Library            collections
Library            Process
Library            String
Library            Screenshot
Library            OperatingSystem
# Library            SeleniumLibrary
Library            json
Test Setup         Set Log Level    TRACE   
Variables          ./Variables/cli_var.py


*** Test Cases ***

Digi Cli Test Case
    Digicloud login
    Create Network
    Check Network list
    Update Network
    Create Subnet
    Subnet details
    Create Router
    Router details
    Enable Router Gateway
    Create Router Interface
    Create Public IP
    Public IP details
    Associating Public IP to Router interface


*** Keywords ***
Digicloud login
    [Documentation]               Activates the .env digicli
    Set Environment Variable      API_BASE_URL                https://api.digicloud.dev
    ${output}=                    Run Process                 ${LOGIN}                                shell=True
    Should Contain                ${output.stdout}            ir-vanak-plaza

Create Network
    ${output}=                    Run Process                 ${CREATE_NETWORK}                      shell=True
    Should Contain                ${output.stdout}            ${NET_NAME}
    Should Contain                ${output.stdout}            ACTIVE

Check Network list
    ${output}=                    Run Process                 ${NET_LIST}                       shell=True
    ${list}                       Split Command Line          ${output.stdout}            
    Should Contain                ${output.stdout}            ${NET_NAME}                    

Update Network    
    
    ${output}=                    Run Process                 ${NET_UPDATE}                                                   shell=True
    Should contain                ${output.stdout}            ${NETWORK_NAME_UPDATE}
    Should contain                ${output.stdout}            ${ADMIN_S_UP}
    Sleep                         20seconds

Create Router
    ${output}=                    Run Process                 ${CREATE_ROUTER}                          shell=True
    Should Contain                ${output.stdout}            ${ROUTER_NAME}          
    Should Contain                ${output.stdout}            ${ADMIN_S_UP}


Create Subnet
Subnet details



Enable Router Gateway


Create Router Interface

Create Public IP
Public IP details
Associating Public IP to Router interface
