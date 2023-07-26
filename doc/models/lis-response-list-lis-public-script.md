
# LIS Response List LIS Public Script

The api response class.

## Structure

`LISResponseListLISPublicScript`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicScript`](../../doc/models/lis-public-script.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "scriptId": "scriptId0",
      "scriptName": "scriptName0",
      "eventType": "WMS_ConsolidateStocksIsAllowed",
      "implementationType": "implementationType6",
      "pythonCode": "pythonCode2"
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

