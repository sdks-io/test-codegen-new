
# LIS Public Customer Group Booking Scope

The LISCustomerGroupBookingScope data contract.

## Structure

`LISPublicCustomerGroupBookingScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `create_foreign_credit_voucher_number_flag` | `bool` | Optional | Gets or sets CreateForeignCreditVoucherNumberFlag. |
| `create_foreign_debit_voucher_number_flag` | `bool` | Optional | Gets or sets CreateForeignDebitVoucherNumberFlag. |
| `switch_debit_print_to_stat_currency_flag` | `bool` | Optional | Gets or sets SwitchDebitPrintToStatCurrencyFlag. |
| `switch_credit_print_to_stat_currency_flag` | `bool` | Optional | Gets or sets SwitchCreditPrintToStatCurrencyFlag. |
| `supress_debit_generation_incoming_invoice_flag` | `bool` | Optional | Gets or sets SupressDebitGenerationIncomingInvoiceFlag. |
| `supress_debit_generation_invoice_flag` | `bool` | Optional | Gets or sets SupressDebitGenerationInvoiceFlag. |
| `supress_debit_generation_special_invoice_flag` | `bool` | Optional | Gets or sets SupressDebitGenerationSpecialInvoiceFlag. |
| `supress_credit_generation_incoming_invoice_flag` | `bool` | Optional | Gets or sets SupressCreditGenerationIncomingInvoiceFlag. |
| `supress_credit_generation_invoice_flag` | `bool` | Optional | Gets or sets SupressCreditGenerationInvoiceFlag. |
| `supress_credit_generation_special_invoice_flag` | `bool` | Optional | Gets or sets SupressCreditGenerationSpecialInvoiceFlag. |
| `finance_mandantor_crediting` | `int` | Optional | Gets or sets FinanceMandantorCrediting. |
| `finance_mandantor_debiting` | `int` | Optional | Gets or sets FinanceMandantorDebiting. |

## Example (as JSON)

```json
{
  "createForeignCreditVoucherNumberFlag": false,
  "createForeignDebitVoucherNumberFlag": false,
  "switchDebitPrintToStatCurrencyFlag": false,
  "switchCreditPrintToStatCurrencyFlag": false,
  "supressDebitGenerationIncomingInvoiceFlag": false
}
```

