
# LIS Public Article

## Structure

`LISPublicArticle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `costs` | [`List of LISPublicArticleCost`](../../doc/models/lis-public-article-cost.md) | Optional | - |
| `customer_id` | `int` | Optional | - |
| `article_id` | `string` | Optional | - |
| `changed_on` | `datetime` | Optional | - |
| `changed_by` | `string` | Optional | - |
| `description_1` | `string` | Optional | - |
| `description_2` | `string` | Optional | - |
| `article_short` | `string` | Optional | - |
| `unit` | `string` | Optional | - |
| `origin_locality_id` | `string` | Optional | - |
| `ean` | `string` | Optional | - |
| `account_table_id` | `int` | Optional | - |
| `weight` | `float` | Optional | - |
| `group` | `string` | Optional | - |
| `dangerous_good_class` | `string` | Optional | - |
| `dangerous_goods` | `bool` | Optional | - |
| `dangerous_good_un` | `int` | Optional | - |
| `dangerous_good_number` | `string` | Optional | - |
| `reefer_cargo` | `bool` | Optional | - |
| `billing_rate` | `string` | Optional | - |
| `ean_minor` | `string` | Optional | - |
| `ccg` | `int` | Optional | - |
| `customs_tariff` | `string` | Optional | - |
| `stack_mark` | `int` | Optional | - |
| `einh_kl` | `string` | Optional | - |
| `height` | `int` | Optional | - |
| `length` | `int` | Optional | - |
| `width` | `int` | Optional | - |
| `supplier_article_no` | `string` | Optional | - |
| `next_ean` | `string` | Optional | - |
| `following_ean_count` | `int` | Optional | - |
| `pallet_unit` | `string` | Optional | - |
| `package_quantity` | `int` | Optional | - |
| `layer_quantity` | `int` | Optional | - |
| `valid_till` | `datetime` | Optional | - |
| `pallet_loading_height` | `int` | Optional | - |
| `article_group` | `string` | Optional | - |
| `stock_lockdown` | `string` | Optional | - |
| `stock_lockdown_characteristic` | `string` | Optional | - |
| `o_charge` | `bool` | Optional | - |
| `quantity_unit` | `string` | Optional | - |
| `package_id` | `string` | Optional | - |
| `quantity_per_package` | `int` | Optional | - |
| `packages_per_pallet` | `int` | Optional | - |
| `stockt_minimum_quantity` | `int` | Optional | - |
| `quantity_value` | `float` | Optional | - |
| `quantity_weight` | `float` | Optional | - |
| `package_weight` | `float` | Optional | - |
| `manufacturer` | `string` | Optional | - |
| `package_label_quantity` | `int` | Optional | - |
| `minimum_amount_in_package_units` | `int` | Optional | - |
| `inventory_date` | `datetime` | Optional | - |
| `inventory_stocks_package` | `int` | Optional | - |
| `cost_center_id` | `int` | Optional | - |
| `statistical_commodity_code` | `string` | Optional | - |
| `purchase_price` | `float` | Optional | - |
| `sales_price` | `float` | Optional | - |
| `cost_estimation_factor` | `float` | Optional | - |
| `bel_txt` | `string` | Optional | - |
| `ent_txt` | `string` | Optional | - |
| `cost_unit_id` | `int` | Optional | - |
| `kemmler_number` | `string` | Optional | - |
| `pallets_minor_stock_according` | `int` | Optional | - |
| `package_minor_stock_according` | `int` | Optional | - |
| `inventory_stocks_pallet` | `int` | Optional | - |
| `inventory_stocks_me` | `int` | Optional | - |
| `occupied_foot_print_quantity` | `float` | Optional | - |
| `footprint_unit` | `string` | Optional | - |
| `major_article_quantity` | `int` | Optional | - |
| `w_kz_wert` | `float` | Optional | - |
| `w_kz_tage` | `int` | Optional | - |
| `description_3` | `string` | Optional | - |
| `waste_code` | `string` | Optional | - |
| `goods_class` | `string` | Optional | - |
| `goods_group` | `string` | Optional | - |
| `disposal_observation_company` | [`DisposalObservationCompanyEnum`](../../doc/models/disposal-observation-company-enum.md) | Optional | - |
| `un_sequence_id` | `int` | Optional | - |
| `sensor_threshold_min_temp_1` | `float` | Optional | - |
| `sensor_threshold_max_temp_1` | `float` | Optional | - |
| `sensor_threshold_min_temp_2` | `float` | Optional | - |
| `sensor_threshold_max_temp_2` | `float` | Optional | - |
| `sensor_threshold_min_temp_3` | `float` | Optional | - |
| `sensor_threshold_max_temp_3` | `float` | Optional | - |
| `sensor_threshold_min_temp_4` | `float` | Optional | - |
| `sensor_threshold_max_temp_4` | `float` | Optional | - |
| `full_height` | `float` | Optional | - |
| `package` | [`LISPublicUnit`](../../doc/models/lis-public-unit.md) | Optional | Data contract for a unit. |
| `ecological_menace` | [`EcologicalMenaceEnum`](../../doc/models/ecological-menace-enum.md) | Optional | - |
| `translation_label_text` | [`LISPublicLanguageItemContainer`](../../doc/models/lis-public-language-item-container.md) | Optional | - |
| `translation_second_label_text` | [`LISPublicLanguageItemContainer`](../../doc/models/lis-public-language-item-container.md) | Optional | - |
| `wms_article` | [`LISPublicWMSArticle`](../../doc/models/lis-public-wms-article.md) | Optional | The LISPublicWMSArticle data contract. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "costs": [
    {
      "id": 178,
      "customerId": 208,
      "articleNo": "articleNo0",
      "validFrom": "2016-03-13T12:52:32.123Z",
      "purchasePrice": 233.28
    },
    {
      "id": 179,
      "customerId": 209,
      "articleNo": "articleNo9",
      "validFrom": "2016-03-13T12:52:32.123Z",
      "purchasePrice": 233.27
    },
    {
      "id": 180,
      "customerId": 210,
      "articleNo": "articleNo8",
      "validFrom": "2016-03-13T12:52:32.123Z",
      "purchasePrice": 233.26
    }
  ],
  "customerId": 114,
  "articleId": "articleId4",
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8"
}
```

