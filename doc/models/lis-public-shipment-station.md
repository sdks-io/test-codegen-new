
# LIS Public Shipment Station

The shipment station.

## Structure

`LISPublicShipmentStation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `station_type` | [`StationTypeEnum`](../../doc/models/station-type-enum.md) | Optional | Gets or sets the type of the station. |
| `operation_hours` | [`List of LISPublicOperationHours`](../../doc/models/lis-public-operation-hours.md) | Optional | Gets or sets the operation hours. |
| `shipment_address` | [`LISPublicAddress`](../../doc/models/lis-public-address.md) | Optional | This class represents the public address object. |
| `locality_id` | `int` | Optional | Gets or sets the locality id. |
| `country_code` | `string` | Optional | Gets or sets the country code. |
| `customer_id` | `int` | Optional | Gets or sets the customer id. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |
| `customer_short` | `string` | Optional | Gets or sets the customer short. |
| `name_1` | `string` | Optional | Gets or sets the name1. |
| `name_2` | `string` | Optional | Gets or sets the name2. |
| `name_3` | `string` | Optional | Gets or sets the name3. |
| `customer_type` | [`CustomerTypeEnum`](../../doc/models/customer-type-enum.md) | Optional | Gets or sets the type of the customer. |
| `address` | [`LISPublicCustomerAddress`](../../doc/models/lis-public-customer-address.md) | Optional | Represents a customer address. |
| `extended_address_id` | `string` | Optional | Gets or sets the extended address id. |
| `blocked_from_date` | `datetime` | Optional | Gets or sets the blocked from date. |
| `mdm_debit_state` | [`MdmDebitStateEnum`](../../doc/models/mdm-debit-state-enum.md) | Optional | Gets or sets the state of the MDM debit. |
| `mdm_credit_state` | [`MdmCreditStateEnum`](../../doc/models/mdm-credit-state-enum.md) | Optional | Gets or sets the state of the MDM credit. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "stationType": "LoadingAddress",
  "operationHours": [
    {
      "dayOfWeek": "Saturday",
      "loadingTimeFrom1": "2016-03-13T12:52:32.123Z",
      "loadingTimeTo1": "2016-03-13T12:52:32.123Z",
      "loadingTimeFrom2": "2016-03-13T12:52:32.123Z",
      "loadingTimeTo2": "2016-03-13T12:52:32.123Z"
    }
  ],
  "shipmentAddress": {
    "addressId": 248,
    "locality": {
      "localityId": 122,
      "countryCode": "countryCode8",
      "zip": "zip0",
      "city": "city6",
      "cityDistrict": "cityDistrict6"
    },
    "street": "street6",
    "coordinate": {
      "longitude": 108.38,
      "latitude": 145.42
    },
    "changedOn": "2016-03-13T12:52:32.123Z"
  },
  "localityId": 112,
  "countryCode": "countryCode4"
}
```

