
# LIS Public Special Invoice

The special invoice

## Structure

`LISPublicSpecialInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `special_invoice_kind` | [`SpecialInvoiceKindEnum`](../../doc/models/special-invoice-kind-enum.md) | Required | Kind of the special invoice |
| `special_invoice_date` | `datetime` | Required | Date of the special invoice |
| `description` | `string` | Optional | Description |
| `customer_id` | `int` | Required | Identifier of the customer. |
| `sender_id` | `int` | Optional | Identifier of the sender |
| `invoice_date` | `datetime` | Required | Date of invoice |
| `booking_nr` | `string` | Required | Booking-Number |
| `date_of_booking` | `datetime` | Required | Date of Booking |
| `archive_information` | `string` | Optional | ArchiveInformation |
| `form_type` | `int` | Optional | FormType |
| `division_id` | `int` | Optional | Identifier of the division |
| `positions` | [`List of LISPublicSpecialInvoicePosition`](../../doc/models/lis-public-special-invoice-position.md) | Optional | Positions to the special invoice |

## Example (as JSON)

```json
{
  "specialInvoiceKind": "IncomingInvoice",
  "specialInvoiceDate": "2016-03-13T12:52:32.123Z",
  "description": "description0",
  "customerId": 114,
  "senderId": 138,
  "invoiceDate": "2016-03-13T12:52:32.123Z",
  "bookingNr": "bookingNr0",
  "dateOfBooking": "2016-03-13T12:52:32.123Z",
  "archiveInformation": "archiveInformation8",
  "formType": 214,
  "divisionId": 106
}
```

