
# LIS Public Invoicing Preview Request

## Structure

`LISPublicInvoicingPreviewRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_preview_type` | [`InvoicePreviewTypeEnum`](../../doc/models/invoice-preview-type-enum.md) | Optional | - |
| `invoice_preview_group` | `uuid\|string` | Optional | - |
| `invoice_documents_count` | `int` | Optional | - |
| `invoice_side` | `string` | Optional | - |
| `is_cancellation` | `bool` | Optional | - |
| `cost_allocation` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "invoicePreviewGroup": "00000000-0000-0000-0000-000000000000",
  "invoicePreviewType": "InvoiceReview",
  "invoiceDocumentsCount": 18,
  "invoiceSide": "invoiceSide4",
  "isCancellation": false
}
```

