
# LIS Public Customer Calculation Scope

The LISCustomerCalculationScope data contract.

## Structure

`LISPublicCustomerCalculationScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `blocking_weight` | `float` | Optional | Gets or sets BlockingWeight. |
| `blocking_weight_base` | [`BlockingWeightBaseEnum`](../../doc/models/blocking-weight-base-enum.md) | Optional | Gets or sets BlockingWeightBase. |
| `automatic_toll_calculation` | [`AutomaticTollCalculationEnum`](../../doc/models/automatic-toll-calculation-enum.md) | Optional | Gets or sets AutomaticTollCalculation. |
| `toll_method` | [`TollMethodEnum`](../../doc/models/toll-method-enum.md) | Optional | Gets or sets TollMethod. |
| `distance_calculation_method_order_1` | [`DistanceCalculationMethodOrder1Enum`](../../doc/models/distance-calculation-method-order-1-enum.md) | Optional | Gets or sets the distance calculation method order1. |
| `distance_calculation_method_order_2` | [`DistanceCalculationMethodOrder2Enum`](../../doc/models/distance-calculation-method-order-2-enum.md) | Optional | Gets or sets the distance calculation method order2. |
| `distance_calculation_method_order_3` | [`DistanceCalculationMethodOrder3Enum`](../../doc/models/distance-calculation-method-order-3-enum.md) | Optional | Gets or sets the distance calculation method order3. |
| `distance_calculation_method_order_4` | [`DistanceCalculationMethodOrder4Enum`](../../doc/models/distance-calculation-method-order-4-enum.md) | Optional | Gets or sets the distance calculation method order4. |
| `collection_point_id` | `int` | Optional | Gets or sets CollectionPoint. |
| `collection_point_country_code` | `string` | Optional | Gets or sets the collection point country code. |
| `consider_bulky_goods` | `bool` | Optional | Gets or sets ConsiderBulkyGoods. |
| `is_invoicing_blocked_for_new_orders` | `bool` | Optional | Gets or sets IsInvoicingBlockedForNewOrders. |

## Example (as JSON)

```json
{
  "blockingWeight": 135.98,
  "blockingWeightBase": "None",
  "automaticTollCalculation": "Deactivated",
  "tollMethod": "DistanceRoadWorkOld",
  "distanceCalculationMethodOrder1": "PTVMapServer"
}
```

