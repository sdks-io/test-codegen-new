
# LIS Public Transport Section Base

The LISTransportSectionEntityBase is the base class for the two derived classes LISPublicTransportSectionBordero and LISPublicTransportSectionShipment. These classes are described in the list of public services structures on the left side.

## Structure

`LISPublicTransportSectionBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transport_section_type` | `string` | Optional | Gets or sets the TranportSectionType |
| `bordero_id` | `int` | Optional | Gets or sets the TranportSectionType |
| `company_id` | `int` | Optional | Gets or sets CompanyId. |
| `division_id` | `int` | Optional | Gets or sets DivisionId. |
| `department_id` | `int` | Optional | Gets or sets DepartmentId. |
| `tour_id` | `int` | Optional | Gets or sets TourId. |
| `id` | `int` | Optional | Gets or sets Id. |
| `no` | `int` | Optional | Gets or sets No. |
| `sub_no` | `int` | Optional | Gets or sets SubNo. |
| `sequence` | `int` | Optional | Gets or sets Sequence. |
| `is_last` | `bool` | Optional | Gets or sets IsLast. |
| `appointments` | [`List of LISPublicOrderAppointment`](../../doc/models/lis-public-order-appointment.md) | Optional | Gets or sets Appointments. |
| `aggregates` | [`LISPublicOrderAggregates`](../../doc/models/lis-public-order-aggregates.md) | Optional | The LIS Order aggregates. |
| `stations` | [`List of LISPublicShipmentStation`](../../doc/models/lis-public-shipment-station.md) | Optional | Gets or sets Stations. |
| `prev_shipment_dispatch_calculated_unloading_time` | `datetime` | Optional | Gets or sets the order informations. |
| `prev_shipment_id` | `int` | Optional | Gets or sets the type of the order. |
| `prev_shipment_tour_id` | `int` | Optional | Gets or sets the previous shipment tour no. |
| `prev_shipment_tour_no` | `int` | Optional | Gets or sets the previous shipment tour identifier. |

## Example (as JSON)

```json
{
  "transportSectionType": "transportSectionType2",
  "borderoId": 222,
  "companyId": 68,
  "divisionId": 106,
  "departmentId": 116
}
```

