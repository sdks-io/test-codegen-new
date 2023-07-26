
# LIS Response List LIS Public Customer Base View

The api response class.

## Structure

`LISResponseListLISPublicCustomerBaseView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicCustomerBaseView`](../../doc/models/lis-public-customer-base-view.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "customerId": 136,
      "customerShort": "customerShort6",
      "name1": "name16",
      "name2": "name20",
      "name3": "name30"
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

