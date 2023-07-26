
# LIS Public DMS Folder

DMS Folder

## Structure

`LISPublicDMSFolder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dms_folder_id` | `int` | Optional | Gets or sets the DMS folder id. |
| `folder_name` | `string` | Optional | Gets or sets the name of the folder. |
| `folder_type` | [`FolderTypeEnum`](../../doc/models/folder-type-enum.md) | Optional | Gets or sets the type of the folder. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |

## Example (as JSON)

```json
{
  "dmsFolderId": 216,
  "folderName": "folderName8",
  "folderType": "NotSet",
  "createdBy": "createdBy2",
  "createdOn": "2016-03-13T12:52:32.123Z"
}
```

