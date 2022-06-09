# [LC_combine-two-tables](https://leetcode.com/problems/combine-two-tables)

* en

  ```en
  query for a report that provides following information for each person in Person table
  Regardless if is an address for each of those people: FirstName, LastName, City, State
  ```

* tc

  ```tc
  Input:

  | Column Name | Type    |
  | ----------- | ------- |
  | PersonId    | int     |
  | FirstName   | varchar |
  | LastName    | varchar |

  Output:

  | Column Name | Type    |
  | ----------- | ------- |
  | AddressId   | int     |
  | PersonId    | int     |
  | City        | varchar |
  | State       | varchar |
  ```

## Solution

* sql

  ```sql
  SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person
    LEFT JOIN Address ON Person.PersonId = Address.PersonId;
  ```
