
# LIS Public Special Invoice Position

Position of a special invoice

## Structure

`LISPublicSpecialInvoicePosition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Optional | Description for the special invoice position |
| `date_of_supply` | `datetime` | Required | Date of supply |
| `amount_net` | `float` | Optional | Net amount |
| `amount_currency_id` | `string` | Required | Currency identifier of the amount |
| `sales_tax_id` | `string` | Required | Identifier of the sales tax |
| `account_table_sap` | `string` | Optional | AccountTableSAP |
| `charge_id` | `int` | Optional | Identifier of the charge |
| `cost_center_sap` | `string` | Optional | CostCenterSAP |
| `cost_unit_sap` | `string` | Optional | CostUnitSAP |
| `order_no` | `int` | Optional | Number of the order |
| `tour_no` | `int` | Optional | Number of the tour |
| `account_table` | `int` | Optional | AccountTable |
| `cost_center` | `int` | Optional | CostCenter |
| `cost_unit` | `int` | Optional | CostUnit |
| `division_id` | `int` | Optional | Identifier of the division |
| `department_id` | `int` | Optional | Identifier of the department |

## Example (as JSON)

```json
{
  "description": "description0",
  "dateOfSupply": "2016-03-13T12:52:32.123Z",
  "amountNet": 163.56,
  "amountCurrencyId": "amountCurrencyId2",
  "salesTaxId": "salesTaxId8",
  "accountTableSAP": "accountTableSAP4",
  "chargeId": 240,
  "costCenterSAP": "costCenterSAP2"
}
```

