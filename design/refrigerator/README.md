# Requirement

* Function requirements
  * Refrigerator

    ```json
    {
      "door": {
        "partition": {
          "id": "str",
          "image": "blob",
        },
      },
    }
    ```

  * Manage Foods inside refrigerator

    ```json
    {
      "name": "cabbage",  // Suggestion
      "expired": "2022-12-12",
      "amount": 100,  // Vision
      "door_id": ""
    }
    ```

  * Order

  * Recommendation

    ```json
    {
      "type": ,
      "meal": "enum",
      "allow_missing": 1,
      "diversity": 2,
    }
    ```

  * User

    ```json
    {
      "name": "",
      "num_member": 5,
      "Location": "",
      "preference": ""  // Google
    }
    ```

* Non Functional Requirements
  * Available, Latency, Cloud

## Architecture

* recommend()
  * items
  * preference

## Database

* In memeory, no-sql
