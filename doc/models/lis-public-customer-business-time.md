
# LIS Public Customer Business Time

The LISCustomerBusinessTime data contract.

## Structure

`LISPublicCustomerBusinessTime`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `day_of_week` | [`DayOfWeekEnum`](../../doc/models/day-of-week-enum.md) | Optional | Gets or sets DayOfWeek. |
| `loading_from_1` | `datetime` | Optional | Gets or sets LoadingFrom1. |
| `loading_to_1` | `datetime` | Optional | Gets or sets LoadingTo1. |
| `loading_from_2` | `datetime` | Optional | Gets or sets LoadingFrom2. |
| `loading_to_2` | `datetime` | Optional | Gets or sets LoadingTo2. |
| `unloading_from_1` | `datetime` | Optional | Gets or sets UnloadingFrom1. |
| `unloading_to_1` | `datetime` | Optional | Gets or sets UnloadingTo1. |
| `unloading_from_2` | `datetime` | Optional | Gets or sets UnloadingFrom2. |
| `unloading_to_2` | `datetime` | Optional | Gets or sets UnloadingTo2. |
| `loading_duration` | `int` | Optional | Gets or sets LoadingDuration. |
| `unloading_duration` | `int` | Optional | Gets or sets UnloadingDuration. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "dayOfWeek": "Thursday",
  "loadingFrom1": "2016-03-13T12:52:32.123Z",
  "loadingTo1": "2016-03-13T12:52:32.123Z",
  "loadingFrom2": "2016-03-13T12:52:32.123Z"
}
```

