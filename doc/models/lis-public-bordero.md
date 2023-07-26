
# LIS Public Bordero

The LISBordero data contract.

## Structure

`LISPublicBordero`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loading_relation_id` | `string` | Optional | Gets or sets the LoadingRelationId property. This property depends on the database field Relation. |
| `unloading_relation_id` | `string` | Optional | Gets or sets the UnloadingRelationId property. This property depends on the database field Relation. |
| `destination_forwarder_id` | `int` | Optional | Gets or sets the DestinationForwarderId property. This property depends on the database field EmpSped. |
| `disposition_text` | `string` | Optional | Gets or sets the DispositionText property. This property depends on the database field AufText. |
| `remark` | `string` | Optional | Gets or sets the Remark property. This property depends on the database field AufInfo. |
| `route_info` | [`LISPublicRouteInfo`](../../doc/models/lis-public-route-info.md) | Optional | Only the basic route informations. |
| `destination_forwarder_condition_type` | [`DestinationForwarderConditionTypeEnum`](../../doc/models/destination-forwarder-condition-type-enum.md) | Optional | Gets or sets the DestinationForwarderConditionType property. This property depends on the database field ESKond. |
| `destination_forwarder_sales_tax_code` | `string` | Optional | Gets or sets the DestinationForwarderSalesTaxCode property. This property depends on the database field ESUC. |
| `swap_body_1` | `string` | Optional | Gets or sets the SwapBody1 property. This property depends on the database field WB1. |
| `swap_body_2` | `string` | Optional | Gets or sets the SwapBody2 property. This property depends on the database field WB2. |
| `security_tag_1` | `string` | Optional | Gets or sets the SecurityTag1 property. This property depends on the database field Plombe1. |
| `security_tag_2` | `string` | Optional | Gets or sets the SecurityTag2 property. This property depends on the database field Plombe2. |
| `traffic_mode_id` | `string` | Optional | Gets or sets the traffic mode identifier. |
| `aggregates` | [`LISPublicBorderoAggregates`](../../doc/models/lis-public-bordero-aggregates.md) | Optional | The LISPulbicBorderoAggregates. The LISPulbicBorderoAggregates are readonly. |
| `appointments` | [`List of LISPublicBorderoAppointment`](../../doc/models/lis-public-bordero-appointment.md) | Optional | Gets or sets the appointments. |
| `bordero_informations` | [`List of LISPublicBorderoInformation`](../../doc/models/lis-public-bordero-information.md) | Optional | Gets or sets the bordero informations. |
| `stations` | [`List of LISPublicShipmentStation`](../../doc/models/lis-public-shipment-station.md) | Optional | Gets or sets the stations. |
| `address_roles` | [`List of LISPublicBorderoAddressRole`](../../doc/models/lis-public-bordero-address-role.md) | Optional | Gets or sets the address roles. |
| `fees` | [`List of LISPublicCommonLumpSum`](../../doc/models/lis-public-common-lump-sum.md) | Optional | Gets or sets Fees. |
| `has_manual_condition` | `bool` | Optional | Gets or sets a value indicating whether this instance has manual condition. |
| `permission` | [`LISPublicBorderoPermission`](../../doc/models/lis-public-bordero-permission.md) | Optional | The LISBorderoPermission data contract. |
| `is_last` | `bool` | Optional | Gets or sets a value indicating whether this instance is last. |
| `condition_temporary_identifier` | `string` | Optional | Gets or sets the condition temporary identifier. |
| `company_id` | `int` | Optional | Gets or sets CompanyId. |
| `division_id` | `int` | Optional | Gets or sets DivisionId. |
| `department_id` | `int` | Optional | Gets or sets DepartmentId. |
| `bordero_id` | `int` | Optional | Gets or sets BorderoId. |
| `bordero_dummy_id` | `int` | Optional | Gets or sets BorderoDummyId. |
| `bordero_no` | `int` | Optional | Gets or sets BorderoNo. |
| `bordero_kind` | [`BorderoKindEnum`](../../doc/models/bordero-kind-enum.md) | Optional | Gets or sets BorderoKind. |
| `transshipment_bordero` | [`TransshipmentBorderoEnum`](../../doc/models/transshipment-bordero-enum.md) | Optional | Gets or sets TransshipmentBordero. |
| `transshipment_bordero_handover` | [`TransshipmentBorderoHandoverEnum`](../../doc/models/transshipment-bordero-handover-enum.md) | Optional | Gets or sets the transshipment bordero handover. |
| `fill_type` | [`FillType1Enum`](../../doc/models/fill-type-1-enum.md) | Optional | Gets or sets FillType. |
| `capture_division` | `int` | Optional | Gets or sets CaptureDivision. |
| `capture_department` | `int` | Optional | Gets or sets CaptureDepartment. |
| `capture_date` | `datetime` | Optional | Gets or sets CaptureDate. |
| `bordero_sequence` | `int` | Optional | Gets or sets BorderoSequence. |
| `internal_cost_allocation_mode` | [`InternalCostAllocationMode1Enum`](../../doc/models/internal-cost-allocation-mode-1-enum.md) | Optional | Gets or sets InternalCostAllocationMode. |
| `bordero_type` | [`BorderoTypeEnum`](../../doc/models/bordero-type-enum.md) | Optional | Gets or sets the type of the bordero. |
| `bordero_type_text_id` | `int` | Optional | Gets or sets the bordero type text identifier. |
| `invoicing_type` | [`InvoicingTypeEnum`](../../doc/models/invoicing-type-enum.md) | Optional | Gets or sets the type of the invoicing. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `created_on` | `datetime` | Optional | Gets or sets the date the item was created. |
| `created_by` | `string` | Optional | Gets or sets the name of the user that created this item. |
| `order_type` | [`OrderType1Enum`](../../doc/models/order-type-1-enum.md) | Optional | Gets or sets the type of the order. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "loadingRelationId": "loadingRelationId2",
  "unloadingRelationId": "unloadingRelationId6",
  "destinationForwarderId": 46,
  "dispositionText": "dispositionText2",
  "remark": "remark6"
}
```

