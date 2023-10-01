Feature: An example of API Tests /pet/{pet_id}

  @requests @medium
  Scenario Outline: <method> <uri><parameters> returns expected pet & status
    Given I "<method>" "<uri>" with the parameters "<parameters>"
    Then it should have a "200" status code
      And the json response should be a dict of least "1" items
      And this dog is named "<pet_name>"
      And this dog's status is "<status>"

    Examples: Grabbing pets by ID shows correct pets
    | method  | uri    | parameters | pet_name | status    |
    | GET     | /pet/  | 5          | Dog 2    | sold      |
    | GET     | /pet/  | 2          | Cat 2    | available |
    | GET     | /pet/  | 6          | Dog 3    | pending   |


  @requests @trivial
  Scenario: GET Pet by ID correct error when parameter is left off
    Given I "GET" "/pet/" with requests
    Then it should have a "405" status code
      And the response message should include "HTTP 405 Method Not Allowed"


  @requests @Blocker
  Scenario: GET Pet by ID rejects SQL Injection
    Given I "GET" "/pet/1'+OR+1=1--" with requests
    Then it should have a "400" status code


  @requests @medium
  Scenario: GET Pet by ID 404s when ID does not exist
    Given I "GET" "/pet/10000000000" with requests
    Then it should have a "404" status code
