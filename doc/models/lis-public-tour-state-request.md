
# LIS Public Tour State Request

A request for a public tour state.

## Structure

`LISPublicTourStateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tour_id` | `int` | Optional | Gets or sets the tour id. |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Optional | Gets or sets the state. |

## Example (as JSON)

```json
{
  "tourId": 112,
  "state": "Delivered"
}
```

