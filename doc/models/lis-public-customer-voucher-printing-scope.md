
# LIS Public Customer Voucher Printing Scope

The LISCustomerVoucherPrintingScope data contract.

## Structure

`LISPublicCustomerVoucherPrintingScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `print_debit` | [`PrintDebitEnum`](../../doc/models/print-debit-enum.md) | Optional | Gets or sets PrintDebit. |
| `print_credit` | [`PrintCreditEnum`](../../doc/models/print-credit-enum.md) | Optional | Gets or sets PrintCredit. |
| `debit_form_type` | `int` | Optional | Gets or sets DebitFormType. |
| `debit_own_form_type` | `int` | Optional | Gets or sets DebitOwnFormType. |
| `debit_formular_type` | `int` | Optional | Gets or sets the type of the debit formular. |
| `credit_form_type` | `int` | Optional | Gets or sets CreditFormType. |
| `credit_own_form_type` | `int` | Optional | Gets or sets CreditOwnFormType. |
| `credit_formular_type` | `int` | Optional | Gets or sets the type of the credit formular. |
| `debit_invoicing_period` | [`DebitInvoicingPeriodEnum`](../../doc/models/debit-invoicing-period-enum.md) | Optional | Gets or sets DebitInvoicingPeriod. |
| `credit_invoicing_period` | [`CreditInvoicingPeriodEnum`](../../doc/models/credit-invoicing-period-enum.md) | Optional | Gets or sets CreditInvoicingPeriod. |
| `debit_invoicing_period_grouping` | [`DebitInvoicingPeriodGroupingEnum`](../../doc/models/debit-invoicing-period-grouping-enum.md) | Optional | Gets or sets DebitInvoicingPeriodGrouping. |
| `credit_invoicing_period_grouping` | [`CreditInvoicingPeriodGroupingEnum`](../../doc/models/credit-invoicing-period-grouping-enum.md) | Optional | Gets or sets CreditInvoicingPeriodGrouping. |
| `debit_print_currency` | `string` | Optional | Gets or sets DebitPrintCurrency. |
| `credit_print_currency` | `string` | Optional | Gets or sets CreditPrintCurrency. |
| `print_vat_separately` | `bool` | Optional | - |
| `invoice_conversion` | [`InvoiceConversionEnum`](../../doc/models/invoice-conversion-enum.md) | Optional | Gets or sets InvoiceConversion. |
| `differing_voucher_recipient_debit` | `int` | Optional | Gets or sets DifferingVoucherRecipientDebit. |
| `differing_voucher_recipient_credit` | `int` | Optional | Gets or sets DifferingVoucherRecipientCredit. |
| `aggregated_print_debit` | `bool` | Optional | Gets or sets AggregatedPrintDebit. |
| `incoming_debit` | `bool` | Optional | Gets or sets IncomingDebit. |
| `aggregated_print_credit` | `bool` | Optional | Gets or sets AggregatedPrintCredit. |
| `incoming_credit` | `bool` | Optional | Gets or sets IncomingCredit. |
| `subsequent_charges_on_amount_level` | `bool` | Optional | Gets or sets the subsequent charges on amount level. |
| `print_sort_debit_1` | `string` | Optional | Gets or sets PrintSortDebit1. |
| `print_sort_debit_2` | `string` | Optional | Gets or sets PrintSortDebit2. |
| `print_sort_debit_3` | `string` | Optional | Gets or sets PrintSortDebit3. |
| `print_sort_debit_4` | `string` | Optional | Gets or sets PrintSortDebit4. |
| `print_sort_credit_1` | `string` | Optional | Gets or sets PrintSortCredit1. |
| `print_sort_credit_2` | `string` | Optional | Gets or sets PrintSortCredit2. |
| `print_sort_credit_3` | `string` | Optional | Gets or sets PrintSortCredit3. |
| `print_sort_credit_4` | `string` | Optional | Gets or sets PrintSortCredit4. |
| `group_by_sort_credit_1` | `bool` | Optional | Gets or sets GroupBySortCredit1. |
| `group_by_sort_debit_1` | `bool` | Optional | Gets or sets GroupBySortDebit1. |
| `print_co_2_emissions` | `bool` | Optional | Gets or sets PrintCO2Emissions. |
| `special_invoice_credit_form_type` | `int` | Optional | Gets or sets the type of the special invoice credit form. |
| `special_invoice_credit_own_form_type` | `int` | Optional | Gets or sets the type of the special invoice credit own form. |
| `special_invoice_credit_formular_type` | `int` | Optional | Gets or sets the type of the special invoice credit formular. |
| `special_invoice_debit_form_type` | `int` | Optional | Gets or sets the type of the special invoice debit form. |
| `special_invoice_debit_own_form_type` | `int` | Optional | Gets or sets the type of the special invoice debit own form. |
| `special_invoice_debit_formular_type` | `int` | Optional | Gets or sets the type of the special invoice debit formular. |
| `max_position_count_debit` | `int` | Optional | Gets or sets MaxPositionCountDebit. |
| `max_position_count_credit` | `int` | Optional | Gets or sets MaxPositionCountCredit. |
| `shipping_papers_charges_debit` | `float` | Optional | Gets or sets ShippingPapersChargesDebit. |
| `shipping_papers_charges_credit` | `float` | Optional | Gets or sets ShippingPapersChargesCredit. |
| `shipping_papers_type_debit` | [`ShippingPapersTypeDebitEnum`](../../doc/models/shipping-papers-type-debit-enum.md) | Optional | Gets or sets ShippingPapersTypeDebit. |
| `shipping_papers_type_credit` | [`ShippingPapersTypeCreditEnum`](../../doc/models/shipping-papers-type-credit-enum.md) | Optional | Gets or sets ShippingPapersTypeCredit. |
| `shipping_papers_charges_limit_credit` | `float` | Optional | Gets or sets ShippingPapersChargesLimitCredit. |
| `shipping_papers_charges_limit_debit` | `float` | Optional | Gets or sets ShippingPapersChargesLimitDebit. |
| `fuel_type` | [`FuelTypeEnum`](../../doc/models/fuel-type-enum.md) | Optional | Gets or sets the type of the fuel. |
| `fuel_consumption` | `float` | Optional | Gets or sets the fuel consumption. |
| `average_emissions` | `float` | Optional | Gets or sets the average emissions. |
| `exchange_rate_date_mode` | [`ExchangeRateDateModeEnum`](../../doc/models/exchange-rate-date-mode-enum.md) | Optional | Gets or sets the exchange rate date mode. |
| `exchange_rate_date_deviation` | `int` | Optional | Gets or sets the exchange rate date deviation. |

## Example (as JSON)

```json
{
  "printDebit": "None",
  "printCredit": "None",
  "debitFormType": 228,
  "debitOwnFormType": 136,
  "debitFormularType": 102
}
```

