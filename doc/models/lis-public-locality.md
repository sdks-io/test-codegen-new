
# LIS Public Locality

It´s a locality object from the orte table.

## Structure

`LISPublicLocality`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locality_id` | `int` | Optional | The primarykey from the 'Orte' Table with CountryCode<br>DB Field: LfdNr |
| `country_code` | `string` | Optional | The car country code! It´s the primary key from the orte table.<br>DB Field: LKZ |
| `zip` | `string` | Optional | The postalcode fromt the locality<br>DB Field: PLZ |
| `city` | `string` | Optional | The cityname<br>DB Field: Ort |
| `city_district` | `string` | Optional | The CityDistrict of the named city.<br>DB Field: Ortsteil |
| `routing_info` | [`LISPublicLocalityRoutingInfo`](../../doc/models/lis-public-locality-routing-info.md) | Optional | Partial class with the correct namespace |

## Example (as JSON)

```json
{
  "localityId": 112,
  "countryCode": "countryCode4",
  "zip": "zip6",
  "city": "city0",
  "cityDistrict": "cityDistrict0"
}
```

