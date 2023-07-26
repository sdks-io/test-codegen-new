
# LIS Public Additional Status Text

LISAdditionalStatusText

## Structure

`LISPublicAdditionalStatusText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_status_text_id` | `int` | Optional | Gets or sets the additional status text identifier. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `status_type` | [`StatusTypeEnum`](../../doc/models/status-type-enum.md) | Optional | Gets or sets the type of the status. |
| `status_nr` | `int` | Optional | Gets or sets the status nr. |
| `additional_status_type` | [`AdditionalStatusTypeEnum`](../../doc/models/additional-status-type-enum.md) | Optional | Gets or sets the type of the additional status. |
| `additional_status_nr` | `int` | Optional | Gets or sets the additional status nr. |
| `send_next` | `bool` | Optional | Gets or sets the send next. |

## Example (as JSON)

```json
{
  "additionalStatusTextId": 206,
  "changedOn": "2016-03-13T12:52:32.123Z",
  "changedBy": "changedBy8",
  "statusType": "DMS",
  "statusNr": 26
}
```

