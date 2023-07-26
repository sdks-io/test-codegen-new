
# LIS Public Extended Field Data Type

This class describes the data type of a extended table column.

## Structure

`LISPublicExtendedFieldDataType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lis_data_type` | [`LisDataTypeEnum`](../../doc/models/lis-data-type-enum.md) | Optional | Gets or sets the LIS data type of this instance represents. |
| `data_type` | `string` | Optional | Gets or sets the CLR type that this instance represents. |
| `max_length` | `int` | Optional | Gets or sets the max length of the field value. |
| `digits` | `int` | Optional | Gets or sets the digits of the field value if field type is numeric. otherwise 0. |

## Example (as JSON)

```json
{
  "lisDataType": "Currency",
  "dataType": "dataType2",
  "maxLength": 126,
  "digits": 188
}
```

