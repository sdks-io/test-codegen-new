
# LIS Public Order Coded Text

The LISOrderCodedText data contract.

## Structure

`LISPublicOrderCodedText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | [`DirectionEnum`](../../doc/models/direction-enum.md) | Optional | Gets or sets Direction. |
| `text_type` | `int` | Optional | Gets or sets TextType. |
| `text` | `string` | Optional | Gets or sets Text. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `date_time_value` | `datetime` | Optional | Gets or sets the date time value. |

## Example (as JSON)

```json
{
  "direction": "Incoming",
  "textType": 16,
  "text": "text0",
  "orderId": 62,
  "dateTimeValue": "2016-03-13T12:52:32.123Z"
}
```

