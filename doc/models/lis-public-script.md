
# LIS Public Script

This class represents a script that can be used for execution.

## Structure

`LISPublicScript`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `script_id` | `string` | Optional | The script identifier (GUID). |
| `script_name` | `string` | Optional | The name of the script. |
| `event_type` | [`EventTypeEnum`](../../doc/models/event-type-enum.md) | Optional | The event type. |
| `implementation_type` | `string` | Optional | The implementation type. |
| `python_code` | `string` | Optional | The executable python code of the script. |
| `sub_scripts` | [`List of LISPublicScript`](../../doc/models/lis-public-script.md) | Optional | A list of sub scripts. |

## Example (as JSON)

```json
{
  "scriptId": "scriptId6",
  "scriptName": "scriptName4",
  "eventType": "NotSet",
  "implementationType": "implementationType0",
  "pythonCode": "pythonCode4"
}
```

