
# LIS Public Tour

The public tour

## Structure

`LISPublicTour`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tour_id` | `int` | Optional | Gets or sets the tour id. |
| `tour_no` | `int` | Optional | Gets or sets the tour no. |
| `dossier_no` | `string` | Optional | Gets or sets the pos no. |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Optional | Gets or sets the state. |
| `loading_date` | `datetime` | Optional | Gets or sets the loading date. |
| `loading_time` | `datetime` | Optional | Gets or sets the loading time. |
| `unloading_date` | `datetime` | Optional | Gets or sets the unloading date. |
| `unloading_time` | `datetime` | Optional | Gets or sets the unloading time. |
| `carrier_id` | `int` | Optional | Gets or sets the carrier id. |
| `lorry_id` | `string` | Optional | Gets or sets the lorry id. |
| `trailer_id` | `string` | Optional | Gets or sets the trailer id. |
| `loading_point` | [`LISPublicAddress`](../../doc/models/lis-public-address.md) | Optional | This class represents the public address object. |
| `unloading_point` | [`LISPublicAddress`](../../doc/models/lis-public-address.md) | Optional | This class represents the public address object. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `tour_information_1` | `int` | Optional | Gets or sets the tour information 1. |
| `tour_information_2` | `int` | Optional | Gets or sets the tour information 2. |
| `tour_information_3` | `int` | Optional | Gets or sets the tour information 3. |
| `tour_information_4` | `int` | Optional | Gets or sets the tour information 4. |
| `tour_information_5` | `int` | Optional | Gets or sets the tour information 5. |
| `tour_information_6` | `int` | Optional | Gets or sets the tour information 6. |
| `tour_information_7` | `int` | Optional | Gets or sets the tour information 7. |
| `tour_information_8` | `int` | Optional | Gets or sets the tour information 8. |
| `tour_information_9` | `int` | Optional | Gets or sets the tour information 9. |
| `tour_information_10` | `int` | Optional | Gets or sets the tour information 10. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `planned_by` | `string` | Optional | Gets or sets the planned by. |
| `lorry_license_plate` | `string` | Optional | Gets or sets the lorry license plate. |
| `trailer_license_plate` | `string` | Optional | Gets or sets the trailer license plate. |
| `carrier_condition_type` | [`CarrierConditionTypeEnum`](../../doc/models/carrier-condition-type-enum.md) | Optional | Gets or sets the type of the carrier condition. |
| `route_info` | [`LISPublicTourRouteInfo`](../../doc/models/lis-public-tour-route-info.md) | Optional | The public common route info |
| `aggregates` | [`LISPublicTourAggregates`](../../doc/models/lis-public-tour-aggregates.md) | Optional | The public tour aggregates |
| `charges` | `float` | Optional | Gets or sets the charges. |
| `calculated_charges` | `float` | Optional | Gets or sets the calculated charges. |
| `proceeds` | `float` | Optional | Gets or sets the proceeds. |
| `proportional_calculated_invoice_amount` | `float` | Optional | Gets or sets the proportional calculated invoice amount. |
| `proportional_credit_net_amount` | `float` | Optional | Gets or sets the proportional credit net amount. |

## Example (as JSON)

```json
{
  "tourId": 112,
  "tourNo": 72,
  "dossierNo": "dossierNo6",
  "state": "Delivered",
  "loadingDate": "2016-03-13T12:52:32.123Z"
}
```

