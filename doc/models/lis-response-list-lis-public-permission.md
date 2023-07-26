
# LIS Response List LIS Public Permission

The api response class.

## Structure

`LISResponseListLISPublicPermission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicPermission`](../../doc/models/lis-public-permission.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "accountName": "accountName0",
      "objectName": "objectName6",
      "grantedByName": "grantedByName0",
      "grantedByType": "User",
      "isDefaultRight": false
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

