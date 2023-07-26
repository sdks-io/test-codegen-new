
# LIS Response List LIS Public User

The api response class.

## Structure

`LISResponseListLISPublicUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicUser`](../../doc/models/lis-public-user.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "accountName": "accountName0"
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

