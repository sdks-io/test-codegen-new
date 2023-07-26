
# LIS Public Customer Outdated Fields Scope

The LISCustomerOutdatedFieldsScope data contract.

## Structure

`LISPublicCustomerOutdatedFieldsScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `commercial_carrier` | `bool` | Optional | Gets or sets CommercialCarrier. |
| `credit_freight_payer_optimization_code` | [`CreditFreightPayerOptimizationCodeEnum`](../../doc/models/credit-freight-payer-optimization-code-enum.md) | Optional | Gets or sets CreditFreightPayerOptimizationCode. |
| `debit_freight_payer_optimization_code` | [`DebitFreightPayerOptimizationCodeEnum`](../../doc/models/debit-freight-payer-optimization-code-enum.md) | Optional | Gets or sets DebitFreightPayerOptimizationCode. |
| `debit_show_total_amount_in_euro` | `bool` | Optional | Gets or sets DebitShowTotalAmountInEuro. |
| `credit_show_total_amount_in_euro` | `bool` | Optional | Gets or sets CreditShowTotalAmountInEuro. |
| `debit_print_fly_leaf` | `bool` | Optional | Gets or sets DebitPrintFlyLeaf. |
| `credit_print_fly_leaf` | `bool` | Optional | Gets or sets CreditPrintFlyLeaf. |
| `separate_local_and_long_distance_traffic` | `bool` | Optional | Gets or sets SeparateLocalAndLongDistanceTraffic. |
| `incoming_invoice_activated_country_codes` | `List of string` | Optional | Gets or sets IncomingInvoiceActivatedCountryCodes. |
| `net_target_days` | `int` | Optional | Gets or sets NetTargetDays. |
| `cashback_target_days` | `int` | Optional | Gets or sets CashbackTargetDays. |
| `cashback_percentage` | `float` | Optional | Gets or sets CashbackPercentage. |
| `company_group` | `int` | Optional | Gets or sets CompanyGroup. |
| `company` | `int` | Optional | Gets or sets Company. |
| `division` | `int` | Optional | Gets or sets Division. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |
| `gft_tariff_valid_date` | `datetime` | Optional | Gets or sets the GFT tariff valid date. |
| `kds_tariff_valid_date` | `datetime` | Optional | Gets or sets the KDS tariff valid date. |
| `in_house_freight_tariff_valid_date` | `datetime` | Optional | Gets or sets the in house freight tariff valid date. |
| `foreign_object_calculation_base` | [`ForeignObjectCalculationBaseEnum`](../../doc/models/foreign-object-calculation-base-enum.md) | Optional | Gets or sets the foreign calculation base. |

## Example (as JSON)

```json
{
  "commercialCarrier": false,
  "creditFreightPayerOptimizationCode": "SerialWithoutFeed",
  "debitFreightPayerOptimizationCode": "TemplateSerial",
  "debitShowTotalAmountInEuro": false,
  "creditShowTotalAmountInEuro": false
}
```

