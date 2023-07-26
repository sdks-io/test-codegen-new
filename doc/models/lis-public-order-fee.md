
# LIS Public Order Fee

The LISOrderFee data contract.

## Structure

`LISPublicOrderFee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `sequential_no` | `int` | Optional | Gets or sets SequentialNo. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `fieldname` | `string` | Optional | Gets or sets Fieldname. |
| `basis` | [`BasisEnum`](../../doc/models/basis-enum.md) | Optional | Gets or sets Basis. |
| `value` | `float` | Optional | Gets or sets Value. |
| `currency_id` | `string` | Optional | Gets or sets CurrencyId. |
| `sales_tax_id` | `string` | Optional | Gets or sets SalesTaxId. |
| `charge_id` | `int` | Optional | Gets or sets ChargeId. |
| `text` | `string` | Optional | Gets or sets Text. |
| `amount` | `float` | Optional | Gets or sets Amount. |

## Example (as JSON)

```json
{
  "orderId": 62,
  "sequentialNo": 252,
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8",
  "fieldname": "fieldname8"
}
```

