# Created by mrinmoy at 9/14/25
Feature: Verify if Books are added and Deleted using Library API

  @library
  Scenario: Verify AddBook API functionality
    Given The Book details which need to be added to Library
    When We execute the AddBook PostAPI method
    Then Book is successfully added
    And Status Code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given The Book details with <isbn> and <aisle>
    When We execute the AddBook PostAPI method
    Then Book is successfully added
    Examples:
      | isbn | aisle |
      | ABC1 | 1234  |
      | ABC1 | 1235  |
      | ABC1 | 1236  |
      | ABC1 | 1237  |
