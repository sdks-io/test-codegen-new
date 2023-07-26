
# LIS Response LIS Public Bordero

The api response class.

## Structure

`LISResponseLISPublicBordero`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicBordero`](../../doc/models/lis-public-bordero.md) | Optional | The LISBordero data contract. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "loadingRelationId": "loadingRelationId0",
    "unloadingRelationId": "unloadingRelationId8",
    "destinationForwarderId": 198,
    "dispositionText": "dispositionText0",
    "remark": "remark8"
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

