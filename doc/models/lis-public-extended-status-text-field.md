
# LIS Public Extended Status Text Field

Extended status text field for status events

## Structure

`LISPublicExtendedStatusTextField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_text_ext_field_id` | `int` | Optional | Gets or sets the status text ext field identifier. |
| `status_text_typ` | [`StatusTextTypEnum`](../../doc/models/status-text-typ-enum.md) | Optional | Gets or sets the status text typ. |
| `status_no` | `int` | Optional | Gets or sets the status no. |
| `extended_field_name` | `string` | Optional | Gets or sets the name of the extended field. |
| `is_required_field` | `bool` | Optional | Gets or sets a value indicating whether this instance is required field. |
| `set_status_remark` | `bool` | Optional | Gets or sets a value indicating whether [set status remark]. |

## Example (as JSON)

```json
{
  "statusTextExtFieldId": 12,
  "statusTextTyp": "DMS",
  "statusNo": 206,
  "extendedFieldName": "extendedFieldName6",
  "isRequiredField": false
}
```

