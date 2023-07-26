
# LIS Public Route Info

Only the basic route informations.

## Structure

`LISPublicRouteInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distance_cost` | `float` | Optional | Gets or sets the distance cost. |
| `distance_toll_cost` | `float` | Optional | Gets or sets the distance toll cost. |
| `distance_toll_cost_provider` | [`DistanceTollCostProviderEnum`](../../doc/models/distance-toll-cost-provider-enum.md) | Optional | Gets or sets the distance toll cost provider. |
| `currency` | `string` | Optional | The currency like the company setting. |
| `distance` | `float` | Optional | The distance in Meils / Kilometers like the company setting. |
| `distance_toll` | `float` | Optional | The toll distance in Meils / Kilometers like the company setting. |
| `distance_empty` | `float` | Optional | The distance emtpy in Meils / Kilometers like the company setting. |
| `distance_toll_empty` | `float` | Optional | The toll empty distance in Meils / Kilometers like the company setting. |
| `time` | `int` | Optional | The time in minutes. |
| `used_routing_provider` | [`UsedRoutingProviderEnum`](../../doc/models/used-routing-provider-enum.md) | Optional | Gets or sets the used routing provider. |
| `distance_state` | [`DistanceState1Enum`](../../doc/models/distance-state-1-enum.md) | Optional | Gets or sets the state of the distance. |
| `declared_distance` | `float` | Optional | Gets or sets the declared distance. |
| `declared_distance_toll` | `float` | Optional | Gets or sets the declared distance toll. |
| `used_toll_provider` | [`UsedTollProviderEnum`](../../doc/models/used-toll-provider-enum.md) | Optional | Gets or sets the used toll provider. |

## Example (as JSON)

```json
{
  "distanceCost": 121.88,
  "distanceTollCost": 221.9,
  "distanceTollCostProvider": "Nokia",
  "currency": "currency0",
  "distance": 146.7
}
```

