
# LIS Public WMS Article Unit

The LISArticleUnit data contract.

## Structure

`LISPublicWMSArticleUnit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `article_id` | `int` | Optional | Gets or sets ArticleId. |
| `article_unit_id` | `int` | Optional | Gets or sets ArticleUnitId. |
| `company_id` | `int` | Optional | Gets or sets CompanyId. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `created_by` | `string` | Optional | Gets or sets ChangedBy. |
| `created_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `base_factor` | `float` | Optional | Gets or sets BaseFactor. |
| `iso_unit` | `string` | Optional | Gets or sets IsoUnit. |
| `unit` | `string` | Optional | Gets or sets Unit. |
| `bin_type_id` | `int` | Optional | Gets or sets BinTypeId. |
| `gross_weight` | `float` | Optional | Gets or sets Grossweight. |
| `net_weight` | `float` | Optional | Gets or sets Netweight. |
| `length` | `float` | Optional | Gets or sets Length. |
| `width` | `float` | Optional | Gets or sets Width. |
| `height` | `float` | Optional | Gets or sets Height. |
| `unit_type` | [`UnitTypeEnum`](../../doc/models/unit-type-enum.md) | Optional | Gets or sets UnitType. |

## Example (as JSON)

```json
{
  "articleId": 80,
  "articleUnitId": 184,
  "companyId": 68,
  "changedBy": "changedBy8",
  "changedOn": "2016-03-13T12:52:32.123Z"
}
```

