
# LIS Public DMS Document

The document in the dms

## Structure

`LISPublicDMSDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_data` | `string` | Optional | Gets or sets the document data. |
| `file_extension` | `string` | Optional | Gets or sets the file extension. |
| `filename` | `string` | Optional | Gets or sets the filename. |
| `dms_document_id` | `int` | Optional | Gets or sets the DMS document id. |
| `archiv` | [`LISPublicDMSArchiv`](../../doc/models/lis-public-dms-archiv.md) | Optional | DMS Archiv |
| `folder` | [`LISPublicDMSFolder`](../../doc/models/lis-public-dms-folder.md) | Optional | DMS Folder |
| `doc_type` | [`LISPublicDMSDocType`](../../doc/models/lis-public-dms-doc-type.md) | Optional | Customer address data of accounts |
| `key_item_values` | [`List of LISPublicDMSDocumentKeyItemValue`](../../doc/models/lis-public-dms-document-key-item-value.md) | Optional | Gets or sets the key item values. |
| `description` | `string` | Optional | Gets or sets the description. |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Gets or sets the status. |
| `file_type` | [`FileTypeEnum`](../../doc/models/file-type-enum.md) | Optional | Gets or sets the type of the file. |
| `responsible_employee` | `string` | Optional | Gets or sets the responsible employee. |
| `responsible_employee_group` | `string` | Optional | Gets or sets the responsible employee group. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |

## Example (as JSON)

```json
{
  "documentData": "documentData4",
  "fileExtension": "fileExtension4",
  "filename": "filename2",
  "dmsDocumentId": 90,
  "archiv": {
    "dmsArchivId": 204,
    "archivName": "archivName6",
    "archivType": "Template",
    "createdBy": "createdBy4",
    "createdOn": "2016-03-13T12:52:32.123Z"
  }
}
```

