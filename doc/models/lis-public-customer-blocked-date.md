
# LIS Public Customer Blocked Date

The LISCustomerBlockedDate data contract.

## Structure

`LISPublicCustomerBlockedDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `address_type` | [`AddressTypeEnum`](../../doc/models/address-type-enum.md) | Optional | Gets or sets AddressType. |
| `blocked_from` | `datetime` | Optional | Gets or sets BlockedFrom. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |
| `unlock_date` | `datetime` | Optional | Gets or sets the unlock date. |
| `lock_status` | [`LockStatusEnum`](../../doc/models/lock-status-enum.md) | Optional | Gets or sets the lock status. |
| `lock_reason` | `string` | Optional | Gets or sets the lock reason. |
| `unlock_reason` | `string` | Optional | Gets or sets the unlock reason. |
| `blocked_date_id` | `int` | Optional | Gets or sets the blocked from identifier. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "addressType": "FinalRecipient",
  "blockedFrom": "2016-03-13T12:52:32.123Z",
  "trackChanges": false,
  "hasChanges": false
}
```

