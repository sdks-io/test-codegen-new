
# LIS Response LIS Public Article

The api response class.

## Structure

`LISResponseLISPublicArticle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicArticle`](../../doc/models/lis-public-article.md) | Optional | - |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "costs": [
      {
        "id": 66,
        "customerId": 96,
        "articleNo": "articleNo0",
        "validFrom": "2016-03-13T12:52:32.123Z",
        "purchasePrice": 62.88
      },
      {
        "id": 65,
        "customerId": 95,
        "articleNo": "articleNo1",
        "validFrom": "2016-03-13T12:52:32.123Z",
        "purchasePrice": 62.89
      }
    ],
    "customerId": 130,
    "articleId": "articleId6",
    "changedOn": "2016-03-13T12:52:32.123Z",
    "changedBy": "changedBy0"
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

