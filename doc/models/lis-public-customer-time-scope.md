
# LIS Public Customer Time Scope

The LISCustomerTimeScope data contract.

## Structure

`LISPublicCustomerTimeScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_times` | [`List of LISPublicCustomerBusinessTime`](../../doc/models/lis-public-customer-business-time.md) | Optional | Gets or sets BusinessTimes. |
| `closed_dates` | [`List of LISPublicCustomerClosedDate`](../../doc/models/lis-public-customer-closed-date.md) | Optional | Gets or sets ClosedDates. |
| `federal_state` | `string` | Optional | Gets or sets the state of the federal. |
| `tolerance_minutes` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "businessTimes": [
    {
      "customerId": 68,
      "dayOfWeek": "Tuesday",
      "loadingFrom1": "2016-03-13T12:52:32.123Z",
      "loadingTo1": "2016-03-13T12:52:32.123Z",
      "loadingFrom2": "2016-03-13T12:52:32.123Z"
    }
  ],
  "closedDates": [
    {
      "customerId": 199,
      "closedForLoading": true,
      "closedForUnloading": true,
      "closedFrom": "2016-03-13T12:52:32.123Z",
      "closedTill": "2016-03-13T12:52:32.123Z"
    },
    {
      "customerId": 200,
      "closedForLoading": false,
      "closedForUnloading": false,
      "closedFrom": "2016-03-13T12:52:32.123Z",
      "closedTill": "2016-03-13T12:52:32.123Z"
    },
    {
      "customerId": 201,
      "closedForLoading": true,
      "closedForUnloading": true,
      "closedFrom": "2016-03-13T12:52:32.123Z",
      "closedTill": "2016-03-13T12:52:32.123Z"
    }
  ],
  "federalState": "federalState6",
  "toleranceMinutes": 34
}
```

