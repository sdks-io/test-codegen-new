
# LIS Public Operation Hours

The operation hours.

## Structure

`LISPublicOperationHours`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day_of_week` | [`DayOfWeek1Enum`](../../doc/models/day-of-week-1-enum.md) | Optional | Gets or sets the day of week. |
| `loading_time_from_1` | `datetime` | Optional | Gets or sets the loading time from1. |
| `loading_time_to_1` | `datetime` | Optional | Gets or sets the loading time to1. |
| `loading_time_from_2` | `datetime` | Optional | Gets or sets the loading time from2. |
| `loading_time_to_2` | `datetime` | Optional | Gets or sets the loading time to2. |
| `loading_time_span` | `int` | Optional | Gets or sets the loading time span. |
| `delivery_time_from_1` | `datetime` | Optional | Gets or sets the delivery time from1. |
| `delivery_time_to_1` | `datetime` | Optional | Gets or sets the delivery time to1. |
| `delivery_time_from_2` | `datetime` | Optional | Gets or sets the delivery time from2. |
| `delivery_time_to_2` | `datetime` | Optional | Gets or sets the delivery time to2. |
| `delivery_time_span` | `int` | Optional | Gets or sets the delivery time span. |

## Example (as JSON)

```json
{
  "dayOfWeek": "Saturday",
  "loadingTimeFrom1": "2016-03-13T12:52:32.123Z",
  "loadingTimeTo1": "2016-03-13T12:52:32.123Z",
  "loadingTimeFrom2": "2016-03-13T12:52:32.123Z",
  "loadingTimeTo2": "2016-03-13T12:52:32.123Z"
}
```

