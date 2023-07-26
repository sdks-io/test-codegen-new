
# LIS Public Customer Shipment Scope

The LISCustomerShipmentScope data contract.

## Structure

`LISPublicCustomerShipmentScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `traffic_mode_id` | `string` | Optional | Gets or sets TrafficModeId. |
| `log_model_id` | `int` | Optional | Gets or sets LogModelId. |
| `sales_tax_id` | `string` | Optional | Gets or sets SalesTaxId. |
| `currency_id` | `string` | Optional | Gets or sets CurrencyId. |
| `freight_term_id` | `string` | Optional | Gets or sets FreightTermId. |
| `article_id` | `string` | Optional | Gets or sets ArticleId. |
| `is_reference_number_required` | `bool` | Optional | Gets or sets IsReferenceNumberRequired. |
| `blocked_from_date` | `datetime` | Optional | Gets or sets BlockedFromDate. |
| `transportation_route_id` | `int` | Optional | Gets or sets TransportationRouteId. |
| `order_sender_id` | `int` | Optional | Gets or sets OrderSenderId. |
| `order_recipient_id` | `int` | Optional | Gets or sets OrderRecipientId. |
| `order_freight_payer_id` | `int` | Optional | Gets or sets OrderFreightPayerId. |
| `order_carrier_id` | `int` | Optional | Gets or sets OrderCarrierId. |
| `division_id` | `int` | Optional | Gets or sets DivisionId. |
| `department_id` | `int` | Optional | Gets or sets DepartmentId. |
| `blocked_dates` | [`List of LISPublicCustomerBlockedDate`](../../doc/models/lis-public-customer-blocked-date.md) | Optional | Gets or sets BlockedDates. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |
| `loading_empty` | `bool` | Optional | Gets or sets a value indicating whether [loading empty]. |
| `unloading_empty` | `bool` | Optional | Gets or sets a value indicating whether [unloading empty]. |
| `unlock_date` | `datetime` | Optional | Gets or sets the unlock date. |
| `lock_reason` | `string` | Optional | Gets or sets the lock reason. |
| `unlock_reason` | `string` | Optional | Gets or sets the unlock reason. |
| `lock_status` | [`LockStatusEnum`](../../doc/models/lock-status-enum.md) | Optional | Gets or sets the lock status. |

## Example (as JSON)

```json
{
  "trafficModeId": "trafficModeId2",
  "logModelId": 108,
  "salesTaxId": "salesTaxId8",
  "currencyId": "currencyId4",
  "freightTermId": "freightTermId8"
}
```

