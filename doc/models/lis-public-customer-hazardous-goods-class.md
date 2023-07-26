
# LIS Public Customer Hazardous Goods Class

The LISCustomerHazardousGoodsClass data contract.

## Structure

`LISPublicCustomerHazardousGoodsClass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_hazardous_goods_class_id` | `int` | Optional | Gets or sets CustomerHazardousGoodsClassId. |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `hazardous_goods_class` | `string` | Optional | Gets or sets HazardousGoodsClass. |
| `blocked` | `bool` | Optional | Gets or sets Blocked. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |

## Example (as JSON)

```json
{
  "customerHazardousGoodsClassId": 202,
  "customerId": 114,
  "hazardousGoodsClass": "hazardousGoodsClass4",
  "blocked": false,
  "trackChanges": false
}
```

