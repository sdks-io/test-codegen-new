
# LIS Public Print Request

## Structure

`LISPublicPrintRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `print_job_id` | `int` | Optional | - |
| `selection_field_string` | `string` | Optional | - |
| `selection_condition_ansi` | `string` | Optional | - |
| `selection_condition_cr` | `string` | Optional | - |
| `additional_constraint_ansi` | `string` | Optional | - |
| `additional_constraint_cr` | `string` | Optional | - |
| `has_additional_constraint` | `bool` | Optional | - |
| `ignore_empty_selection` | `bool` | Optional | - |
| `invoicing_preview_request` | [`LISPublicInvoicingPreviewRequest`](../../doc/models/lis-public-invoicing-preview-request.md) | Optional | - |
| `is_custom_print` | `bool` | Optional | - |
| `report_group_id` | `int` | Optional | - |
| `form_type` | `int` | Optional | - |
| `has_form_type` | `bool` | Optional | - |
| `form_sub_type` | `int` | Optional | - |
| `has_form_sub_type` | `bool` | Optional | - |
| `modify_type` | `int` | Optional | - |
| `has_modify_type` | `bool` | Optional | - |
| `print_description` | `string` | Optional | - |
| `selection_field_type` | [`SelectionFieldTypeEnum`](../../doc/models/selection-field-type-enum.md) | Optional | - |
| `selection_value_list` | `List of int` | Optional | - |
| `custom_print_name` | `string` | Optional | - |
| `custom_print_base` | [`CustomPrintBaseEnum`](../../doc/models/custom-print-base-enum.md) | Optional | - |
| `formula_list` | `dict` | Optional | - |
| `print_action` | [`PrintActionEnum`](../../doc/models/print-action-enum.md) | Optional | - |
| `language_id` | `int` | Optional | - |
| `tables_to_replace` | `dict` | Optional | - |
| `user_print_settings` | [`LISPublicUserPrintSettings`](../../doc/models/lis-public-user-print-settings.md) | Optional | LISPrintCommandOverrids |
| `need_to_compile_request` | `bool` | Optional | - |
| `pdf_byte_buffer_to_print` | `string` | Optional | - |
| `caller_context` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "printJobId": 158,
  "selectionFieldString": "selectionFieldString2",
  "selectionConditionANSI": "selectionConditionANSI0",
  "selectionConditionCR": "selectionConditionCR6",
  "additionalConstraintANSI": "additionalConstraintANSI4"
}
```

