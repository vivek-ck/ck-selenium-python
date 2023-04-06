Feature: Testing JSONPlaceholder API

  Scenario: Retrieve a list of posts
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts"
    When I send a GET request
    Then the response status code should be 200
    And the response body should contain a list of posts

  Scenario: Retrieve a single post
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request
    Then the response status code should be 200
    And the response body should contain a single post

  Scenario: Create a new post
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts"
    And I give the payload from file test_payload.json
    When I send a POST request
    Then the response status code should be 201
    And the response body should contain the newly created post
