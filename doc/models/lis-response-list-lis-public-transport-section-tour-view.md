
# LIS Response List LIS Public Transport Section Tour View

The api response class.

## Structure

`LISResponseListLISPublicTransportSectionTourView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicTransportSectionTourView`](../../doc/models/lis-public-transport-section-tour-view.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "trafficModeId": 32,
      "id2": 156,
      "orderNo": 122,
      "orderSubNumber": 152,
      "orderInputType": "IncomingDelivery"
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

