
# LIS Public Customer Accounting Scope

The LISCustomerAccountingScope data contract.

## Structure

`LISPublicCustomerAccountingScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_table_id` | `int` | Optional | Gets or sets AccountTableId. |
| `cost_unit_id` | `int` | Optional | Gets or sets PayerId. |
| `cost_center` | `int` | Optional | Gets or sets CostCenter. |
| `final_consumer` | `bool` | Optional | Gets or sets FinalConsumer. |
| `tax_id_number` | `string` | Optional | Gets or sets TaxIdNumber. |
| `tax_number` | `string` | Optional | Gets or sets TaxNumber. |
| `debitor_account` | `string` | Optional | Gets or sets DebitorAccount. |
| `creditor_account` | `string` | Optional | Gets or sets CreditorAccount. |
| `debit_booking` | [`DebitBookingEnum`](../../doc/models/debit-booking-enum.md) | Optional | Gets or sets DebitBooking. |
| `credit_booking` | [`CreditBookingEnum`](../../doc/models/credit-booking-enum.md) | Optional | Gets or sets CreditBooking. |
| `terms_of_payment` | `int` | Optional | Gets or sets TermsOfPayment. |
| `is_simple_term_of_payment` | `bool` | Optional | Gets or sets a value indicating whether this instance is simple term of payment. |
| `search_procedure` | [`SearchProcedureEnum`](../../doc/models/search-procedure-enum.md) | Optional | Gets or sets SearchProcedure. |
| `sales_tax_number` | `string` | Optional | Gets or sets SalesTaxNumber. |
| `no_dunning` | `bool` | Optional | Gets or sets NoDunning. |
| `bank_code` | `string` | Optional | Gets or sets BankCode. |
| `bank_name` | `string` | Optional | Gets or sets the name of the bank. |
| `bank_account_number` | `string` | Optional | Gets or sets BankAccountNumber. |
| `international_bank_account_number` | `string` | Optional | Gets or sets InternationalBankAccountNumber. |
| `swift_code` | `string` | Optional | Gets or sets SwiftCode. |
| `retain_amount` | `float` | Optional | Gets or sets the retain amount. |
| `limit_debit` | `int` | Optional | Gets or sets the credit limit. |
| `invoice_sum_debit` | `int` | Optional | Gets or sets the invoice sum. |
| `voucher_sum_debit` | `int` | Optional | Gets or sets the voucher sum. |
| `limit_credit` | `int` | Optional | Gets or sets the credit limit. |
| `invoice_sum_credit` | `int` | Optional | Gets or sets the invoice sum. |
| `voucher_sum_credit` | `int` | Optional | Gets or sets the voucher sum. |
| `open_items_factor_debit` | `float` | Optional | Gets or sets the open items factor debit. |
| `open_items_factor_credit` | `float` | Optional | Gets or sets the open items factor credit. |
| `creditor_sequence_account_no` | `int` | Optional | Gets or sets the creditor sequence account no. |
| `debitor_sequence_account_no` | `int` | Optional | Gets or sets the debitor sequence account no. |
| `bank_city` | `string` | Optional | Gets or sets the bank city. |
| `bank_country_code` | `string` | Optional | Gets or sets the bank country code. |
| `minimum_wage_certificate_valid_till` | `datetime` | Optional | Gets or sets the debitor sequence account no. |
| `secu_sped_whitelist_id` | `int` | Optional | Gets or sets the secu sped whitelist identifier. |
| `is_secu_sped_whitelisted` | `bool` | Optional | Gets or sets a value indicating whether this instance is secu sped whitelisted. |
| `debitor_account_numbers` | [`List of LISCustomerAccountNumber`](../../doc/models/lis-customer-account-number.md) | Optional | Gets or sets the debitor account numbers. |
| `creditor_account_numbers` | [`List of LISCustomerAccountNumber`](../../doc/models/lis-customer-account-number.md) | Optional | Gets or sets the creditor account numbers. |
| `rating` | `string` | Optional | Gets or sets the rating. |
| `rating_limit` | `string` | Optional | Gets or sets the rating limit. |

## Example (as JSON)

```json
{
  "accountTableId": 220,
  "costUnitId": 16,
  "costCenter": 96,
  "finalConsumer": false,
  "taxIdNumber": "taxIdNumber6"
}
```

