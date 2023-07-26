
# LIS Response LIS Public DMS Document

The api response class.

## Structure

`LISResponseLISPublicDMSDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicDMSDocument`](../../doc/models/lis-public-dms-document.md) | Optional | The document in the dms |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "documentData": "documentData8",
    "fileExtension": "fileExtension8",
    "filename": "filename4",
    "dmsDocumentId": 78,
    "archiv": {
      "dmsArchivId": 216,
      "archivName": "archivName6",
      "archivType": "Template",
      "createdBy": "createdBy8",
      "createdOn": "2016-03-13T12:52:32.123Z"
    }
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

