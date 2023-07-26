
# LIS Response LIS Public Tour

The api response class.

## Structure

`LISResponseLISPublicTour`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicTour`](../../doc/models/lis-public-tour.md) | Optional | The public tour |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "tourId": 132,
    "tourNo": 172,
    "dossierNo": "dossierNo8",
    "state": "Printed",
    "loadingDate": "2016-03-13T12:52:32.123Z"
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

