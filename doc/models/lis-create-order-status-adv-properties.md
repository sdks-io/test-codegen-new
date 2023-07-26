
# LIS Create Order Status Adv Properties

The LISOrderStatusEntityAdvProperties data contract.

## Structure

`LISCreateOrderStatusAdvProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_item` | `int` | Optional | Gets or sets OrderItem. |
| `difference_quantity` | `int` | Optional | Gets or sets DifferenceQuantity. |
| `difference_unit` | `string` | Optional | Gets or sets DifferenceUnit. |
| `note` | `string` | Optional | Gets or sets Note. |
| `event_date` | `datetime` | Optional | Gets or sets EventDate. |
| `event_time` | `datetime` | Optional | Gets or sets EventTime. |
| `edi_status` | `int` | Optional | Gets or sets EDIStatus. |
| `data_source` | `int` | Optional | Gets or sets DataSource. |
| `generated_internal_no` | `int` | Optional | Gets or sets GeneratedInternalNo. |
| `carrier_id` | `int` | Optional | Gets or sets CarrierId. |
| `special_invoicing_id` | `int` | Optional | Gets or sets SpecialInvoicingId. |
| `receipt` | `string` | Optional | Gets or sets Receipt. |
| `tour_id` | `int` | Optional | Gets or sets TourId. |
| `tour_no` | `int` | Optional | Gets or sets TourNo. |
| `status_category_id` | `string` | Optional | Gets or sets the status category id. |
| `contact_information` | `string` | Optional | Gets or sets the contact information. |
| `text_master_id` | `int` | Optional | Gets or sets the text master identifier. |
| `long_text` | `string` | Optional | Gets or sets the long text. |

## Example (as JSON)

```json
{
  "orderItem": 142,
  "differenceQuantity": 68,
  "differenceUnit": "differenceUnit8",
  "note": "note4",
  "eventDate": "2016-03-13T12:52:32.123Z"
}
```

