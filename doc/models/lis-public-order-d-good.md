
# LIS Public Order D Good

The LISOrderDGood data contract.

## Structure

`LISPublicOrderDGood`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `d_good_id` | `int` | Optional | Gets or sets DGoodId. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `order_detail_id` | `int` | Optional | Gets or sets OrderDetailId. |
| `un_number_id` | `int` | Optional | Gets or sets UNNumberId. |
| `un_number` | `string` | Optional | Gets or sets UNNumber. |
| `transport_category` | `string` | Optional | Gets or sets TransportCategory. |
| `un_class` | `string` | Optional | Gets or sets UNClass. |
| `un_digit` | `string` | Optional | Gets or sets UNDigit. |
| `un_character` | `string` | Optional | Gets or sets UNCharacter. |
| `material_name` | `string` | Optional | Gets or sets MaterialName. |
| `chemical_name` | `string` | Optional | Gets or sets ChemicalName. |
| `nos_entrie` | `string` | Optional | Gets or sets NOSEntrie. |
| `material_amount` | `float` | Optional | Gets or sets MaterialAmount. |
| `factor` | `float` | Optional | Gets or sets Factor. |
| `score` | `float` | Optional | Gets or sets Score. |
| `code` | `string` | Optional | Gets or sets Code. |
| `kemler_number` | `string` | Optional | Gets or sets KemlerNumber. |
| `limited_quantity` | `string` | Optional | Gets or sets LimitedQuantity. |
| `package_type` | `string` | Optional | Gets or sets PackageType. |
| `packages` | `float` | Optional | Gets or sets Packages. |
| `weight` | `float` | Optional | Gets or sets Weight. |
| `gross_weight` | `float` | Optional | Gets or sets GrossWeight. |
| `net_weight` | `float` | Optional | Gets or sets NetWeight. |
| `cubic_decimeter` | `float` | Optional | Gets or sets CubicDecimeter. |
| `flash_point` | `float` | Optional | Gets or sets FlashPoint. |
| `label_1` | `string` | Optional | Gets or sets Label1. |
| `label_2` | `string` | Optional | Gets or sets Label2. |
| `label_3` | `string` | Optional | Gets or sets Label3. |
| `label_4` | `string` | Optional | Gets or sets Label4. |
| `special_provisions` | `string` | Optional | Gets or sets SpecialProvisions. |
| `tunnelcode` | `string` | Optional | Gets or sets Tunnelcode. |
| `compatibility_group` | `string` | Optional | Gets or sets CompatibilityGroup. |
| `ecological_menace_flag` | [`EcologicalMenaceFlagEnum`](../../doc/models/ecological-menace-flag-enum.md) | Optional | Gets or sets EcologicalMenaceFlag. |
| `disposal_observation` | [`DisposalObservationEnum`](../../doc/models/disposal-observation-enum.md) | Optional | Gets or sets DisposalObservation. |
| `group_id` | `int` | Optional | Gets or sets GroupId. |
| `un_type` | [`UnTypeEnum`](../../doc/models/un-type-enum.md) | Optional | Gets or sets UNType. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |
| `pi_pass_nr` | `string` | Optional | Gets or sets the pi pass nr. |
| `pi_pass_max` | `string` | Optional | Gets or sets the pi pass maximum. |
| `ypi_pass_nr` | `string` | Optional | Gets or sets the ypi pass nr. |
| `ypi_pass_max` | `string` | Optional | Gets or sets the ypi pass maximum. |
| `pi_cargo_nr` | `string` | Optional | Gets or sets the pi cargo nr. |
| `pi_cargo_max` | `string` | Optional | Gets or sets the pi cargo maximum. |
| `erg_code` | `string` | Optional | Gets or sets the erg code. |
| `em_s_nummer_1` | `string` | Optional | Gets or sets the em s nummer1. |
| `em_s_nummer_2` | `string` | Optional | Gets or sets the em s nummer2. |
| `composite_packaging` | `int` | Optional | Gets or sets the composite packaging. |
| `reference_id` | `int` | Optional | Gets or sets the reference identifier. |
| `reference_type` | [`ReferenceTypeEnum`](../../doc/models/reference-type-enum.md) | Optional | Gets or sets the type of the reference. |
| `route_determination` | `int` | Optional | Gets or sets the route determination. |
| `serious_hazard` | `int` | Optional | Gets or sets the serious hazard. |
| `excepted_quantities` | `string` | Optional | Gets or sets the excepted quantities. |
| `sort_index` | `int` | Optional | Gets or sets the index of the sort. |

## Example (as JSON)

```json
{
  "dGoodId": 194,
  "orderId": 62,
  "orderDetailId": 218,
  "unNumberId": 86,
  "unNumber": "unNumber8"
}
```

