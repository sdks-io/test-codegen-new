
# LIS Public Script Info

This class contains meta information about a script.

## Structure

`LISPublicScriptInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `script_id` | `string` | Optional | The script identifier (GUID). |
| `script_name` | `string` | Optional | The name of the script. |
| `script_comment` | `string` | Optional | A description of the script. |
| `event_type` | [`EventTypeEnum`](../../doc/models/event-type-enum.md) | Optional | The event type. |
| `implementation_type` | `string` | Optional | The implementation type. |
| `product` | [`ProductEnum`](../../doc/models/product-enum.md) | Optional | The product. |
| `external_key` | `string` | Optional | The external key. |

## Example (as JSON)

```json
{
  "scriptId": "scriptId6",
  "scriptName": "scriptName4",
  "scriptComment": "scriptComment4",
  "eventType": "NotSet",
  "implementationType": "implementationType0"
}
```

