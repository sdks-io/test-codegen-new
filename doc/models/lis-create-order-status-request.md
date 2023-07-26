
# LIS Create Order Status Request

Request object for creating an order status.

## Structure

`LISCreateOrderStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_id` | `int` | Required | The identifier of order status which should be created. |
| `order_id` | `int` | Required | The identifier of affected order. |
| `advanced_properties` | [`LISCreateOrderStatusAdvProperties`](../../doc/models/lis-create-order-status-adv-properties.md) | Optional | The LISOrderStatusEntityAdvProperties data contract. |
| `event_date_time` | `datetime` | Optional | The date and time when given status is occured. |
| `receipt` | `string` | Optional | The receipt of given status. |
| `tour_id` | `int` | Optional | The tour id of given status. |
| `bordero_id` | `int` | Optional | The bordero id of given status. |
| `order_status_history_id` | `int` | Optional | The OrderStatusHistoryId id of given status. |
| `do_not_copy_data_ref` | `bool` | Optional | Describes if copying the data reference of given status is allowd. |
| `return_primary_keys` | `bool` | Optional | Describes if primary keys of givenstatus should be returned. |
| `is_manually_recorded` | `bool` | Optional | Describes if givenstatus is manually recorded. |
| `data_reference_id` | `int` | Optional | Gets or sets DataReferenceId. |
| `status_event_id` | [`StatusEventIdEnum`](../../doc/models/status-event-id-enum.md) | Optional | Event Id of given status. |

## Example (as JSON)

```json
{
  "statusId": 250,
  "orderId": 62,
  "advancedProperties": {
    "orderItem": 208,
    "differenceQuantity": 134,
    "differenceUnit": "differenceUnit6",
    "note": "note0",
    "eventDate": "2016-03-13T12:52:32.123Z"
  },
  "eventDateTime": "2016-03-13T12:52:32.123Z",
  "receipt": "receipt4",
  "tourId": 112,
  "borderoId": 222
}
```

