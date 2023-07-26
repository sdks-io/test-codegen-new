
# LIS Response LIS Public Special Invoice

The api response class.

## Structure

`LISResponseLISPublicSpecialInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicSpecialInvoice`](../../doc/models/lis-public-special-invoice.md) | Optional | The special invoice |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "specialInvoiceKind": "NotSet",
    "specialInvoiceDate": "2016-03-13T12:52:32.123Z",
    "description": "description2",
    "customerId": 130,
    "senderId": 106,
    "invoiceDate": "2016-03-13T12:52:32.123Z",
    "bookingNr": "bookingNr2",
    "dateOfBooking": "2016-03-13T12:52:32.123Z",
    "archiveInformation": "archiveInformation4",
    "formType": 202,
    "divisionId": 94
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

