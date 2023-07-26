
# LIS Public Customer Loading Point Scope

The LISCustomerLoadingPointScope data contract.

## Structure

`LISPublicCustomerLoadingPointScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name_1` | `string` | Optional | Gets or sets Name1. |
| `name_2` | `string` | Optional | Gets or sets Name2. |
| `name_3` | `string` | Optional | Gets or sets Name3. |
| `address` | [`LISPublicCustomerLoadingPointAddress`](../../doc/models/lis-public-customer-loading-point-address.md) | Optional | Represents a customer address. |
| `differing_loading_point` | `int` | Optional | Gets or sets DifferingLoadingPoint. |
| `differing_unloading_point` | `int` | Optional | Gets or sets DifferingUnloadingPoint. |

## Example (as JSON)

```json
{
  "name1": "name10",
  "name2": "name24",
  "name3": "name34",
  "address": {
    "addressId": 224,
    "locality": {
      "localityId": 146,
      "countryCode": "countryCode8",
      "zip": "zip0",
      "city": "city6",
      "cityDistrict": "cityDistrict6"
    },
    "street": "street6",
    "coordinate": {
      "longitude": 123.98,
      "latitude": 129.82
    },
    "changedOn": "2016-03-13T12:52:32.123Z"
  },
  "differingLoadingPoint": 196
}
```

