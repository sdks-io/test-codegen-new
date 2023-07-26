
# LIS Public Customer Commission Calculation

The ILISCustomerCommissionCalculationEntity data contract.

## Structure

`LISPublicCustomerCommissionCalculation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_commission_calculation_id` | `int` | Optional | Gets or sets the customer commission calculation identifier. |
| `customer_id` | `int` | Optional | Gets or sets the customer identifier. |
| `transport_type_id` | `string` | Optional | Gets or sets the transport type identifier. |
| `contact_person_id` | `int` | Optional | Gets or sets the contact person identifier. |
| `fee_group_id` | `int` | Optional | Gets or sets the fee group identifier. |
| `valid_from` | `datetime` | Optional | Gets or sets the valid from. |
| `commission_percentage` | `float` | Optional | Gets or sets the commission percentage. |

## Example (as JSON)

```json
{
  "customerCommissionCalculationId": 22,
  "customerId": 114,
  "transportTypeId": "transportTypeId2",
  "contactPersonId": 78,
  "feeGroupId": 200
}
```

