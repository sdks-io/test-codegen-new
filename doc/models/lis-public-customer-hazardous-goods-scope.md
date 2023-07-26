
# LIS Public Customer Hazardous Goods Scope

LISCustomerHazardousGoodsScope

## Structure

`LISPublicCustomerHazardousGoodsScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hazardous_goods_blocked` | `bool` | Optional | Gets or sets a value indicating whether [hazardous goods blocked]. |
| `hazardous_goods_classes` | [`List of LISPublicCustomerHazardousGoodsClass`](../../doc/models/lis-public-customer-hazardous-goods-class.md) | Optional | Gets or sets the hazardous goods classes. |

## Example (as JSON)

```json
{
  "hazardousGoodsBlocked": false,
  "hazardousGoodsClasses": [
    {
      "customerHazardousGoodsClassId": 19,
      "customerId": 215,
      "hazardousGoodsClass": "hazardousGoodsClass7",
      "blocked": true,
      "trackChanges": true
    },
    {
      "customerHazardousGoodsClassId": 20,
      "customerId": 216,
      "hazardousGoodsClass": "hazardousGoodsClass6",
      "blocked": false,
      "trackChanges": false
    }
  ]
}
```

