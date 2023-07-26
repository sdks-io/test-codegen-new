
# LIS Public Customer

Represents a customer.

## Structure

`LISPublicCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_person_scope` | [`LISPublicCustomerContactPersonScope`](../../doc/models/lis-public-customer-contact-person-scope.md) | Optional | The LISCustomerContactPersonScope data contract. |
| `shipment_scope` | [`LISPublicCustomerShipmentScope`](../../doc/models/lis-public-customer-shipment-scope.md) | Optional | The LISCustomerShipmentScope data contract. |
| `accounting_scope` | [`LISPublicCustomerAccountingScope`](../../doc/models/lis-public-customer-accounting-scope.md) | Optional | The LISCustomerAccountingScope data contract. |
| `text_scope` | [`LISPublicCustomerTextScope`](../../doc/models/lis-public-customer-text-scope.md) | Optional | The LISCustomerTextScope data contract. |
| `loading_point_scope` | [`LISPublicCustomerLoadingPointScope`](../../doc/models/lis-public-customer-loading-point-scope.md) | Optional | The LISCustomerLoadingPointScope data contract. |
| `time_scope` | [`LISPublicCustomerTimeScope`](../../doc/models/lis-public-customer-time-scope.md) | Optional | The LISCustomerTimeScope data contract. |
| `contact_scope` | [`LISPublicCustomerContactScope`](../../doc/models/lis-public-customer-contact-scope.md) | Optional | The LISCustomerContactScope data contract. |
| `additional_addresses_scope` | [`LISPublicCustomerAdditionalAddressesScope`](../../doc/models/lis-public-customer-additional-addresses-scope.md) | Optional | The LISCustomerAdditionalAddressesScope data contract. |
| `calculation_scope` | [`LISPublicCustomerCalculationScope`](../../doc/models/lis-public-customer-calculation-scope.md) | Optional | The LISCustomerCalculationScope data contract. |
| `invoicing_scope` | [`LISPublicCustomerInvoicingScope`](../../doc/models/lis-public-customer-invoicing-scope.md) | Optional | The LISCustomerInvoicingScope data contract. |
| `voucher_printing_scope` | [`LISPublicCustomerVoucherPrintingScope`](../../doc/models/lis-public-customer-voucher-printing-scope.md) | Optional | The LISCustomerVoucherPrintingScope data contract. |
| `additional_info_scope` | [`LISPublicCustomerAdditionalInfoScope`](../../doc/models/lis-public-customer-additional-info-scope.md) | Optional | The LISCustomerAdditionalInfoScope data contract. |
| `edi_scope` | [`LISPublicCustomerEDIScope`](../../doc/models/lis-public-customer-edi-scope.md) | Optional | The LISCustomerEDIScope data contract. |
| `disposition_scope` | [`LISPublicCustomerDispositionScope`](../../doc/models/lis-public-customer-disposition-scope.md) | Optional | The LISCustomerDispositionScope data contract. |
| `customs_scope` | [`LISPublicCustomerCustomsScope`](../../doc/models/lis-public-customer-customs-scope.md) | Optional | The LISCustomerCustomsScope data contract. |
| `criterion_scope` | [`LISPublicCustomerCriterionScope`](../../doc/models/lis-public-customer-criterion-scope.md) | Optional | The LISCustomerCriterionScope data contract. |
| `loading_devices_scope` | [`LISPublicCustomerLoadingDevicesScope`](../../doc/models/lis-public-customer-loading-devices-scope.md) | Optional | The LISCustomerLoadingDevicesScope data contract. |
| `group_booking_scope` | [`LISPublicCustomerGroupBookingScope`](../../doc/models/lis-public-customer-group-booking-scope.md) | Optional | The LISCustomerGroupBookingScope data contract. |
| `calculation_basis_scope` | [`LISPublicCustomerCalculationBasisScope`](../../doc/models/lis-public-customer-calculation-basis-scope.md) | Optional | The LISCustomerCalculationBasisScope data contract. |
| `account_manager_scope` | [`LISPublicCustomerAccountManagerScope`](../../doc/models/lis-public-customer-account-manager-scope.md) | Optional | The LISCustomerAccountManagerScope data contract. |
| `outdated_fields_scope` | [`LISPublicCustomerOutdatedFieldsScope`](../../doc/models/lis-public-customer-outdated-fields-scope.md) | Optional | The LISCustomerOutdatedFieldsScope data contract. |
| `extended_fields_scope` | [`LISPublicCustomerExtendedFieldsScope`](../../doc/models/lis-public-customer-extended-fields-scope.md) | Optional | LISCustomerExtendedFieldsScope data contract. |
| `hazardous_goods_scope` | [`LISPublicCustomerHazardousGoodsScope`](../../doc/models/lis-public-customer-hazardous-goods-scope.md) | Optional | LISCustomerHazardousGoodsScope |
| `addressable_print_scope` | [`LISPublicCustomerAddressablePrintScope`](../../doc/models/lis-public-customer-addressable-print-scope.md) | Optional | The LISCustomerAddressablePrintScope data contract. |
| `slip_fees_scope` | [`LISPublicCustomerSlipFeesScope`](../../doc/models/lis-public-customer-slip-fees-scope.md) | Optional | The LISCustomerSlipFeesScope data contract. |
| `identification_scope` | [`LISPublicCustomerIdentificationScope`](../../doc/models/lis-public-customer-identification-scope.md) | Optional | The LISCustomerIdentificationScope data contract. |
| `logistic_provider_network_scope` | [`LISPublicCustomerLogisticProviderNetworkScope`](../../doc/models/lis-public-customer-logistic-provider-network-scope.md) | Optional | The LISCustomerSystemTrafficScope data contract. |
| `mdm_scope` | [`LISPublicCustomerMDMScope`](../../doc/models/lis-public-customer-mdm-scope.md) | Optional | The LISCustomerMDMScope data contract. |
| `customer_id` | `int` | Optional | Gets or sets the customer id. |
| `created_by` | `string` | Optional | Gets or sets the date the item was created. |
| `created_on` | `datetime` | Optional | Gets or sets the name of the user that created this item. |
| `changed_by` | `string` | Optional | Gets or sets the name of the user that made the last change to this item. |
| `changed_on` | `datetime` | Optional | Gets or sets the date of the last change to this item. |
| `customer_short` | `string` | Optional | Gets or sets the customer short. |
| `name_1` | `string` | Optional | Gets or sets the name1. |
| `name_2` | `string` | Optional | Gets or sets the name2. |
| `name_3` | `string` | Optional | Gets or sets the name3. |
| `customer_type` | [`CustomerTypeEnum`](../../doc/models/customer-type-enum.md) | Optional | Gets or sets the type of the customer. |
| `address` | [`LISPublicCustomerAddress`](../../doc/models/lis-public-customer-address.md) | Optional | Represents a customer address. |
| `extended_address_id` | `string` | Optional | Gets or sets the extended address id. |
| `blocked_from_date` | `datetime` | Optional | Gets or sets the blocked from date. |
| `mdm_debit_state` | [`MdmDebitStateEnum`](../../doc/models/mdm-debit-state-enum.md) | Optional | Gets or sets the state of the MDM debit. |
| `mdm_credit_state` | [`MdmCreditStateEnum`](../../doc/models/mdm-credit-state-enum.md) | Optional | Gets or sets the state of the MDM credit. |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "contactPersonScope": {
    "contactPersons": [
      {
        "transportTypes": [
          "transportTypes8",
          "transportTypes9"
        ],
        "customerContactPersonId": 126,
        "customerId": 154,
        "name": "name4",
        "forename": "forename2"
      },
      {
        "transportTypes": [
          "transportTypes9",
          "transportTypes0",
          "transportTypes1"
        ],
        "customerContactPersonId": 127,
        "customerId": 155,
        "name": "name5",
        "forename": "forename3"
      },
      {
        "transportTypes": [
          "transportTypes0"
        ],
        "customerContactPersonId": 128,
        "customerId": 156,
        "name": "name6",
        "forename": "forename4"
      }
    ]
  },
  "shipmentScope": {
    "trafficModeId": "trafficModeId4",
    "logModelId": 208,
    "salesTaxId": "salesTaxId0",
    "currencyId": "currencyId6",
    "freightTermId": "freightTermId0"
  },
  "accountingScope": {
    "accountTableId": 30,
    "costUnitId": 10,
    "costCenter": 154,
    "finalConsumer": false,
    "taxIdNumber": "taxIdNumber6"
  },
  "textScope": {
    "shortTexts": [
      {
        "customerId": 38,
        "section": "Label",
        "function": "Agreement",
        "changedOn": "2016-03-13T12:52:32.123Z",
        "changedBy": "changedBy2"
      }
    ],
    "notice1": "notice18",
    "notice2": "notice22"
  },
  "loadingPointScope": {
    "name1": "name12",
    "name2": "name26",
    "name3": "name36",
    "address": {
      "addressId": 216,
      "locality": {
        "localityId": 74,
        "countryCode": "countryCode4",
        "zip": "zip2",
        "city": "city8",
        "cityDistrict": "cityDistrict8"
      },
      "street": "street8",
      "coordinate": {
        "longitude": 18.3,
        "latitude": 20.5
      },
      "changedOn": "2016-03-13T12:52:32.123Z"
    },
    "differingLoadingPoint": 12
  }
}
```

