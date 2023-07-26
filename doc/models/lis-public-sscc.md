
# LIS Public SSCC

The LISSSCC data contract.

## Structure

`LISPublicSSCC`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sscc_id` | `int` | Optional | Gets or sets SSCCId. |
| `sscc` | `string` | Optional | Gets or sets SSCC. |
| `sequence_no` | `int` | Optional | Gets or sets SequenceNo. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `order_detail_id` | `int` | Optional | Gets or sets OrderDetailId. |
| `kind` | [`KindEnum`](../../doc/models/kind-enum.md) | Optional | Gets or sets Kind. |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Optional | Gets or sets Type. |
| `sscc_status_text_id` | `int` | Optional | Gets or sets SSCCStatusTextId. |
| `sscc_status_history_id` | `int` | Optional | Gets or sets SSCCStatusHistoryId. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `damage_state` | [`DamageStateEnum`](../../doc/models/damage-state-enum.md) | Optional | Gets or sets DamageState. |
| `sscc_foreign` | `string` | Optional | Gets or sets SSCCForeign. |
| `sscc_foreign_2` | `string` | Optional | Gets or sets SSCCForeign2. |
| `sscc_foreign_return` | `string` | Optional | Gets or sets SSCCForeignReturn. |
| `service_provider_control` | `string` | Optional | Gets or sets ServiceProviderControl. |
| `stock_location` | `string` | Optional | Gets or sets StockLocation. |
| `inbound_carrier_id` | `int` | Optional | Gets or sets InboundCarrierId. |
| `inbound_bordero_id` | `int` | Optional | Gets or sets InboundBorderoId. |
| `picked_up` | `bool` | Optional | Gets or sets PickedUp. |
| `delivered` | `bool` | Optional | Gets or sets Delivered. |
| `inbound_scan` | `bool` | Optional | Gets or sets InboundScan. |
| `outbound_scan` | `bool` | Optional | Gets or sets OutboundScan. |
| `inbound_scan_odd` | `bool` | Optional | Gets or sets InboundScanOdd. |
| `outbound_scan_odd` | `bool` | Optional | Gets or sets OutboundScanOdd. |
| `date_of_hall_revision` | `datetime` | Optional | Gets or sets DateOfHallRevision. |
| `real_height` | `float` | Optional | Gets or sets RealHeight. |
| `real_width` | `float` | Optional | Gets or sets RealWidth. |
| `real_length` | `float` | Optional | Gets or sets RealLength. |
| `real_package` | `string` | Optional | Gets or sets RealPackage. |
| `real_pallet_unit` | `string` | Optional | Gets or sets RealPalletUnit. |
| `real_pallet_unit_count` | `int` | Optional | Gets or sets RealPalletUnitCount. |
| `real_weight` | `float` | Optional | Gets or sets RealWeight. |
| `hall_revision_state` | [`HallRevisionStateEnum`](../../doc/models/hall-revision-state-enum.md) | Optional | Gets or sets HallRevisionState. |
| `quantity_unit` | `string` | Optional | Gets or sets the quantity unit. |
| `quantity_count` | `int` | Optional | Gets or sets the quantity count. |
| `relation` | `string` | Optional | Gets or sets the quantity unit. |
| `additional_info` | `string` | Optional | Gets or sets the additional information. |
| `text` | `string` | Optional | Gets or sets the iln nummer. |
| `planned_unit` | `string` | Optional | Gets or sets the needed pallet unit. |
| `chargen_no` | `string` | Optional | Gets or sets the chargen nummer. |

## Example (as JSON)

```json
{
  "ssccId": 166,
  "sscc": "sscc2",
  "sequenceNo": 226,
  "orderId": 62,
  "orderDetailId": 218
}
```

