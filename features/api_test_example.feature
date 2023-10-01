Feature: An example of API Tests on the Swagger Pet Store API

  @requests @medium
  Scenario Outline: <method> <uri><parameters> returns expected pet
    Given I "<method>" "<uri>" with the parameters "<parameters>"
    Then it should have a "200" status code
      And the json response should be a list of least "1" items
      And the json response should contain a dog named "<pet_name>"
      And the json response should not contain a dog named "<not_pet>"

    Examples: Filtering by parameters works
    | method  | uri                | parameters         | pet_name    | not_pet  |
    | GET     | /pet/findByStatus  | ?status=available  | Cat 1       | Dog 3    |
    | GET     | /pet/findByStatus  | ?status=pending    | Dog 3       | Cat 1    |
    | GET     | /pet/findByStatus  | ?status=sold       | Dog 2       | Cat 1    |


  @requests @Blocker
  Scenario: All dogs should have a name, status & ID
    Given I "GET" "/pet/findByStatus?status=available" with requests
    Then it should have a "200" status code
      And all dogs should have a name
      And all dogs should have an ID
      And all dogs should have a status
      And should not reveal dog pii


  @requests @medium
  Scenario Outline: <method> <uri><parameters> returns expected pet & status
    Given I "<method>" "<uri>" with the parameters "<parameters>"
    Then it should have a "200" status code
      And the json response should be a dict of least "1" items
      And this dog is named "<pet_name>"
      And this dog's status is "<status>"

    Examples: Filtering by parameters works
    | method  | uri    | parameters | pet_name | status    |
    | GET     | /pet/  | 5          | Dog 2    | sold      |
    | GET     | /pet/  | 2          | Cat 2    | available |
    | GET     | /pet/  | 6          | Dog 3    | pending   |

  @requests @medium @KEY-1 @should-fail
  Scenario: Should upgrade insecure requests
    Given I "GET" "/pet/findByStatus?status=available" with requests
    Then it should have a "200" status code
      And the response should use https
