
# LIS Public Order Aggregates

The LIS Order aggregates.

## Structure

`LISPublicOrderAggregates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `weight` | `float` | Optional | Gets or sets the weight. |
| `chargeable_weight` | `float` | Optional | Gets or sets the chargeable weight. |
| `cubic_decimeter` | `float` | Optional | Gets or sets the cubic decimeter. |
| `loading_meter` | `float` | Optional | Gets or sets the loading meter. |
| `square_meter` | `float` | Optional | Gets or sets the square meter. |
| `storage_places` | `float` | Optional | Gets or sets the storage places. |
| `given_weight` | `float` | Optional | Gets or sets the given weight. |
| `palletts` | `float` | Optional | Gets or sets the palletts. |
| `packages` | `float` | Optional | Gets or sets the packages. |
| `pieces` | `float` | Optional | Gets or sets the pieces. |
| `shipping_units` | `float` | Optional | Gets or sets the shipping units. |
| `dangerous_goods` | `bool` | Optional | Gets or sets a value indicating whether [dangerous goods]. |
| `reefer_cargo` | `bool` | Optional | Gets or sets a value indicating whether [reefer cargo]. |
| `declared_value` | `float` | Optional | Gets or sets the declared value. |
| `calculated_amount` | `float` | Optional | Gets or sets the calculated amount. |
| `orders` | `int` | Optional | Gets or sets the orders. |
| `given_packages` | `float` | Optional | Gets or sets the given packages. |
| `ecological_menace` | [`EcologicalMenace1Enum`](../../doc/models/ecological-menace-1-enum.md) | Optional | Gets or sets the ecological menace. |
| `tunnel_category` | [`TunnelCategoryEnum`](../../doc/models/tunnel-category-enum.md) | Optional | Gets or sets the tunnel category. |
| `is_explosiv` | `bool` | Optional | Gets or sets a value indicating whether this instance is explosiv. |

## Example (as JSON)

```json
{
  "weight": 192.04,
  "chargeableWeight": 138.94,
  "cubicDecimeter": 36.7,
  "loadingMeter": 50.52,
  "squareMeter": 114.94
}
```

