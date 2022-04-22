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

*** Test Cases ***
Create new QuestDB instance
    &{data}=            Create dictionary  name=${DEFAULT_NAME}   namespace=${DEFAULT_NS}
    ${resp}=            POST  ${URL}  json=${data}
    Status Should Be    200    ${resp}

Get a QuestDB status by name
    ${resp}=                    GET                         ${URL}/${DEFAULT_NS}/${DEFAULT_NAME}
    Status Should Be            200                         ${resp}
    Should Be Equal As Strings  ['OK']                      ${resp.json()["status"]}

Delete a QuestDB instance
    DELETE  ${URL}/${DEFAULT_NS}/${DEFAULT_NAME}