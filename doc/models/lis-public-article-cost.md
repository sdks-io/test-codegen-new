
# LIS Public Article Cost

The LISPublicArticleCost class

## Structure

`LISPublicArticleCost`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Gets or sets Id. |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `article_no` | `string` | Optional | Gets or sets ArticleNo. |
| `valid_from` | `datetime` | Optional | Gets or sets ValidFrom. |
| `purchase_price` | `float` | Optional | Gets or sets PurchasePrice. |
| `sales_price` | `float` | Optional | Gets or sets SalesPrice. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "id": 112,
  "customerId": 114,
  "articleNo": "articleNo6",
  "validFrom": "2016-03-13T12:52:32.123Z",
  "purchasePrice": 233.94
}
```

