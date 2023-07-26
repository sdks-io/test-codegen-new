
# LIS Public Customer Closed Date

The LISCustomerClosedDate data contract.

## Structure

`LISPublicCustomerClosedDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `closed_for_loading` | `bool` | Optional | Gets or sets ClosedForLoading. |
| `closed_for_unloading` | `bool` | Optional | Gets or sets ClosedForUnloading. |
| `closed_from` | `datetime` | Optional | Gets or sets ClosedOn. |
| `closed_till` | `datetime` | Optional | Gets or sets the closed till. |
| `reason` | `string` | Optional | Gets or sets Reason. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "closedForLoading": false,
  "closedForUnloading": false,
  "closedFrom": "2016-03-13T12:52:32.123Z",
  "closedTill": "2016-03-13T12:52:32.123Z"
}
```

