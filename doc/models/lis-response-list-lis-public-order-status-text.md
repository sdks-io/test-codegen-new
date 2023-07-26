
# LIS Response List LIS Public Order Status Text

The api response class.

## Structure

`LISResponseListLISPublicOrderStatusText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicOrderStatusText`](../../doc/models/lis-public-order-status-text.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy4",
      "statusId": 0,
      "text": "text4",
      "unloadingReport": false
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

