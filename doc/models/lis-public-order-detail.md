
# LIS Public Order Detail

The LISOrderDetail data contract.

## Structure

`LISPublicOrderDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `units` | [`List of LISPublicOrderDetailUnit`](../../doc/models/lis-public-order-detail-unit.md) | Optional | Gets or sets Units. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `detail_id` | `int` | Optional | Gets or sets DetailId. |
| `reference` | `string` | Optional | Gets or sets Reference. |
| `content` | `string` | Optional | Gets or sets Content. |
| `weight` | `float` | Optional | Gets or sets Weight. |
| `tare_weight` | `float` | Optional | Gets or sets TareWeight. |
| `chargeable_weight` | `float` | Optional | Gets or sets ChargeableWeight. |
| `bulky_weight` | `float` | Optional | Gets or sets BulkyWeight. |
| `tariff_id` | `string` | Optional | Gets or sets ChargeId. |
| `article_no` | `string` | Optional | Gets or sets ArticleNo. |
| `cubic_decimeter` | `float` | Optional | Gets or sets CubicDecimeter. |
| `loading_meter` | `float` | Optional | Gets or sets LoadingMeter. |
| `square_meter` | `float` | Optional | Gets or sets SquareMeter. |
| `storage_places` | `float` | Optional | Gets or sets StoragePlaces. |
| `declared_value` | `float` | Optional | Gets or sets DeclaredValue. |
| `hazardous_good_qualified` | `bool` | Optional | Gets or sets HazardousGoodQualified. |
| `free_text_1` | `string` | Optional | Gets or sets FreeText1. |
| `free_text_2` | `string` | Optional | Gets or sets FreeText2. |
| `free_text_3` | `string` | Optional | Gets or sets FreeText3. |
| `free_number_1` | `int` | Optional | Gets or sets FreeNumber1. |
| `free_number_2` | `int` | Optional | Gets or sets FreeNumber2. |
| `free_date_1` | `datetime` | Optional | Gets or sets FreeDate1. |
| `free_date_2` | `datetime` | Optional | Gets or sets FreeDate2. |
| `free_amount_1` | `float` | Optional | Gets or sets FreeAmount1. |
| `free_amount_2` | `float` | Optional | Gets or sets FreeAmount2. |
| `free_amount_3` | `float` | Optional | Gets or sets the free amount3. |
| `free_amount_4` | `float` | Optional | Gets or sets the free amount4. |
| `free_amount_5` | `float` | Optional | Gets or sets the free amount5. |
| `free_amount_6` | `float` | Optional | Gets or sets the free amount6. |
| `free_amount_7` | `float` | Optional | Gets or sets the free amount7. |
| `free_amount_8` | `float` | Optional | Gets or sets the free amount8. |
| `free_amount_9` | `float` | Optional | Gets or sets the free amount9. |
| `free_amount_10` | `float` | Optional | Gets or sets the free amount10. |
| `free_amount_11` | `float` | Optional | Gets or sets the free amount11. |
| `free_amount_12` | `float` | Optional | Gets or sets the free amount12. |
| `temp_min` | `float` | Optional | Gets or sets the temporary minimum. |
| `temp_max` | `float` | Optional | Gets or sets the temporary maximum. |
| `freight_payer_id` | `int` | Optional | Gets or sets FreightPayerId. |
| `reefer_cargo` | `bool` | Optional | Gets or sets ReeferCargo. |
| `sub_pallet` | `string` | Optional | Gets or sets SubPallet. |
| `height` | `int` | Optional | Gets or sets Height. |
| `length` | `int` | Optional | Gets or sets Length. |
| `width` | `int` | Optional | Gets or sets Width. |
| `goods_group` | `string` | Optional | Gets or sets GoodsGroup. |
| `target_quantity` | `float` | Optional | Gets or sets TargetQuantity. |
| `content_2` | `string` | Optional | Gets or sets Content2. |
| `target_pallets` | `float` | Optional | Gets or sets TargetPallets. |
| `target_weight` | `float` | Optional | Gets or sets TargetWeight. |
| `cost_center` | `int` | Optional | Gets or sets CostCenter. |
| `cost_unit` | `int` | Optional | Gets or sets CostUnit. |
| `account_table` | `int` | Optional | Gets or sets AccountTable. |
| `account_table_sap` | `string` | Optional | Gets or sets AccountTableSAP. |
| `cost_center_sap` | `string` | Optional | Gets or sets CostCenterSAP. |
| `cost_unit_sap` | `string` | Optional | Gets or sets CostUnitSAP. |
| `target_package` | `float` | Optional | Gets or sets TargetPackage. |
| `detail_reference` | `string` | Optional | Gets or sets DetailReference. |
| `goods_class` | `string` | Optional | Gets or sets GoodsClass. |
| `target_storage_places` | `float` | Optional | Gets or sets TargetStoragePlaces. |
| `statistical_commodity_code` | `string` | Optional | Gets or sets StatisticalCommodityCode. |
| `compartment` | `string` | Optional | Gets or sets Compartment. |
| `insurable_value` | `float` | Optional | Gets or sets InsurableValue. |
| `created_on` | `datetime` | Optional | Gets or sets CreatedOn. |
| `created_by` | `string` | Optional | Gets or sets CreatedBy. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `efb_observe` | [`EfbObserveEnum`](../../doc/models/efb-observe-enum.md) | Optional | Gets or sets the efb observe. |
| `empties` | [`EmptiesEnum`](../../doc/models/empties-enum.md) | Optional | Gets or sets the empties. |
| `ecological_menace` | [`EcologicalMenace1Enum`](../../doc/models/ecological-menace-1-enum.md) | Optional | Gets or sets the ecological menace. |
| `dangerous_goods` | [`List of LISPublicOrderDGood`](../../doc/models/lis-public-order-d-good.md) | Optional | Gets or sets the dangerous goods. |
| `un_number` | `int` | Optional | Gets or sets the un number. |
| `un_class` | `string` | Optional | Gets or sets the un class. |
| `un_digit` | `string` | Optional | Gets or sets the un digit. |
| `order_d_good_id` | `int` | Optional | Gets or sets the order d good identifier. |
| `transport_category` | `string` | Optional | Gets or sets the transport category. |
| `container_id` | `string` | Optional | Gets or sets the container identifier. |
| `container_amount` | `float` | Optional | Gets or sets the container amount. |
| `container_type` | `string` | Optional | Gets or sets the type of the container. |
| `statistic_value` | `float` | Optional | Gets or sets the statistic value. |
| `component` | `string` | Optional | Gets or sets the component. |
| `intra_int_nr` | `int` | Optional | Gets or sets the intra int nr. |
| `outra_int_nr` | `int` | Optional | Gets or sets the outra int nr. |
| `booking` | `int` | Optional | Gets or sets the booking. |
| `zoll_intnr` | `int` | Optional | Gets or sets the zoll intnr. |
| `cont_plombe` | `string` | Optional | Gets or sets the cont plombe. |
| `delivery_note_package_reference` | `int` | Optional | Gets or sets the delivery note package reference. |

## Example (as JSON)

```json
{
  "units": [
    {
      "unitType": "Quantity",
      "unitId": "unitId9",
      "quantity": 190.83,
      "createdOn": "2016-03-13T12:52:32.123Z",
      "createdBy": "createdBy5"
    },
    {
      "unitType": "All",
      "unitId": "unitId0",
      "quantity": 190.84,
      "createdOn": "2016-03-13T12:52:32.123Z",
      "createdBy": "createdBy4"
    },
    {
      "unitType": "Unkown",
      "unitId": "unitId1",
      "quantity": 190.85,
      "createdOn": "2016-03-13T12:52:32.123Z",
      "createdBy": "createdBy3"
    }
  ],
  "orderId": 62,
  "detailId": 234,
  "reference": "reference4",
  "content": "content4"
}
```

