
# LIS Public Order Short Text

The LISOrderShortText data contract.

## Structure

`LISPublicOrderShortText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text_type` | [`TextTypeEnum`](../../doc/models/text-type-enum.md) | Optional | Gets or sets TextType. |
| `text` | `string` | Optional | Gets or sets Text. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |

## Example (as JSON)

```json
{
  "textType": "Label",
  "text": "text0",
  "orderId": 62
}
```

