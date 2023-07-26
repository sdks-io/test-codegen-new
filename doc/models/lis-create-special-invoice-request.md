
# LIS Create Special Invoice Request

Request object for creating a special invoice.

## Structure

`LISCreateSpecialInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | [`LISPublicSpecialInvoice`](../../doc/models/lis-public-special-invoice.md) | Optional | The special invoice |
| `options` | [`LISSpecialInvoiceOptions`](../../doc/models/lis-special-invoice-options.md) | Optional | Options to create a special invoice |

## Example (as JSON)

```json
{
  "entity": {
    "specialInvoiceKind": "NotSet",
    "specialInvoiceDate": "2016-03-13T12:52:32.123Z",
    "description": "description8",
    "customerId": 164,
    "senderId": 116,
    "invoiceDate": "2016-03-13T12:52:32.123Z",
    "bookingNr": "bookingNr2",
    "dateOfBooking": "2016-03-13T12:52:32.123Z",
    "archiveInformation": "archiveInformation4",
    "formType": 236,
    "divisionId": 128
  },
  "options": {
    "bookIncomingVouchers": false
  }
}
```

