
# LIS Public Customer Customs Scope

The LISCustomerCustomsScope data contract.

## Structure

`LISPublicCustomerCustomsScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `own_customs_number` | `string` | Optional | Gets or sets OwnCustomsNumber. |
| `is_intra_stat_active` | `bool` | Optional | Gets or sets a value indicating whether this instance is intra stat active. |
| `intra_stat_from` | `datetime` | Optional | Gets or sets the intra stat from. |
| `intra_stat_till` | `datetime` | Optional | Gets or sets the intra stat till. |
| `tax_number` | `string` | Optional | Gets or sets the tax number. |
| `distinction_no` | `int` | Optional | Gets or sets the distinction no. |
| `business_type` | `int` | Optional | Gets or sets the type of the business. |
| `process_type` | `string` | Optional | Gets or sets the type of the process. |
| `process_type_national` | `string` | Optional | Gets or sets the process type numeric. |
| `print_export_documents` | `bool` | Optional | Gets or sets a value indicating whether [print export documents]. |

## Example (as JSON)

```json
{
  "ownCustomsNumber": "ownCustomsNumber8",
  "isIntraStatActive": false,
  "intraStatFrom": "2016-03-13T12:52:32.123Z",
  "intraStatTill": "2016-03-13T12:52:32.123Z",
  "taxNumber": "taxNumber2"
}
```

