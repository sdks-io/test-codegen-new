
# LIS Public Customer Contact Person

The LISCustomerContactPerson data contract.

## Structure

`LISPublicCustomerContactPerson`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transport_types` | `List of string` | Optional | Gets or sets the transport types. |
| `customer_contact_person_id` | `int` | Optional | Gets or sets CustomerContactPersonId. |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `name` | `string` | Optional | Gets or sets Name. |
| `forename` | `string` | Optional | Gets or sets Forename. |
| `mc` | `string` | Optional | Gets or sets MC. |
| `title` | `string` | Optional | Gets or sets Title. |
| `gender` | `string` | Optional | Gets or sets Gender. |
| `role` | `string` | Optional | Gets or sets Function. |
| `activity` | `string` | Optional | Gets or sets Activity. |
| `work_area` | `string` | Optional | Gets or sets WorkArea. |
| `phone_business_1` | `string` | Optional | Gets or sets PhoneBusiness1. |
| `phone_business_2` | `string` | Optional | Gets or sets PhoneBusiness2. |
| `mobile_business` | `string` | Optional | Gets or sets MobileBusiness. |
| `e_mail_business` | `string` | Optional | Gets or sets EMailBusiness. |
| `fax_business` | `string` | Optional | Gets or sets FaxBusiness. |
| `information_business` | `string` | Optional | Gets or sets InformationBusiness. |
| `cost_center_id` | `string` | Optional | Gets or sets CostCenterId. |
| `phone` | `string` | Optional | Gets or sets Phone. |
| `mobile` | `string` | Optional | Gets or sets Mobile. |
| `e_mail` | `string` | Optional | Gets or sets EMail. |
| `fax` | `string` | Optional | Gets or sets Fax. |
| `city` | `string` | Optional | Gets or sets City. |
| `city_district` | `string` | Optional | Gets or sets CityDistrict. |
| `zip_code` | `string` | Optional | Gets or sets ZipCode. |
| `street` | `string` | Optional | Gets or sets Street. |
| `information` | `string` | Optional | Gets or sets Information. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `win_sped_user_id` | `string` | Optional | Gets or sets WinSpedUserId. |
| `signature_prefix` | `string` | Optional | Gets or sets SignaturePrefix. |
| `server_user` | `string` | Optional | Gets or sets ServerUser. |
| `server_password` | `string` | Optional | Gets or sets ServerPassword. |
| `date_of_birth` | `datetime` | Optional | Gets or sets DateOfBirth. |
| `serial_e_mail` | `int` | Optional | Gets or sets SerialEMail. |
| `tapi_line` | `string` | Optional | Gets or sets TapiLine. |
| `extended_fields` | [`LISPublicExtendedDataTableRecord`](../../doc/models/lis-public-extended-data-table-record.md) | Optional | This class represents a row within an extended table. Therefor it holds a<br>collection of {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtendedDataField}. |
| `country_code` | `string` | Optional | Gets or sets the country code. |
| `person_role` | [`PersonRoleEnum`](../../doc/models/person-role-enum.md) | Optional | Gets or sets the person role. |
| `is_updated` | `bool` | Optional | - |
| `is_deleted` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "transportTypes": [
    "transportTypes4",
    "transportTypes5"
  ],
  "customerContactPersonId": 114,
  "customerId": 114,
  "name": "name0",
  "forename": "forename8"
}
```

