
# LIS Response List LIS Public Order View

The api response class.

## Structure

`LISResponseListLISPublicOrderView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicOrderView`](../../doc/models/lis-public-order-view.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "initialCost": 212.66,
      "isFBFPrinted": false,
      "isSpedUsPrinted": false,
      "incomingBorderoNo": "incomingBorderoNo6",
      "sequenceNo": 24
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

