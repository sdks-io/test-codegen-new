
# LIS Public Customer Contact Person Scope

The LISCustomerContactPersonScope data contract.

## Structure

`LISPublicCustomerContactPersonScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_persons` | [`List of LISPublicCustomerContactPerson`](../../doc/models/lis-public-customer-contact-person.md) | Optional | Gets or sets ContactPersons. |

## Example (as JSON)

```json
{
  "contactPersons": [
    {
      "transportTypes": [
        "transportTypes0",
        "transportTypes1"
      ],
      "customerContactPersonId": 50,
      "customerId": 78,
      "name": "name6",
      "forename": "forename4"
    },
    {
      "transportTypes": [
        "transportTypes1",
        "transportTypes2",
        "transportTypes3"
      ],
      "customerContactPersonId": 51,
      "customerId": 79,
      "name": "name7",
      "forename": "forename5"
    },
    {
      "transportTypes": [
        "transportTypes2"
      ],
      "customerContactPersonId": 52,
      "customerId": 80,
      "name": "name8",
      "forename": "forename6"
    }
  ]
}
```

