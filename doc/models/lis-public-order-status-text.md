
# LIS Public Order Status Text

The LISOrderStatusText data contract.

## Structure

`LISPublicOrderStatusText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `status_id` | `int` | Optional | Gets or sets StatusId. |
| `text` | `string` | Optional | Gets or sets Text. |
| `unloading_report` | `bool` | Optional | Gets or sets UnloadingReport. |
| `manual` | `bool` | Optional | Gets or sets Manual. |
| `automatic` | `bool` | Optional | Gets or sets Automatic. |
| `status_event_id` | [`StatusEventId1Enum`](../../doc/models/status-event-id-1-enum.md) | Optional | Gets or sets StatusEventId. |
| `send_message` | `bool` | Optional | Gets or sets SendMessage. |
| `quality` | `bool` | Optional | Gets or sets Quality. |
| `email` | `string` | Optional | Gets or sets email. |
| `note_mandatory` | `int` | Optional | Gets or sets NoteMandatory. |
| `unique` | `int` | Optional | Gets or sets Unique. |
| `state` | `int` | Optional | Gets or sets State. |
| `punctuality_of_delivery` | `int` | Optional | Gets or sets PunctualityOfDelivery. |
| `event_location` | `int` | Optional | Gets or sets EventLocation. |
| `order_information_no` | `int` | Optional | Gets or sets OrderInformationNo. |
| `order_information_text_id` | `int` | Optional | Gets or sets OrderInformationTextId. |
| `status_write_only` | `string` | Optional | Gets or sets StatusWriteOnly. |
| `task_action` | `string` | Optional | Gets or sets TaskAction. |
| `allow_deletion` | [`AllowDeletionEnum`](../../doc/models/allow-deletion-enum.md) | Optional | Gets or sets AllowDeletion. |
| `employee_group_id` | `string` | Optional | Gets or sets EmployeeGroupId. |
| `additional_order_status_texts` | [`List of LISPublicAdditionalStatusText`](../../doc/models/lis-public-additional-status-text.md) | Optional | Gets or sets the additional order status texts. |
| `extended_status_text_fields` | [`List of LISPublicExtendedStatusTextField`](../../doc/models/lis-public-extended-status-text-field.md) | Optional | Gets or sets the additional order status texts. |
| `order_information_activity` | [`OrderInformationActivityEnum`](../../doc/models/order-information-activity-enum.md) | Optional | Gets or sets OrderInformationActivity. |
| `web_entry` | `int` | Optional | Gets or sets WebEntry. |
| `raise_alarm` | `int` | Optional | Gets or sets RaiseAlarm. |
| `shipping_unit_status_id` | `int` | Optional | Gets or sets ShippingUnitStatusId. |
| `additional_dossier_status_id` | `int` | Optional | Gets or sets the additional dossier status identifier. |
| `next_section` | `int` | Optional | Gets or sets NextSection. |
| `tour_information_no` | `int` | Optional | Gets or sets TourInformationNo. |
| `tour_information_text_id` | `int` | Optional | Gets or sets TourInformationTextId. |
| `tour_information_activity` | [`TourInformationActivityEnum`](../../doc/models/tour-information-activity-enum.md) | Optional | Gets or sets TourInformationActivity. |
| `status_category_id` | `string` | Optional | Gets or sets the status category id. |
| `macro` | `string` | Optional | Gets or sets the macro. |
| `execute_macro_or_script` | `bool` | Optional | Gets or sets the execute macro. |
| `macro_edi_sequence` | [`MacroEDISequenceEnum`](../../doc/models/macro-edi-sequence-enum.md) | Optional | Gets or sets the execute macro. |
| `no_date_time_proposel` | `bool` | Optional | Gets or sets a value indicating whether [no date time proposel]. |
| `script_id` | `string` | Optional | Gets or sets the script identifier. |
| `trigger_on` | [`TriggerOnEnum`](../../doc/models/trigger-on-enum.md) | Optional | Gets or sets the trigger on. |
| `service_order_template_id` | `int` | Optional | - |
| `transportation_unit_status_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8",
  "statusId": 250,
  "text": "text0",
  "unloadingReport": false
}
```

