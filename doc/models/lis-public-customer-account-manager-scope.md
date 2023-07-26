
# LIS Public Customer Account Manager Scope

The LISCustomerAccountManagerScope data contract.

## Structure

`LISPublicCustomerAccountManagerScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_managers` | [`List of LISPublicCustomerManager`](../../doc/models/lis-public-customer-manager.md) | Optional | Gets or sets AccountManagers. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |

## Example (as JSON)

```json
{
  "accountManagers": [
    {
      "customerId": 189,
      "foreignContactPerson": 75,
      "contactPersonId": 225,
      "customerManagerType": "CustomerManager",
      "changedOn": "2016-03-13T12:52:32.123Z"
    }
  ],
  "trackChanges": false,
  "hasChanges": false
}
```

