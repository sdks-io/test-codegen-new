
# LIS Public Customer Address

Represents a customer address.

## Structure

`LISPublicCustomerAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adress_type` | [`AdressTypeEnum`](../../doc/models/adress-type-enum.md) | Optional | Gets or sets the type of the adress. |
| `post_office_box` | `string` | Optional | Gets or sets the post office box. |
| `post_office_zip_code` | `string` | Optional | Gets or sets the post office zip code. |
| `address_id` | `int` | Optional | The id of the address (at the moment must be the same as the locality id) |
| `locality` | [`LISPublicLocality`](../../doc/models/lis-public-locality.md) | Optional | It´s a locality object from the orte table. |
| `street` | `string` | Optional | The street of the address including the House number |
| `coordinate` | [`LISPublicCoordinate`](../../doc/models/lis-public-coordinate.md) | Optional | This class represents the public coordinate object. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |

## Example (as JSON)

```json
{
  "adressType": "InvoiceAddress",
  "postOfficeBox": "postOfficeBox0",
  "postOfficeZipCode": "postOfficeZipCode8",
  "addressId": 240,
  "locality": {
    "localityId": 94,
    "countryCode": "countryCode4",
    "zip": "zip6",
    "city": "city0",
    "cityDistrict": "cityDistrict0"
  }
}
```

