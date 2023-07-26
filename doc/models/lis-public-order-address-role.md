
# LIS Public Order Address Role

The LISOrderAddressRole data contract.

## Structure

`LISPublicOrderAddressRole`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `sequential_no` | `int` | Optional | Gets or sets SequentialNo. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `address_type_id` | `int` | Optional | Gets or sets AddressTypeId. |
| `note` | `string` | Optional | Gets or sets Note. |

## Example (as JSON)

```json
{
  "orderId": 62,
  "sequentialNo": 252,
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8",
  "customerId": 114
}
```

