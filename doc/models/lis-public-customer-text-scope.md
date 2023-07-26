
# LIS Public Customer Text Scope

The LISCustomerTextScope data contract.

## Structure

`LISPublicCustomerTextScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `short_texts` | [`List of LISPublicCustomerShortText`](../../doc/models/lis-public-customer-short-text.md) | Optional | Gets or sets ShortTexts. |
| `notice_1` | `string` | Optional | Gets or sets the notice1. |
| `notice_2` | `string` | Optional | Gets or sets the notice2. |

## Example (as JSON)

```json
{
  "shortTexts": [
    {
      "customerId": 52,
      "section": "Sales",
      "function": "Sender",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy6"
    },
    {
      "customerId": 53,
      "section": "Order",
      "function": "None",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy7"
    }
  ],
  "notice1": "notice10",
  "notice2": "notice26"
}
```

