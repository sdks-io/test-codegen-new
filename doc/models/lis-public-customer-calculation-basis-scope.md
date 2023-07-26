
# LIS Public Customer Calculation Basis Scope

The LISCustomerCalculationBasisScope data contract.

## Structure

`LISPublicCustomerCalculationBasisScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference_number_mask` | `string` | Optional | Gets or sets ReferenceNumberMask. |
| `reference_number_mask_counter` | `int` | Optional | Gets or sets ReferenceNumberMaskCounter. |
| `sscc_base_no` | `string` | Optional | Gets or sets the SSCC base no. |
| `producer_no` | `string` | Optional | Gets or sets the producer no. |
| `disposal_company_no` | `string` | Optional | Gets or sets the disposal company no. |
| `disposal_company_transport_no` | `string` | Optional | Gets or sets the disposal company transport no. |
| `disposal_transport_permission` | `string` | Optional | Gets or sets the disposal transport permission. |
| `disposal_transport_permission_valid_till` | `datetime` | Optional | Gets or sets the disposal transport permission valid till. |
| `commission_calculations` | [`List of LISPublicCustomerCommissionCalculation`](../../doc/models/lis-public-customer-commission-calculation.md) | Optional | Gets or sets the commission calculations. |
| `join_split_setting_id` | `int` | Optional | Gets or sets the join split setting identifier. |
| `uic_country_code` | `int` | Optional | Gets or sets UICCountryCode. |
| `uic_no` | `int` | Optional | Gets or sets UICNo. |
| `uirr_no` | `int` | Optional | Gets or sets UIRRNo. |
| `is_protected` | `bool` | Optional | Gets or sets the is protected. |

## Example (as JSON)

```json
{
  "referenceNumberMask": "referenceNumberMask6",
  "referenceNumberMaskCounter": 234,
  "ssccBaseNo": "ssccBaseNo8",
  "producerNo": "producerNo0",
  "disposalCompanyNo": "disposalCompanyNo0"
}
```

