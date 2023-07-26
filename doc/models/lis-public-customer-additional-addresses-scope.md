
# LIS Public Customer Additional Addresses Scope

The LISCustomerAdditionalAddressesScope data contract.

## Structure

`LISPublicCustomerAdditionalAddressesScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_roles` | [`List of LISPublicCustomerAddressRole`](../../doc/models/lis-public-customer-address-role.md) | Optional | Gets or sets AddressRoles. |
| `copy_lock` | `bool` | Optional | Gets or sets the copy lock. |
| `transshipment_point` | `int` | Optional | Gets or sets the transshipment point. |
| `warehouse_scanning` | `bool` | Optional | Gets or sets the warehouse scanning. |
| `external_address_id` | `string` | Optional | Gets or sets the external address id. |

## Example (as JSON)

```json
{
  "addressRoles": [
    {
      "customerAddressRoleId": 254,
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy0",
      "customerId": 42,
      "customerSequenceNo": 150
    },
    {
      "customerAddressRoleId": 255,
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy1",
      "customerId": 43,
      "customerSequenceNo": 151
    },
    {
      "customerAddressRoleId": 0,
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy2",
      "customerId": 44,
      "customerSequenceNo": 152
    }
  ],
  "copyLock": false,
  "transshipmentPoint": 0,
  "warehouseScanning": false,
  "externalAddressId": "externalAddressId0"
}
```

