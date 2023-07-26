
# LIS Public Order Lump Sum

The LISOrderLumpSum data contract.

## Structure

`LISPublicOrderLumpSum`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Optional | Gets or sets Amount. |
| `currency` | `string` | Optional | Gets or sets Currency. |
| `price_per` | `int` | Optional | Gets or sets PricePer. |
| `value` | `float` | Optional | Gets or sets Value. |
| `sales_tax_code` | `string` | Optional | Gets or sets SalesTaxCode. |
| `charge_id` | `int` | Optional | Gets or sets ChargeId. |
| `charge_description` | `string` | Optional | Gets or sets ChargeDescription. |
| `cash_discount` | `bool` | Optional | Gets or sets a value indicating whether [cash discount]. |

## Example (as JSON)

```json
{
  "amount": 56.78,
  "currency": "currency0",
  "pricePer": 204,
  "value": 251.52,
  "salesTaxCode": "salesTaxCode6"
}
```

