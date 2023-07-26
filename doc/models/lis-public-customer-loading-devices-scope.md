
# LIS Public Customer Loading Devices Scope

The LISCustomerLoadingDevicesScope data contract.

## Structure

`LISPublicCustomerLoadingDevicesScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ledger_account` | `bool` | Optional | Gets or sets LedgerAccount. |
| `reminder` | `bool` | Optional | Gets or sets Reminder. |
| `is_edi_receiver` | `bool` | Optional | Gets or sets IDEReceiver. |
| `print_schedule` | `bool` | Optional | Gets or sets PrintSchedule. |
| `mprint` | `bool` | Optional | Gets or sets Print. |
| `print_positive` | `bool` | Optional | Gets or sets PrintPositiv. |
| `reminder_date` | `int` | Optional | Gets or sets ReminderDate. |
| `days_return` | `int` | Optional | Gets or sets DaysReturn. |
| `print_invoice` | [`PrintInvoiceEnum`](../../doc/models/print-invoice-enum.md) | Optional | Gets or sets PrintInvoice. |
| `group` | `string` | Optional | Gets or sets Group. |
| `account_number` | `int` | Optional | Gets or sets AccountNumber. |
| `crediting_account` | [`CreditingAccountEnum`](../../doc/models/crediting-account-enum.md) | Optional | Gets or sets CreditingAccount. |
| `debiting_account` | [`DebitingAccountEnum`](../../doc/models/debiting-account-enum.md) | Optional | Gets or sets DebitingAccount. |
| `skip_statistic` | `bool` | Optional | Gets or sets SkipStatistic. |
| `ledger_account_sales_tax_id` | `string` | Optional | Gets or sets UCCode. |
| `account_table` | `int` | Optional | Gets or sets AccountTable. |
| `crediting_booking` | `bool` | Optional | Gets or sets CreditingBooking. |
| `auto_print_special_invoice` | `bool` | Optional | Gets or sets AutoPrintSpecialInvoice. |
| `lock_booking` | `bool` | Optional | Gets or sets LockBooking. |
| `is_transshipment_point` | `bool` | Optional | Gets or sets a value indicating whether this instance is transshipment point. |
| `compensation_units_account_from` | `List of string` | Optional | Gets or sets the compensation units account from. |
| `compensation_units_account_to` | `List of string` | Optional | Gets or sets the compensation units account to. |

## Example (as JSON)

```json
{
  "ledgerAccount": false,
  "reminder": false,
  "isEDIReceiver": false,
  "printSchedule": false,
  "print": false
}
```

