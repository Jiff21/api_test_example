Feature: An example of API Tests /pet/{pet_id}

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
