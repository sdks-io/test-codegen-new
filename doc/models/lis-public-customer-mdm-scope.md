
# LIS Public Customer MDM Scope

The LISCustomerMDMScope data contract.

## Structure

`LISPublicCustomerMDMScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `matchcode` | `string` | Optional | Gets or sets Matchcode. |
| `name_1` | `string` | Optional | Gets or sets Name1. |
| `name_2` | `string` | Optional | Gets or sets Name2. |
| `name_3` | `string` | Optional | Gets or sets Name3. |
| `street` | `string` | Optional | Gets or sets Street. |
| `country_code` | `string` | Optional | Gets or sets CountryCode. |
| `zip` | `string` | Optional | Gets or sets Zip. |
| `city` | `string` | Optional | Gets or sets City. |
| `city_district` | `string` | Optional | Gets or sets the city district. |
| `post_office_box` | `string` | Optional | Gets or sets PostOfficeBox. |
| `post_office_zip_code` | `string` | Optional | Gets or sets PostOfficeZipCode. |
| `tax_id_number` | `string` | Optional | Gets or sets TaxIdNumber. |
| `tax_number` | `string` | Optional | Gets or sets TaxNumber. |
| `search_procedure` | [`SearchProcedureEnum`](../../doc/models/search-procedure-enum.md) | Optional | Gets or sets SearchProcedure. |
| `limit_debit` | `int` | Optional | Gets or sets LimitDebit. |
| `limit_credit` | `int` | Optional | Gets or sets LimitCredit. |
| `debit_print_currency` | `string` | Optional | Gets or sets DebitPrintCurrency. |
| `credit_print_currency` | `string` | Optional | Gets or sets CreditPrintCurrency. |
| `terms_of_payment_debitor` | `int` | Optional | Gets or sets TermsOfPaymentDebitor. |
| `terms_of_payment_creditor` | `int` | Optional | Gets or sets TermsOfPaymentCreditor. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "matchcode": "matchcode2",
  "name1": "name10",
  "name2": "name24",
  "name3": "name34"
}
```

