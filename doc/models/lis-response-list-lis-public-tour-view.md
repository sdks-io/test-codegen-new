
# LIS Response List LIS Public Tour View

The api response class.

## Structure

`LISResponseListLISPublicTourView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicTourView`](../../doc/models/lis-public-tour-view.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "cashPayment": "cashPayment2",
      "isCreditInvoiced": 94,
      "isInvoiceInvoiced": 250,
      "tourId": 118,
      "tourNo": 78
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

