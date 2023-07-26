
# LIS Public DMS Doc Type

Customer address data of accounts

## Structure

`LISPublicDMSDocType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dms_doc_type_id` | `int` | Optional | Gets or sets the DMS doc type id. |
| `doc_type_name` | `string` | Optional | Gets or sets the name of the doc type. |
| `send_mails_only_to_contact_persons` | `bool` | Optional | Gets or sets a value indicating whether [send mails only to contact persons]. |
| `status_id` | `int` | Optional | Gets or sets the status identifier. |
| `doc_type_key_items` | [`List of LISPublicDMSDocTypeKeyItem`](../../doc/models/lis-public-dms-doc-type-key-item.md) | Optional | Gets or sets the doc type key items. |
| `auf_nr_search` | `bool` | Optional | Gets or sets a value indicating whether [auf nr search]. |
| `no_db_archiv` | `bool` | Optional | Gets or sets a value indicating whether [no database archiv]. |
| `keep_while_delete_company_data` | `bool` | Optional | Gets or sets a value indicating whether [keep while delete company data]. |
| `no_doc_to_pdf` | `bool` | Optional | Gets or sets a value indicating whether [no document to PDF]. |
| `mandatory_type` | [`MandatoryTypeEnum`](../../doc/models/mandatory-type-enum.md) | Optional | Gets or sets a value indicating whether [mandatory document]. |
| `related_folder_id` | `int` | Optional | Gets or sets the related folder identifier. |
| `related_archive_id` | `int` | Optional | Gets or sets the related archive identifier. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |

## Example (as JSON)

```json
{
  "dmsDocTypeId": 232,
  "docTypeName": "docTypeName2",
  "sendMailsOnlyToContactPersons": false,
  "statusId": 250,
  "docTypeKeyItems": [
    {
      "dmsDocTypeKeyItemId": 147,
      "required": true,
      "dmsDocTypeKeyItemName": "dmsDocTypeKeyItemName5",
      "dmsDocTypeSbINR": 247,
      "lfdNr": 37
    },
    {
      "dmsDocTypeKeyItemId": 148,
      "required": false,
      "dmsDocTypeKeyItemName": "dmsDocTypeKeyItemName6",
      "dmsDocTypeSbINR": 246,
      "lfdNr": 38
    }
  ]
}
```

