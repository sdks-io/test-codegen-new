
# LIS Public Customer Addressable Print Scope

The LISCustomerAddressablePrintScope data contract.

## Structure

`LISPublicCustomerAddressablePrintScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_prints` | [`List of LISPublicCustomerPrint`](../../doc/models/lis-public-customer-print.md) | Optional | Gets or sets CustomerPrints. |

## Example (as JSON)

```json
{
  "customerPrints": [
    {
      "customerId": 51,
      "group": 91,
      "printBase": 149,
      "printName": "printName7",
      "contactPersonSeqNo": 11
    }
  ]
}
```

