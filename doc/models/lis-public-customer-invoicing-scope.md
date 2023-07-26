
# LIS Public Customer Invoicing Scope

The LISCustomerInvoicingScope data contract.

## Structure

`LISPublicCustomerInvoicingScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `general_creditor` | `int` | Optional | Gets or sets GeneralCreditor. |
| `credit_condition_code` | [`CreditConditionCodeEnum`](../../doc/models/credit-condition-code-enum.md) | Optional | Gets or sets CreditConditionCode. |
| `general_debitor` | `int` | Optional | Gets or sets GeneralDebitor. |
| `debit_condition_code` | [`DebitConditionCodeEnum`](../../doc/models/debit-condition-code-enum.md) | Optional | Gets or sets DebitConditionCode. |
| `cargo_insurance` | [`CargoInsuranceEnum`](../../doc/models/cargo-insurance-enum.md) | Optional | Gets or sets CargoInsurance. |
| `invoicing_indicator` | [`InvoicingIndicatorEnum`](../../doc/models/invoicing-indicator-enum.md) | Optional | Gets or sets InvoicingIndicator. |
| `differing_invoicing_address_for_system_traffic` | `int` | Optional | Gets or sets the differing invoicing address for system traffic. |
| `debit_accounting_date` | [`DebitAccountingDateEnum`](../../doc/models/debit-accounting-date-enum.md) | Optional | Gets or sets DebitAccountingDate. |
| `credit_accounting_date` | [`CreditAccountingDateEnum`](../../doc/models/credit-accounting-date-enum.md) | Optional | Gets or sets CreditAccountingDate. |
| `in_advance_route_mode` | [`InAdvanceRouteModeEnum`](../../doc/models/in-advance-route-mode-enum.md) | Optional | Gets or sets the in advance route mode. |

## Example (as JSON)

```json
{
  "generalCreditor": 210,
  "creditConditionCode": "NotSet",
  "generalDebitor": 90,
  "debitConditionCode": "NotSet",
  "cargoInsurance": "Country"
}
```

