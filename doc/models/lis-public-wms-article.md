
# LIS Public WMS Article

The LISPublicWMSArticle data contract.

## Structure

`LISPublicWMSArticle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `article_units` | [`List of LISPublicWMSArticleUnit`](../../doc/models/lis-public-wms-article-unit.md) | Optional | - |
| `article_eans` | [`List of LISPublicWMSArticleEan`](../../doc/models/lis-public-wms-article-ean.md) | Optional | - |
| `article_id` | `int` | Optional | Gets or sets ArticleId. |
| `company_id` | `int` | Optional | Gets or sets CompanyId. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `created_by` | `string` | Optional | Gets or sets ChangedBy. |
| `created_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `article_number` | `string` | Optional | Gets or sets ArticleNumber. |
| `customer_id` | `int` | Optional | Gets or sets Client. |
| `name_1` | `string` | Optional | Gets or sets Name1. |
| `name_2` | `string` | Optional | Gets or sets Name2. |
| `name_3` | `string` | Optional | Gets or sets Name3. |
| `name_4` | `string` | Optional | Gets or sets Name4. |
| `article_short` | `string` | Optional | Gets or sets ArticleShort. |
| `matchcode` | `string` | Optional | Gets or sets Matchcode. |
| `product_group` | `string` | Optional | Gets or sets ProductGroup. |
| `always_batched` | `bool` | Optional | Gets or sets AlwaysBatched. |
| `serial_number_required` | `bool` | Optional | Gets or sets SerialNumberRequiered. |
| `subject_to_ed` | `bool` | Optional | Gets or sets SubjectToMHD. |
| `bom_item` | `bool` | Optional | Gets or sets BOMItem. |
| `article_parts_id` | `int` | Optional | Gets or sets ArticlePartsId. |
| `not_commissionable` | `bool` | Optional | Gets or sets NotCommissionable. |
| `storage_unit_id` | `int` | Optional | Gets or sets StorageUnitId. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "articleUnits": [
    {
      "articleId": 23,
      "articleUnitId": 127,
      "companyId": 125,
      "changedBy": "changedBy5",
      "changedOn": "2016-03-13T12:52:32.123Z"
    },
    {
      "articleId": 24,
      "articleUnitId": 128,
      "companyId": 124,
      "changedBy": "changedBy6",
      "changedOn": "2016-03-13T12:52:32.123Z"
    }
  ],
  "articleEans": [
    {
      "articleEanId": 9,
      "companyId": 37,
      "changedBy": "changedBy9",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "createdBy": "createdBy1"
    },
    {
      "articleEanId": 10,
      "companyId": 36,
      "changedBy": "changedBy0",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "createdBy": "createdBy0"
    },
    {
      "articleEanId": 11,
      "companyId": 35,
      "changedBy": "changedBy1",
      "changedOn": "2016-03-13T12:52:32.123Z",
      "createdBy": "createdBy9"
    }
  ],
  "articleId": 80,
  "companyId": 68,
  "changedBy": "changedBy8"
}
```

