*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=   Get Contact List
    ${contact}=  New Contact    firstname=Name_1   lastname=Name_2  mobile=111
    Create Contact   ${contact}
    ${new_list}=   Get Contact List
    Append To List    ${old_list}    ${contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}

Delete contact
    ${old_list}=   Get Contact List
    ${len}=    Get Length    ${old_list}
    ${index}=    Evaluate   random.randrange(${len})    random
    ${contact}=   Get From List   ${old_list}   ${index}
    Delete Contact   ${contact}
    ${new_list}=   Get Contact List
    Remove Values From List    ${old_list}    ${contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}

Edit contact
    ${old_list}=   Get Contact List
    ${len}=    Get Length    ${old_list}
    ${index}=    Evaluate   random.randrange(${len})    random
    ${random_contact}=   Get From List   ${old_list}   ${index}
    ${edit_contact}=  New Contact    firstname=Name_1   lastname=Name_2  mobile=111
    Edit Contact    ${random_contact}    ${edit_contact}
    ${new_list}=   Get Contact List
    Replace Values List    ${old_list}   ${index}   ${edit_contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}
