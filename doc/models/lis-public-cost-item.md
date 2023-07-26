
# LIS Public Cost Item

The public cost item

## Structure

`LISPublicCostItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `float` | Optional | Gets or sets the Value. |
| `amount` | `float` | Optional | Gets or sets the Amount. |
| `currency` | `string` | Optional | Gets or sets the currency. |
| `sales_tax_code` | `string` | Optional | Gets or sets the sales tax code. |
| `cost_per` | [`CostPerEnum`](../../doc/models/cost-per-enum.md) | Optional | Gets or sets the cost per. |
| `charge_id` | `int` | Optional | Gets or sets the charge id. |
| `surcharge` | [`LISPublicCostSurchargeItem`](../../doc/models/lis-public-cost-surcharge-item.md) | Optional | The surcharge for costs |

## Example (as JSON)

```json
{
  "value": 251.52,
  "amount": 56.78,
  "currency": "currency0",
  "salesTaxCode": "salesTaxCode6",
  "costPer": "CubicDecimeter"
}
```

