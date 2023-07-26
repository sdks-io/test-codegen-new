
# LIS Public Customer Slip Fee

Represents an entity class. This class depends on the database table #*KunBelG

## Structure

`LISPublicCustomerSlipFee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets the CustomerId property. This property depends on the database field KundenNr. |
| `slip_fee_id` | `int` | Optional | Gets or sets the SlipFeeId property. This property depends on the database field BelGebNr. |
| `calculation_base` | [`CalculationBaseEnum`](../../doc/models/calculation-base-enum.md) | Optional | Gets or sets the CalculationBase property. This property depends on the database field GueltigF. |
| `changed_on` | `datetime` | Optional | Gets or sets the ChangedOn property. This property depends on the database field AendDat. |
| `changed_by` | `string` | Optional | Gets or sets the ChangedBy property. This property depends on the database field AendUs. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "slipFeeId": 44,
  "calculationBase": "NotSet",
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8"
}
```

