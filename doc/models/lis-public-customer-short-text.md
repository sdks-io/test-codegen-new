
# LIS Public Customer Short Text

The LISCustomerShortText data contract.

## Structure

`LISPublicCustomerShortText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `section` | [`SectionEnum`](../../doc/models/section-enum.md) | Optional | Gets or sets Section. |
| `function` | [`FunctionEnum`](../../doc/models/function-enum.md) | Optional | Gets or sets Function. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `description` | `string` | Optional | Gets or sets Description. |
| `number` | `int` | Optional | Gets or sets Number. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "section": "Sales",
  "function": "Delivery",
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8"
}
```

