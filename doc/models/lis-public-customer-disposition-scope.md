
# LIS Public Customer Disposition Scope

The LISCustomerDispositionScope data contract.

## Structure

`LISPublicCustomerDispositionScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `departure_type` | [`DepartureTypeEnum`](../../doc/models/departure-type-enum.md) | Optional | Gets or sets DepartureType. |
| `warehouse` | `int` | Optional | Gets or sets the warehouse. |
| `additional_usage` | [`AdditionalUsageEnum`](../../doc/models/additional-usage-enum.md) | Optional | Gets or sets AdditionalUsage. |
| `insurance_international_valid_till` | `datetime` | Optional | Gets or sets InsuranceInternationalValidTill. |
| `insurance_international_amount` | `float` | Optional | Gets or sets InsuranceInternationalAmount. |
| `insurance_international_currency` | `string` | Optional | Gets or sets InsuranceInternationalCurrency. |
| `insurance_national_valid_till` | `datetime` | Optional | Gets or sets InsuranceNationalValidTill. |
| `insurance_national_amount` | `float` | Optional | Gets or sets InsuranceNationalAmount. |
| `insurance_national_currency` | `string` | Optional | Gets or sets InsuranceNationalCurrency. |
| `insurance_international_additional_valid_till` | `datetime` | Optional | Gets or sets InsuranceInternationalAdditionalValidTill. |
| `insurance_international_additional_amount` | `float` | Optional | Gets or sets InsuranceInternationalAdditionalAmount. |
| `insurance_international_additional_currency` | `string` | Optional | Gets or sets InsuranceInternationalAdditionalCurrency. |
| `european_license_valid_till` | `datetime` | Optional | Gets or sets EuropeanLicenseValidTill. |
| `cabotage_allowed_from` | `datetime` | Optional | Gets or sets CabotageAllowedFrom. |
| `equipment_code` | `string` | Optional | Gets or sets EquipmentCode. |
| `customer_protection` | `bool` | Optional | Gets or sets a value indicating whether [customer protection]. |

## Example (as JSON)

```json
{
  "departureType": "Retrieval",
  "warehouse": 110,
  "additionalUsage": "Normal",
  "insuranceInternationalValidTill": "2016-03-13T12:52:32.123Z",
  "insuranceInternationalAmount": 134.12
}
```

