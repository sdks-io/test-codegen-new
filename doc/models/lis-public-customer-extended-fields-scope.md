
# LIS Public Customer Extended Fields Scope

LISCustomerExtendedFieldsScope data contract.

## Structure

`LISPublicCustomerExtendedFieldsScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extended_fields` | [`LISPublicExtendedDataTableRecord`](../../doc/models/lis-public-extended-data-table-record.md) | Optional | This class represents a row within an extended table. Therefor it holds a<br>collection of {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtendedDataField}. |

## Example (as JSON)

```json
{
  "extendedFields": {
    "table": {
      "baseTableName": "baseTableName0",
      "extendedTableName": "extendedTableName6"
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
        "caption": "caption7",
        "columnName": "columnName3",
        "dataType": {
          "lisDataType": "Unsupported",
          "dataType": "dataType7",
          "maxLength": 215,
          "digits": 153
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
        "caption": "caption8",
        "columnName": "columnName4",
        "dataType": {
          "lisDataType": "Int32",
          "dataType": "dataType8",
          "maxLength": 216,
          "digits": 154
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
        "caption": "caption9",
        "columnName": "columnName5",
        "dataType": {
          "lisDataType": "Date",
          "dataType": "dataType9",
          "maxLength": 217,
          "digits": 155
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
        "caption": "caption4",
        "columnName": "columnName0",
        "dataType": {
          "lisDataType": "Unsupported",
          "dataType": "dataType4",
          "maxLength": 66,
          "digits": 4
        }
      }
    ]
  }
}
```

