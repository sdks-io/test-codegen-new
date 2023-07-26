
# LIS Public Order Cash on Delivery

The LISOrderCashOnDelivery data contract.

## Structure

`LISPublicOrderCashOnDelivery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carriage_forward_currency` | `string` | Optional | Gets or sets CarriageForwardCurrency. |
| `cash_on_delivery_currency` | `string` | Optional | Gets or sets CashOnDeliveryCurrency. |
| `cash_on_delivery_sales_tax_code` | `string` | Optional | Gets or sets CashOnDeliverySalesTaxCode. |
| `cash_on_delivery` | `float` | Optional | Gets or sets CashOnDelivery. |
| `cash_on_delivery_vat_free` | `float` | Optional | Gets or sets CashOnDeliveryVATFree. |
| `initial_cost` | `float` | Optional | Gets or sets InitialCost. |

## Example (as JSON)

```json
{
  "carriageForwardCurrency": "carriageForwardCurrency4",
  "cashOnDeliveryCurrency": "cashOnDeliveryCurrency0",
  "cashOnDeliverySalesTaxCode": "cashOnDeliverySalesTaxCode4",
  "cashOnDelivery": 138.3,
  "cashOnDeliveryVATFree": 98.1
}
```

