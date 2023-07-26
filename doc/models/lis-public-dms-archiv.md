
# LIS Public DMS Archiv

DMS Archiv

## Structure

`LISPublicDMSArchiv`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dms_archiv_id` | `int` | Optional | Gets or sets the DMS archiv id. |
| `archiv_name` | `string` | Optional | Gets or sets the name of the archiv. |
| `archiv_type` | [`ArchivTypeEnum`](../../doc/models/archiv-type-enum.md) | Optional | Gets or sets the type of the archiv. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |

## Example (as JSON)

```json
{
  "dmsArchivId": 228,
  "archivName": "archivName0",
  "archivType": "Archiv",
  "createdBy": "createdBy2",
  "createdOn": "2016-03-13T12:52:32.123Z"
}
```

