
# LIS Public Customer EDI Scope

The LISCustomerEDIScope data contract.

## Structure

`LISPublicCustomerEDIScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bordero_exchange_no` | `string` | Optional | Gets or sets BorderoExchangeNo. |
| `data_exchange_type` | [`DataExchangeTypeEnum`](../../doc/models/data-exchange-type-enum.md) | Optional | Gets or sets DataExchangeType. |
| `data_exchange_format` | [`DataExchangeFormatEnum`](../../doc/models/data-exchange-format-enum.md) | Optional | Gets or sets DataExchangeFormat. |
| `edi_customer_id` | `int` | Optional | Gets or sets EDICustomerId. |

## Example (as JSON)

```json
{
  "borderoExchangeNo": "borderoExchangeNo0",
  "dataExchangeType": "Email",
  "dataExchangeFormat": "IFTMIN",
  "ediCustomerId": 212
}
```

