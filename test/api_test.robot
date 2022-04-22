*** Settings ***
Documentation     A test suite Con-Quest API.
Library           RequestsLibrary
Default Tags      api

***Variables***
${HOST}           127.0.0.1
${PORT}           8000
${URL}            http://${HOST}:${PORT}

*** Test Cases ***
Get all QuestDB status
    GET  ${URL}

Get a QuestDB status by name
    GET  ${URL}/my-personal-db

Delete a QuestDB instance
    DELETE  ${URL}/my-personal-db

Create new QuestDB instance
    &{data}=            Create dictionary  name=test  namespace=tmp
    ${resp}=            POST  ${URL}  json=${data}
    Status Should Be    200    ${resp}
