
# LIS Public Order Additional Charging

The LISOrderAdditionalCharging data contract.

## Structure

`LISPublicOrderAdditionalCharging`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_additional_charging_id` | `int` | Optional | Gets or sets the order additional charging id. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `basis` | [`BasisEnum`](../../doc/models/basis-enum.md) | Optional | Gets or sets Basis. |
| `address_type_id` | `int` | Optional | Gets or sets AddressTypeId. |
| `invoice_side` | [`InvoiceSideEnum`](../../doc/models/invoice-side-enum.md) | Optional | Gets or sets InvoiceSide. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `information` | `string` | Optional | Gets or sets the information. |
| `general_condition_customer_id` | `int` | Optional | Gets or sets the general condition customer id. |
| `additional_charging_id` | `int` | Optional | Gets or sets the additional charging id. |
| `calculation_shipment_id` | `int` | Optional | Gets or sets the calculation shipment id. |
| `invoice_state` | [`InvoiceStateEnum`](../../doc/models/invoice-state-enum.md) | Optional | Gets or sets the state of the invoice. |
| `lump_sum` | `float` | Optional | Gets or sets the lump sum. |
| `condition_temporary_identifier` | `string` | Optional | Gets or sets the condition temporary identifier. |
| `additional_charging_condition_type` | [`AdditionalChargingConditionTypeEnum`](../../doc/models/additional-charging-condition-type-enum.md) | Optional | Gets or sets the type of the additional charging condition. |
| `has_complex_manual_condition` | `bool` | Optional | Gets or sets a value indicating whether this instance has complex manual condition. |
| `currency` | `string` | Optional | Gets or sets the currency. |
| `price_per` | [`PricePerEnum`](../../doc/models/price-per-enum.md) | Optional | Gets or sets the price per. |
| `amount` | `float` | Optional | Gets or sets the amount. |
| `sales_tax_code` | `string` | Optional | Gets or sets the sales tax code. |
| `charge_id` | `int` | Optional | Gets or sets the charge id. |
| `charge_description` | `string` | Optional | Gets or sets the charge description. |
| `cash_discount` | `bool` | Optional | Gets or sets a value indicating whether [cash discount]. |
| `division_id` | `int` | Optional | - |
| `department_id` | `int` | Optional | - |
| `tour_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "orderAdditionalChargingId": 82,
  "orderId": 62,
  "basis": "Consignee",
  "addressTypeId": 206,
  "invoiceSide": "Any"
}
```

