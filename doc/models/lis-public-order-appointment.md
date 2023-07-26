
# LIS Public Order Appointment

The order appointment data contract.

## Structure

`LISPublicOrderAppointment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `appointment_type` | [`AppointmentTypeEnum`](../../doc/models/appointment-type-enum.md) | Optional | Gets or sets the type of the appointment. |
| `loading_type` | [`LoadingTypeEnum`](../../doc/models/loading-type-enum.md) | Optional | Gets or sets the type of the loading. |
| `date_from` | `datetime` | Optional | Gets or sets the date from. |
| `time_from` | `datetime` | Optional | Gets or sets the time from. |
| `date_till` | `datetime` | Optional | Gets or sets the date till. |
| `time_till` | `datetime` | Optional | Gets or sets the time till. |

## Example (as JSON)

```json
{
  "appointmentType": "Original",
  "loadingType": "Loading",
  "dateFrom": "2016-03-13T12:52:32.123Z",
  "timeFrom": "2016-03-13T12:52:32.123Z",
  "dateTill": "2016-03-13T12:52:32.123Z"
}
```

