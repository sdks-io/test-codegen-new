
# LIS Response LIS Public Unit

The api response class.

## Structure

`LISResponseLISPublicUnit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicUnit`](../../doc/models/lis-public-unit.md) | Optional | Data contract for a unit. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "unitId": "unitId4",
    "descSing": "descSing0",
    "descPlural": "descPlural0",
    "description": "description2",
    "changedOn": "2016-03-13T12:52:32.123Z"
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

