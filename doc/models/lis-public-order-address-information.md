
# LIS Public Order Address Information

The LISOrderAddressInformation data contract.

## Structure

`LISPublicOrderAddressInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `contact_person_id` | `int` | Optional | Gets or sets ContactPersonId. |
| `address_type` | [`AddressType1Enum`](../../doc/models/address-type-1-enum.md) | Optional | Gets or sets AddressType. |

## Example (as JSON)

```json
{
  "customerId": 114,
  "contactPersonId": 78,
  "addressType": "Sender"
}
```

