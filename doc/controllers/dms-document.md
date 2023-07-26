# DMS Document

```python
dms_document_controller = client.dms_document
```

## Class Name

`DMSDocumentController`

## Methods

* [Get Document Data](../../doc/controllers/dms-document.md#get-document-data)
* [Get Documents](../../doc/controllers/dms-document.md#get-documents)


# Get Document Data

Get DMS document selection

```python
def get_document_data(self,
                     document_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_id` | `int` | Query, Required | The request. |

## Response Type

[`LISResponseLISPublicDMSDocument`](../../doc/models/lis-response-lis-public-dms-document.md)

## Example Usage

```python
document_id = 48

result = dms_document_controller.get_document_data(document_id)
print(result)
```


# Get Documents

Get DMS document selection. Example Request http://{{ServerAddress}}/DMSDocument/Documents?KeyValues=[{"KeyItemName":"AufIntNr","KeyItemValue":"653"}]

```python
def get_documents(self,
                 key_values,
                 document_id=None,
                 dms_archiv=None,
                 dms_folder=None,
                 dms_doc_types=None,
                 document_desc=None,
                 state=None,
                 file_type=None,
                 created_on_from=None,
                 created_on_to=None,
                 key_item_linkage=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key_values` | `string` | Query, Required | Request for DMS Documents Example value: [{"KeyItemName":"AufIntNr","KeyItemValue":"653"}] |
| `document_id` | `int` | Query, Optional | Request for DMS Documents |
| `dms_archiv` | `string` | Query, Optional | Request for DMS Documents |
| `dms_folder` | `string` | Query, Optional | Request for DMS Documents |
| `dms_doc_types` | `List of string` | Query, Optional | Request for DMS Documents |
| `document_desc` | `string` | Query, Optional | Request for DMS Documents |
| `state` | [`State3Enum`](../../doc/models/state-3-enum.md) | Query, Optional | Request for DMS Documents |
| `file_type` | [`FileType1Enum`](../../doc/models/file-type-1-enum.md) | Query, Optional | Request for DMS Documents |
| `created_on_from` | `datetime` | Query, Optional | Request for DMS Documents |
| `created_on_to` | `datetime` | Query, Optional | Request for DMS Documents |
| `key_item_linkage` | [`KeyItemLinkageEnum`](../../doc/models/key-item-linkage-enum.md) | Query, Optional | Request for DMS Documents |

## Response Type

[`LISResponseListLISPublicDMSDocumentMeta`](../../doc/models/lis-response-list-lis-public-dms-document-meta.md)

## Example Usage

```python
key_values = 'KeyValues4'

result = dms_document_controller.get_documents(key_values)
print(result)
```

