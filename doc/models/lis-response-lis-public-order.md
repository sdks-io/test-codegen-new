
# LIS Response LIS Public Order

The api response class.

## Structure

`LISResponseLISPublicOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation_result` | [`LISPublicOrder`](../../doc/models/lis-public-order.md) | Optional | This class represents the public order object. |
| `message` | `List of string` | Optional | The message. |

## Example (as JSON)

```json
{
  "operationResult": {
    "aggregates": {
      "weight": 218.84,
      "chargeableWeight": 37.82,
      "cubicDecimeter": 191.58,
      "loadingMeter": 104.36,
      "squareMeter": 39.94
    },
    "addresses": [
      {
        "customerId": 68,
        "contactPersonId": 104,
        "addressType": "FinalRecipient"
      },
      {
        "customerId": 69,
        "contactPersonId": 105,
        "addressType": "DestinationForwarder"
      }
    ],
    "addressRoles": [
      {
        "orderId": 226,
        "sequentialNo": 220,
        "changedOn": "2016-03-13T12:52:32.123Z",
        "changedBy": "changedBy4",
        "customerId": 174
      },
      {
        "orderId": 227,
        "sequentialNo": 219,
        "changedOn": "2016-03-13T12:52:32.123Z",
        "changedBy": "changedBy5",
        "customerId": 175
      }
    ],
    "details": [
      {
        "units": [
          {
            "unitType": "Package",
            "unitId": "unitId8",
            "quantity": 17.52,
            "createdOn": "2016-03-13T12:52:32.123Z",
            "createdBy": "createdBy4"
          },
          {
            "unitType": "Quantity",
            "unitId": "unitId9",
            "quantity": 17.53,
            "createdOn": "2016-03-13T12:52:32.123Z",
            "createdBy": "createdBy5"
          }
        ],
        "orderId": 43,
        "detailId": 127,
        "reference": "reference3",
        "content": "content1"
      },
      {
        "units": [
          {
            "unitType": "Quantity",
            "unitId": "unitId9",
            "quantity": 17.53,
            "createdOn": "2016-03-13T12:52:32.123Z",
            "createdBy": "createdBy5"
          },
          {
            "unitType": "All",
            "unitId": "unitId0",
            "quantity": 17.54,
            "createdOn": "2016-03-13T12:52:32.123Z",
            "createdBy": "createdBy6"
          },
          {
            "unitType": "Unkown",
            "unitId": "unitId1",
            "quantity": 17.55,
            "createdOn": "2016-03-13T12:52:32.123Z",
            "createdBy": "createdBy7"
          }
        ],
        "orderId": 44,
        "detailId": 128,
        "reference": "reference4",
        "content": "content2"
      },
      {
        "units": [
          {
            "unitType": "All",
            "unitId": "unitId0",
            "quantity": 17.54,
            "createdOn": "2016-03-13T12:52:32.123Z",
            "createdBy": "createdBy6"
          }
        ],
        "orderId": 45,
        "detailId": 129,
        "reference": "reference5",
        "content": "content3"
      }
    ],
    "appointments": [
      {
        "appointmentType": "Original",
        "loadingType": "Loading",
        "dateFrom": "2016-03-13T12:52:32.123Z",
        "timeFrom": "2016-03-13T12:52:32.123Z",
        "dateTill": "2016-03-13T12:52:32.123Z"
      },
      {
        "appointmentType": "DispatchCalculated",
        "loadingType": "Delivery",
        "dateFrom": "2016-03-13T12:52:32.123Z",
        "timeFrom": "2016-03-13T12:52:32.123Z",
        "dateTill": "2016-03-13T12:52:32.123Z"
      }
    ]
  },
  "message": [
    "message0",
    "message1",
    "message2"
  ]
}
```

