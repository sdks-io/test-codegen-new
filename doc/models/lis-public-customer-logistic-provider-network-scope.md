
# LIS Public Customer Logistic Provider Network Scope

The LISCustomerSystemTrafficScope data contract.

## Structure

`LISPublicCustomerLogisticProviderNetworkScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logistic_provider_networks` | [`List of LISPublicCustomerLogisticProviderNetwork`](../../doc/models/lis-public-customer-logistic-provider-network.md) | Optional | Gets or sets ShortTexts. |

## Example (as JSON)

```json
{
  "logisticProviderNetworks": [
    {
      "systemTrafficId": 200,
      "customerId": 116,
      "serviceProviderId": 58,
      "serviceId": 134,
      "lastImport": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

