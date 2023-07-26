
# LIS Response List LIS Public Transport Section Base

The api response class.

## Structure

`LISResponseListLISPublicTransportSectionBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicTransportSectionBase`](../../doc/models/lis-public-transport-section-base.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "transportSectionType": "transportSectionType6",
      "borderoId": 216,
      "companyId": 182,
      "divisionId": 100,
      "departmentId": 134
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

