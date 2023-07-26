
# LIS Public Extended Data Field

This class represents a column value (cell) within an {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtendedDataTable}.
Besides the schema information of the column it contains a specific data value.

## Structure

`LISPublicExtendedDataField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `object` | Optional | Gets or sets the value of the cell. |
| `original_value` | `object` | Optional | Gets or sets the original value. |
| `caption` | `string` | Optional | Gets or sets the caption. |
| `column_name` | `string` | Optional | Gets or sets the name of the column. |
| `data_type` | [`LISPublicExtendedFieldDataType`](../../doc/models/lis-public-extended-field-data-type.md) | Optional | This class describes the data type of a extended table column. |
| `is_key` | `bool` | Optional | Gets or sets a value indicating whether this instance is part of a primary key. |

## Example (as JSON)

```json
{
  "value": {
    "key1": "val1",
    "key2": "val2"
  },
  "originalValue": {
    "key1": "val1",
    "key2": "val2"
  },
  "caption": "caption4",
  "columnName": "columnName0",
  "dataType": {
    "lisDataType": "Date",
    "dataType": "dataType4",
    "maxLength": 112,
    "digits": 174
  }
}
```

