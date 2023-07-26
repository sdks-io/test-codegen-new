
# LIS Public User Print Settings

LISPrintCommandOverrids

## Structure

`LISPublicUserPrintSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dms_attach_docs` | `int` | Optional | - |
| `skip_dms_docs_merge` | `bool` | Optional | - |
| `skip_send_mail` | `bool` | Optional | - |
| `skip_post_actions` | `bool` | Optional | - |
| `print_original_document` | `bool` | Optional | - |
| `preview_only` | `bool` | Optional | - |
| `skip_preview` | `bool` | Optional | - |
| `printer_name` | `string` | Optional | - |
| `execute_post_actions` | `bool` | Optional | - |
| `skip_group_selection` | `bool` | Optional | - |
| `skip_print_original` | `bool` | Optional | - |
| `create_stream_only` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "dmsAttachDocs": 156,
  "skipDMSDocsMerge": false,
  "skipSendMail": false,
  "skipPostActions": false,
  "printOriginalDocument": false
}
```

