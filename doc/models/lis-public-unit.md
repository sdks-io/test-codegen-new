
# LIS Public Unit

Data contract for a unit.

## Structure

`LISPublicUnit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit_id` | `string` | Optional | Gets or sets the unit id. |
| `desc_sing` | `string` | Optional | Gets or sets the desc sing. |
| `desc_plural` | `string` | Optional | Gets or sets the desc plural. |
| `description` | `string` | Optional | Gets or sets the description. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `self_weight` | `float` | Optional | Gets or sets the self weight. |
| `load_dev_booking` | `bool` | Optional | Gets or sets the load dev booking. |
| `load_dev_reference` | `string` | Optional | Gets or sets the load dev reference. |
| `load_dev_conversion_factor` | `float` | Optional | Gets or sets the load dev conversion factor. |
| `load_dev_base_price` | `float` | Optional | Gets or sets the load dev base price. |
| `load_dev_sales_price` | `float` | Optional | Gets or sets the load dev sales price. |
| `load_dev_print_accompanying_letter` | `bool` | Optional | Gets or sets the load dev print accompanying letter. |
| `exchange_price` | `float` | Optional | Gets or sets the exchange price. |
| `length` | `float` | Optional | Gets or sets the length. |
| `width` | `float` | Optional | Gets or sets the width. |
| `height` | `float` | Optional | Gets or sets the height. |
| `load_dev_sort` | `int` | Optional | Gets or sets the load dev sort. |
| `load_dev_customer_id` | `int` | Optional | Gets or sets the load dev customer id. |
| `load_dev_debiting_account` | [`LoadDevDebitingAccountEnum`](../../doc/models/load-dev-debiting-account-enum.md) | Optional | Gets or sets the load dev debiting account. |
| `square_meter_per_loading_meter` | `float` | Optional | Gets or sets the square meter per loading meter. |
| `heavy_cargo_factor_1` | `float` | Optional | Gets or sets the heavy cargo factor1. |
| `heavy_cargo_factor_starts_on_1` | `datetime` | Optional | Gets or sets the heavy cargo factor starts on1. |
| `heavy_cargo_factor_2` | `float` | Optional | Gets or sets the heavy cargo factor2. |
| `heavy_cargo_factor_starts_on_2` | `datetime` | Optional | Gets or sets the heavy cargo factor starts on2. |
| `load_dev_crediting_account` | [`LoadDevCreditingAccountEnum`](../../doc/models/load-dev-crediting-account-enum.md) | Optional | Gets or sets the load dev crediting account. |
| `full_height` | `float` | Optional | Gets or sets the full height. |
| `iso_code` | `string` | Optional | Gets or sets the ISO code. |
| `tare_weight` | `float` | Optional | Gets or sets the tare weight. |
| `stackable` | `bool` | Optional | Gets or sets the stackable. |
| `load_dev_fortras_id` | [`LoadDevFortrasIdEnum`](../../doc/models/load-dev-fortras-id-enum.md) | Optional | Gets or sets the load dev fortras id. |
| `adr_package_type` | `int` | Optional | Gets or sets the type of the ADR package. |
| `adr_description` | `string` | Optional | Gets or sets the ADR description. |
| `filling_degree` | `float` | Optional | Gets or sets the filling degree. |
| `container_lease_price` | `float` | Optional | Gets or sets ContainerLeasePrice. |
| `container_description` | `string` | Optional | Gets or sets ContainerDescription. |
| `desc_sing_container` | [`LISPublicLanguageItemContainer`](../../doc/models/lis-public-language-item-container.md) | Optional | - |
| `desc_plural_container` | [`LISPublicLanguageItemContainer`](../../doc/models/lis-public-language-item-container.md) | Optional | - |
| `description_container` | [`LISPublicLanguageItemContainer`](../../doc/models/lis-public-language-item-container.md) | Optional | - |
| `at_scanner` | `bool` | Optional | Gets or sets a value indicating whether [at scanner]. |
| `hotkey` | [`HotkeyEnum`](../../doc/models/hotkey-enum.md) | Optional | Gets or sets the hotkey. |
| `at_package` | `bool` | Optional | Gets or sets a value indicating whether [at scanner]. |
| `at_quantity` | `bool` | Optional | Gets or sets a value indicating whether [at scanner]. |
| `at_additional_loading_unit` | `bool` | Optional | Gets or sets a value indicating whether [at scanner]. |
| `extended_fields` | [`LISPublicExtendedDataTableRecord`](../../doc/models/lis-public-extended-data-table-record.md) | Optional | This class represents a row within an extended table. Therefor it holds a<br>collection of {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtendedDataField}. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "unitId": "unitId8",
  "descSing": "descSing2",
  "descPlural": "descPlural2",
  "description": "description0",
  "changedOn": "2016-03-13T12:52:32.123Z"
}
```

