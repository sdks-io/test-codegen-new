
# LIS Public Extended Data Table Record

This class represents a row within an extended table. Therefor it holds a
collection of {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtendedDataField}.

## Structure

`LISPublicExtendedDataTableRecord`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `table` | [`LISPublicExtendedTable`](../../doc/models/lis-public-extended-table.md) | Optional | LISExtendedTable class. |
| `primary_key` | [`List of LISPublicExtendedDataField`](../../doc/models/lis-public-extended-data-field.md) | Optional | Gets the primary key. It is delivered as a list as the pk may consist of<br>more than one column. |
| `fields` | [`List of LISPublicExtendedDataField`](../../doc/models/lis-public-extended-data-field.md) | Optional | Gets or sets the data fields of this row. |

## Example (as JSON)

```json
{
  "table": {
    "baseTableName": "baseTableName4",
    "extendedTableName": "extendedTableName0"
  },
  "primaryKey": [
    {
      "value": {
        "key1": "val1",
        "key2": "val2"
      },
      "originalValue": {
        "key1": "val1",
        "key2": "val2"
      },
      "caption": "caption9",
      "columnName": "columnName5",
      "dataType": {
        "lisDataType": "Double",
        "dataType": "dataType9",
        "maxLength": 107,
        "digits": 169
      }
    }
  ],
  "fields": [
    {
      "value": {
        "key1": "val1",
        "key2": "val2"
      },
      "originalValue": {
        "key1": "val1",
        "key2": "val2"
      },
      "caption": "caption6",
      "columnName": "columnName2",
      "dataType": {
        "lisDataType": "Double",
        "dataType": "dataType6",
        "maxLength": 0,
        "digits": 194
      }
    },
    {
      "value": {
        "key1": "val1",
        "key2": "val2"
      },
      "originalValue": {
        "key1": "val1",
        "key2": "val2"
      },
      "caption": "caption7",
      "columnName": "columnName3",
      "dataType": {
        "lisDataType": "Decimal",
        "dataType": "dataType7",
        "maxLength": 1,
        "digits": 195
      }
    }
  ]
}
```

