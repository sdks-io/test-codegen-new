
# LIS Public Order Status History

The LISOrderStatusHistory data contract.

## Structure

`LISPublicOrderStatusHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_item` | `int` | Optional | Gets or sets OrderItem. |
| `order_status_history_id` | `int` | Optional | Gets or sets OrderStatusHistoryId. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `order_no` | `int` | Optional | Gets or sets OrderNo. |
| `order_status_id` | `int` | Optional | Gets or sets OrderStatusId. |
| `difference_quantity` | `int` | Optional | Gets or sets DifferenceQuantity. |
| `difference_unit` | `string` | Optional | Gets or sets DifferenceUnit. |
| `note` | `string` | Optional | Gets or sets Note. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `event_date` | `datetime` | Optional | Gets or sets EventDate. |
| `event_time` | `datetime` | Optional | Gets or sets EventTime. |
| `edi_status` | [`EdiStatusEnum`](../../doc/models/edi-status-enum.md) | Optional | Gets or sets EDIStatus. |
| `data_source` | [`DataSourceEnum`](../../doc/models/data-source-enum.md) | Optional | Gets or sets DataSource. |
| `generated_internal_no` | `int` | Optional | Gets or sets GeneratedInternalNo. |
| `carrier_id` | `int` | Optional | Gets or sets CarrierId. |
| `tour_id` | `int` | Optional | Gets or sets TourId. |
| `tour_no` | `int` | Optional | Gets or sets TourNo. |
| `special_invoicing_id` | `int` | Optional | Gets or sets SpecialInvoicingId. |
| `receipt` | `string` | Optional | Gets or sets Receipt. |
| `created_by` | `string` | Optional | Gets or sets CreatedBy. |
| `created_on` | `datetime` | Optional | Gets or sets CreatedOn. |
| `bordero_id` | `int` | Optional | Gets or sets BorderoId. |
| `course` | `string` | Optional | Gets or sets Course. |
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Optional | Gets or sets the type. |
| `status_history_id` | `int` | Optional | Gets or sets the status history id. |

## Example (as JSON)

```json
{
  "orderItem": 142,
  "orderStatusHistoryId": 26,
  "orderId": 62,
  "orderNo": 128,
  "orderStatusId": 50
}
```

