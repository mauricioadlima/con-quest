*** Settings ***
Documentation     A test suite Con-Quest API.
Library           RequestsLibrary
Library           Collections
Default Tags      api

***Variables***
${HOST}           127.0.0.1
${PORT}           8000
${URL}            http://${HOST}:${PORT}
${DEFAULT_NS}     tmp
${DEFAULT_NAME}   test

*** Keywords ***
Get Status
    ${resp}=                      GET      ${URL}/${DEFAULT_NS}/${DEFAULT_NAME}
    Status Should Be              200      ${resp}
    Should Be Equal As Strings    ['OK']   ${resp.json()["status"]}

*** Test Cases ***
Should test creating a questdb instance
    &{data}=            Create dictionary   name=${DEFAULT_NAME}   namespace=${DEFAULT_NS}
    ${resp}=            POST                ${URL}                 json=${data}
    Status Should Be    200                 ${resp}


Should test the return status of a questdb instance
    Wait Until Keyword Succeeds   10x
    ...                           1s
    ...                           Get Status


Should test deleting a questdb instance
    ${resp}=            DELETE  ${URL}/${DEFAULT_NS}/${DEFAULT_NAME}
    Status Should Be    200     ${resp}