
# LIS Response List LIS Public Script Info

The api response class.

## Structure

`LISResponseListLISPublicScriptInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicScriptInfo`](../../doc/models/lis-public-script-info.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "scriptId": "scriptId0",
      "scriptName": "scriptName0",
      "scriptComment": "scriptComment0",
      "eventType": "WMS_ConsolidateStocksIsAllowed",
      "implementationType": "implementationType6"
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

