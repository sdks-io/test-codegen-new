
# LIS Response List LIS Public Order Status History

The api response class.

## Structure

`LISResponseListLISPublicOrderStatusHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicOrderStatusHistory`](../../doc/models/lis-public-order-status-history.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "orderItem": 148,
      "orderStatusHistoryId": 32,
      "orderId": 188,
      "orderNo": 122,
      "orderStatusId": 44
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

