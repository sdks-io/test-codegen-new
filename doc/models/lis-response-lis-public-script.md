
# LIS Response LIS Public Script

The api response class.

## Structure

`LISResponseLISPublicScript`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicScript`](../../doc/models/lis-public-script.md) | Optional | This class represents a script that can be used for execution. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "scriptId": "scriptId6",
    "scriptName": "scriptName6",
    "eventType": "WMS_SwitchLocationIsAllowed",
    "implementationType": "implementationType2",
    "pythonCode": "pythonCode8"
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

