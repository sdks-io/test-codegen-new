
# LIS Public Order Tour

A base class for all order data contracts.

## Structure

`LISPublicOrderTour`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tour_id` | `int` | Optional | The internal number of the Tour<br>DB:TourIntNr |
| `tour_no` | `int` | Optional | The number of the Tour<br>DB:TourNr |
| `state` | [`State2Enum`](../../doc/models/state-2-enum.md) | Optional | The state of the tour<br>DB:Status |
| `lorry_id` | `string` | Optional | Gets or sets the lorry.<br>DB: #*Tour.KfzZugId |
| `trailer_id` | `string` | Optional | Gets or sets the trailer.<br>DB: #*Tour.KfzAnhId |
| `swap_body_1` | `string` | Optional | Gets or sets the swap body1.<br>DB:#*Tour.WBruecke1 |
| `swap_body_2` | `string` | Optional | Gets or sets the swap body2.<br>DB:#*Tour.WBruecke2 |
| `lorry_license_plate` | `string` | Optional | Gets or sets the lorry license plate.<br>DB:#*Tour.KfzPolKz |
| `trailer_license_plate` | `string` | Optional | Gets or sets the trailer license plate.<br>DB:#*Tour.AnhPolKz |
| `driver_id` | `int` | Optional | The dirver of the tour<br>DB: #*Tour.FahId |
| `co_driver_id` | `int` | Optional | The co dirver of the tour<br>DB: #*Tour.BFahId |
| `lorry_group_id` | `string` | Optional | Gets or sets the lorry group identifier. |
| `permit_id` | `string` | Optional | Gets or sets the permit identifier. |
| `carrier_id` | `int` | Optional | Gets or sets the carrier identifier. |

## Example (as JSON)

```json
{
  "tourId": 112,
  "tourNo": 72,
  "state": "Delivered",
  "lorryId": "lorryId4",
  "trailerId": "trailerId6"
}
```

