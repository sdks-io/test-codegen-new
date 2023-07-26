
# LIS Response List LIS Public DMS Document Meta

The api response class.

## Structure

`LISResponseListLISPublicDMSDocumentMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`List of LISPublicDMSDocumentMeta`](../../doc/models/lis-public-dms-document-meta.md) | Optional | The operation result. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": [
    {
      "documentId": 86,
      "status": 46,
      "archivName": "archivName6",
      "folderName": "folderName4",
      "docTypeName": "docTypeName8"
    }
  ],
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

