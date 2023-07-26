
# LIS Public Order Invoice Data

A base class for all order data contracts.

## Structure

`LISPublicOrderInvoiceData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `costs` | `float` | Optional | Gets or sets the costs. |
| `costs_error` | `bool` | Optional | - |
| `costs_internal` | `float` | Optional | Gets or sets the costs internal. |
| `costs_internal_error` | `bool` | Optional | - |
| `proceeds` | `float` | Optional | Gets or sets the proceeds. |
| `proceeds_error` | `bool` | Optional | - |
| `proceeds_internal` | `float` | Optional | Gets or sets the proceeds internal. |
| `proceeds_internal_error` | `bool` | Optional | - |
| `currency_id` | `string` | Optional | Gets or sets the currency identifier. |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Optional | Gets or sets the type. |

## Example (as JSON)

```json
{
  "costs": 1.32,
  "costsError": false,
  "costsInternal": 217.5,
  "costsInternalError": false,
  "proceeds": 230.16
}
```

