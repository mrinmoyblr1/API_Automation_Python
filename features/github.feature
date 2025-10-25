# Created by mrinmoy at 9/20/25
Feature: GitHub API Validation
  # Enter feature description here

  Scenario: Session Management
    Given I have github credentials
    When I hit getRepo API of github
    Then Status Code of response should be 401
    # Enter steps here