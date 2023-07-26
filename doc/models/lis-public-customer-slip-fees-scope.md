
# LIS Public Customer Slip Fees Scope

The LISCustomerSlipFeesScope data contract.

## Structure

`LISPublicCustomerSlipFeesScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `slip_fees` | [`List of LISPublicCustomerSlipFee`](../../doc/models/lis-public-customer-slip-fee.md) | Optional | Gets or sets CustomerPrints. |

## Example (as JSON)

```json
{
  "slipFees": [
    {
      "customerId": 156,
      "slipFeeId": 58,
      "calculationBase": "Credit",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy2"
    },
    {
      "customerId": 157,
      "slipFeeId": 59,
      "calculationBase": "All",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy3"
    }
  ]
}
```

