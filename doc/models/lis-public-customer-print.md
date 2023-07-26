
# LIS Public Customer Print

The LISCustomerPrint data contract.

## Structure

`LISPublicCustomerPrint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets CustomerId. |
| `group` | `int` | Optional | Gets or sets Group. |
| `print_base` | `int` | Optional | Gets or sets PrintBase. |
| `print_name` | `string` | Optional | Gets or sets PrintName. |
| `contact_person_seq_no` | `int` | Optional | Gets or sets ContactPersonSeqNo. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `employee_seq_no` | `int` | Optional | Gets or sets EmployeeSeqNo. |
| `print_enabled` | `bool` | Optional | Gets or sets PrintOriginalEnabled. |
| `print_original_enabled` | `bool` | Optional | Gets or sets the print original enabled. |
| `print_copy_enabled` | `bool` | Optional | - |
| `fax_original_enabled` | `bool` | Optional | Gets or sets FaxOriginalEnabled. |
| `send_mail_original_enabled` | `bool` | Optional | Gets or sets SendMailOriginalEnabled. |
| `output_original_enabled` | `bool` | Optional | Gets or sets OutputOriginalEnabled. |
| `blank_template_enabled` | `bool` | Optional | Gets or sets BlankTemplateEnabled. |
| `number_of_copies` | `int` | Optional | Gets or sets NumberOfCopies. |
| `override_print` | `bool` | Optional | Gets or sets OverridePrint. |
| `dms_print_assigned` | `bool` | Optional | Gets or sets DMSPrintAssigned. |
| `mail_cc` | `int` | Optional | Gets or sets MailCC. |
| `mail_cc_text` | `string` | Optional | Gets or sets MailCCText. |
| `subject_number` | `int` | Optional | Gets or sets SubjectNumber. |
| `subject_text` | `string` | Optional | Gets or sets SubjectText. |
| `changed_by_user` | `bool` | Optional | Gets or sets a value indicating whether [changed by user]. |
| `track_changes` | `bool` | Optional | Gets or sets TrackChanges. |
| `has_changes` | `bool` | Optional | Gets or sets HasChanges. |
| `additional_print` | `string` | Optional | Gets or sets the additional print. |
| `additional_print_2` | `string` | Optional | Gets or sets the additional print 2. |
| `csv_view` | `string` | Optional | Gets or sets a value indicating whether [CSV view]. |
| `is_additional_print_created_by_repeat` | `bool` | Optional | Gets or sets the is additional print created by repeat. |
| `is_preview_document_enabled` | `bool` | Optional | Gets or sets a value indicating whether this instance is preview document enabled. |
| `is_mail_on_repeating_print_enabled` | `bool` | Optional | Gets or sets a value indicating whether this instance is mail on repeating print enabled. |
| `ordered_account` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "customerId": 114,
  "group": 182,
  "printBase": 240,
  "printName": "printName4",
  "contactPersonSeqNo": 102
}
```

