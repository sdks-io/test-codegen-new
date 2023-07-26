
# LIS Response LIS Public Customer

The api response class.

## Structure

`LISResponseLISPublicCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicCustomer`](../../doc/models/lis-public-customer.md) | Optional | Represents a customer. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "contactPersonScope": {
      "contactPersons": [
        {
          "transportTypes": [
            "transportTypes4",
            "transportTypes5"
          ],
          "customerContactPersonId": 218,
          "customerId": 246,
          "name": "name0",
          "forename": "forename8"
        },
        {
          "transportTypes": [
            "transportTypes5",
            "transportTypes6",
            "transportTypes7"
          ],
          "customerContactPersonId": 219,
          "customerId": 247,
          "name": "name1",
          "forename": "forename9"
        },
        {
          "transportTypes": [
            "transportTypes6"
          ],
          "customerContactPersonId": 220,
          "customerId": 248,
          "name": "name2",
          "forename": "forename0"
        }
      ]
    },
    "shipmentScope": {
      "trafficModeId": "trafficModeId6",
      "logModelId": 36,
      "salesTaxId": "salesTaxId2",
      "currencyId": "currencyId8",
      "freightTermId": "freightTermId2"
    },
    "accountingScope": {
      "accountTableId": 18,
      "costUnitId": 254,
      "costCenter": 142,
      "finalConsumer": false,
      "taxIdNumber": "taxIdNumber6"
    },
    "textScope": {
      "shortTexts": [
        {
          "customerId": 202,
          "section": "Label",
          "function": "ServiceDescription",
          "changedOn": "2016-03-13T12:52:32.123Z",
          "changedBy": "changedBy2"
        },
        {
          "customerId": 203,
          "section": "CustomerTransfer",
          "function": "Credit",
          "changedOn": "2016-03-13T12:52:32.123Z",
          "changedBy": "changedBy3"
        },
        {
          "customerId": 204,
          "section": "CustomerEquipment",
          "function": "Invoice",
          "changedOn": "2016-03-13T12:52:32.123Z",
          "changedBy": "changedBy4"
        }
      ],
      "notice1": "notice16",
      "notice2": "notice22"
    },
    "loadingPointScope": {
      "name1": "name14",
      "name2": "name28",
      "name3": "name38",
      "address": {
        "addressId": 204,
        "locality": {
          "localityId": 62,
          "countryCode": "countryCode6",
          "zip": "zip4",
          "city": "city0",
          "cityDistrict": "cityDistrict0"
        },
        "street": "street0",
        "coordinate": {
          "longitude": 105.22,
          "latitude": 107.42
        },
        "changedOn": "2016-03-13T12:52:32.123Z"
      },
      "differingLoadingPoint": 232
    }
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

