
# LIS Public Customer Manager

The LISCustomerAccountManager data contract.

## Structure

`LISPublicCustomerManager`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `foreign_contact_person` | `int` | Optional | Gets or sets ExternalContactPersonId. |
| `contact_person_id` | `int` | Optional | Gets or sets AccountManagerId. |
| `customer_manager_type` | [`CustomerManagerTypeEnum`](../../doc/models/customer-manager-type-enum.md) | Optional | Gets or sets State. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `mail` | `string` | Optional | Gets or sets EMail. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "foreignContactPerson": 28,
  "contactPersonId": 78,
  "customerManagerType": "Purchase",
  "changedOn": "2016-03-13T12:52:32.123Z"
}
```

