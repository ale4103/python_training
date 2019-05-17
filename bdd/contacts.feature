Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <mobile>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | lastname  | mobile  |
  | firstname1 | lastname1 | mobile1 |
  | firstname2 | lastname2 | mobile2 |
  | firstname3 | lastname3 | mobile3 |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted

Scenario Outline: Edit a contact
  Given a contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname> and <mobile>
  When I edit the contact from the list
  Then the new contact list is equal to the old contact list

  Examples:
  | firstname  | lastname  | mobile  |
  | firstname1 | lastname1 | mobile1 |