
# LIS Public Locality Routing Info

Partial class with the correct namespace

## Structure

`LISPublicLocalityRoutingInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_middle` | `bool` | Optional | Gets or sets a value indicating whether this instance is middle. |
| `bsl` | `string` | Optional | Gets or sets the BSL. |
| `degt` | `string` | Optional | Gets or sets the DEGT. |
| `community_code` | `int` | Optional | Gets or sets the community code. |
| `area` | `int` | Optional | Gets or sets the area. |
| `method` | [`MethodEnum`](../../doc/models/method-enum.md) | Optional | Gets or sets the method. |
| `coordinate` | [`LISPublicCoordinate`](../../doc/models/lis-public-coordinate.md) | Optional | This class represents the public coordinate object. |
| `area_node_1` | `int` | Optional | Gets or sets the node1. |
| `area_node_2` | `int` | Optional | Gets or sets the node2. |
| `area_node_3` | `int` | Optional | Gets or sets the node3. |
| `area_node_4` | `int` | Optional | Gets or sets the node4. |
| `area_node_5` | `int` | Optional | Gets or sets the node5. |
| `area_node_6` | `int` | Optional | Gets or sets the node6. |
| `area_node_7` | `int` | Optional | Gets or sets the node7. |
| `area_node_8` | `int` | Optional | Gets or sets the node8. |
| `area_node_9` | `int` | Optional | Gets or sets the node9. |
| `area_node_10` | `int` | Optional | Gets or sets the node10. |
| `displacement_km_1` | `int` | Optional | Gets or sets the displacement KM1. |
| `displacement_km_2` | `int` | Optional | Gets or sets the displacement KM2. |
| `displacement_km_3` | `int` | Optional | Gets or sets the displacement KM3. |
| `displacement_km_4` | `int` | Optional | Gets or sets the displacement KM4. |
| `displacement_km_5` | `int` | Optional | Gets or sets the displacement KM5. |
| `displacement_km_6` | `int` | Optional | Gets or sets the displacement KM6. |
| `displacement_km_7` | `int` | Optional | Gets or sets the displacement KM7. |
| `displacement_km_8` | `int` | Optional | Gets or sets the displacement KM8. |
| `displacement_km_9` | `int` | Optional | Gets or sets the displacement KM9. |
| `displacement_km_10` | `int` | Optional | Gets or sets the displacement KM10. |
| `source` | [`SourceEnum`](../../doc/models/source-enum.md) | Optional | Is it the middle of the locality? |
| `ews_node` | `int` | Optional | - |
| `ews_old_node` | `int` | Optional | - |
| `astag_node` | `int` | Optional | - |
| `astag_old_node` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "isMiddle": false,
  "bsl": "bsl0",
  "degt": "degt6",
  "communityCode": 54,
  "area": 106
}
```

