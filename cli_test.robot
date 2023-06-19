Documentation      This test case aims to automate the testing of CLI commands for the DigiCloud platform. 
           


*** Settings ***
Library            collections
Library            Process
Library            String
Library            Screenshot
Library            OperatingSystem
Library            SeleniumLibrary
Library            json
Test Setup         Set Log Level    TRACE   
Variables          ./Variables/cli_var.py


*** Test Cases ***

Digi Cli Test Case
    Digicloud login
    Instance create
    Check Instance Details
    Delete Instance
    Show Instance List



*** Keywords ***
# This step involves executing the CLI command to log in to the DigiCloud platform.
# The specific command to be executed will depend on the CLI interface provided by DigiCloud.
Digicloud login
    [Documentation]               Activates the .env digicli
    Set Environment Variable      API_BASE_URL                https://api.digicloud.dev
    ${output}=                    Run Process                 ${LOGIN}                                shell=True
    Should Contain                ${output.stdout}            ir-vanak-plaza

# In this step, the CLI command to create a new instance on the DigiCloud platform is executed. 
# This command may include parameters such as instance type, region, and other specifications.
Instance create
    ${output}=                    Run Process                 ${CREATE_INSTANCE}                      shell=True
    Should Contain                ${output.stdout}            ${INS_NAME}
# After creating the instance, this step focuses on verifying the instance details. 
# The CLI command to retrieve the details of the created instance is executed, and the obtained information is compared against the expected values.
Check Instance Details
    ${output}=                    Run Process                 ${SHOW_INSTANCE}                       shell=True
    ${list}                       Split Command Line          ${output.stdout}            
    Should Contain                ${output.stdout}            BUILD
    Should Contain                ${output.stdout}            ${G1_TYPE}                
    Should Contain                ${output.stdout}            ${UBUNTU_IMG}
    Sleep                         20seconds
# This step involves executing the CLI command to delete the previously created instance. 
# The command may require specifying the instance ID or another identifier to identify the instance to be deleted.
Delete Instance
    
    Run Process                   ${DELETE_INSTANCE}                                                   shell=True
    ${output}=                    Run Process                 ${SHOW_INSTANCE}                         shell=True
    Sleep                         20seconds
# ?The final step of this test case is to execute the CLI command that retrieves a list of instances available on the DigiCloud platform. 
# sThe output of this command is then validated to ensure that the deleted instance no longer appears in the list.
Show Instance List
    ${output}=                    Run Process                 ${INSTANCE_LIST}                          shell=True
    Should Not Contain            ${output.stdout}            ${INS_NAME}                              
