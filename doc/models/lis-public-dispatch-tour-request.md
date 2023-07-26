
# LIS Public Dispatch Tour Request

A request for a public dispatch tour.

## Structure

`LISPublicDispatchTourRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tour_id` | `int` | Optional | Gets or sets the carrier id. |
| `carrier_id` | `int` | Optional | Gets or sets the carrier id. |
| `lorry_id` | `string` | Optional | Gets or sets the lorry id. |
| `trailer_id` | `string` | Optional | Gets or sets the trailer id. |
| `costs` | [`List of LISPublicCostItem`](../../doc/models/lis-public-cost-item.md) | Optional | Gets or sets the cost. |

## Example (as JSON)

```json
{
  "tourId": 112,
  "carrierId": 44,
  "lorryId": "lorryId4",
  "trailerId": "trailerId6",
  "costs": [
    {
      "value": 252.18,
      "amount": 199.88,
      "currency": "currency6",
      "salesTaxCode": "salesTaxCode2",
      "costPer": "Quantity"
    },
    {
      "value": 252.19,
      "amount": 199.89,
      "currency": "currency7",
      "salesTaxCode": "salesTaxCode3",
      "costPer": "Distance"
    },
    {
      "value": 252.2,
      "amount": 199.9,
      "currency": "currency8",
      "salesTaxCode": "salesTaxCode4",
      "costPer": "LoadingMeter"
    }
  ]
}
```

