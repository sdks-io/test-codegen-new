
# LIS Public Order

This class represents the public order object.

## Structure

`LISPublicOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregates` | [`LISPublicOrderAggregates`](../../doc/models/lis-public-order-aggregates.md) | Optional | The LIS Order aggregates. |
| `addresses` | [`List of LISPublicOrderAddressInformation`](../../doc/models/lis-public-order-address-information.md) | Optional | Gets or sets Addresses. |
| `address_roles` | [`List of LISPublicOrderAddressRole`](../../doc/models/lis-public-order-address-role.md) | Optional | Gets or sets AddressRoles. |
| `details` | [`List of LISPublicOrderDetail`](../../doc/models/lis-public-order-detail.md) | Optional | Gets or sets Details. |
| `appointments` | [`List of LISPublicOrderAppointment`](../../doc/models/lis-public-order-appointment.md) | Optional | Gets or sets Appointments. |
| `stations` | [`List of LISPublicShipmentStation`](../../doc/models/lis-public-shipment-station.md) | Optional | Gets or sets Stations. |
| `order_informations` | [`List of LISPublicOrderInformation`](../../doc/models/lis-public-order-information.md) | Optional | Gets or sets OrderInformations. |
| `fees` | [`List of LISPublicOrderFee`](../../doc/models/lis-public-order-fee.md) | Optional | Gets or sets Fees. |
| `additional_chargings` | [`List of LISPublicOrderAdditionalCharging`](../../doc/models/lis-public-order-additional-charging.md) | Optional | Gets or sets AdditionalChargings. |
| `cash_on_delivery` | [`LISPublicOrderCashOnDelivery`](../../doc/models/lis-public-order-cash-on-delivery.md) | Optional | The LISOrderCashOnDelivery data contract. |
| `invoice_department_id` | `int` | Optional | Gets or sets InvoiceDepartmentId. |
| `invoice_division_id` | `int` | Optional | Gets or sets InvoiceDivisionId. |
| `invoicing_indicator` | [`InvoicingIndicatorEnum`](../../doc/models/invoicing-indicator-enum.md) | Optional | Gets or sets InvoicingIndicator. |
| `cargo_insurance` | `bool` | Optional | Gets or sets CargoInsurance. |
| `bonus_lump_sum` | `float` | Optional | Gets or sets the bonus lumpsum. |
| `general_condition_customer_id` | `int` | Optional | Gets or sets GeneralConditionCustomerId. |
| `freight_term_id` | `string` | Optional | Gets or sets FreightTermId. |
| `freight_payer_condition_type` | [`FreightPayerConditionTypeEnum`](../../doc/models/freight-payer-condition-type-enum.md) | Optional | Gets or sets FreightPayerConditionType. |
| `freight_payer_main_carriage` | [`FreightPayerMainCarriageEnum`](../../doc/models/freight-payer-main-carriage-enum.md) | Optional | Gets or sets FreightPayerMainCarriage. |
| `freight_payer_sales_tax_code` | `string` | Optional | Gets or sets FreightPayerSalesTaxCode. |
| `is_cash_payment` | `bool` | Optional | Gets or sets IsCashPayment. |
| `is_freight_payer_invoicing_blocked` | `bool` | Optional | Gets or sets IsFreightPayerInvoicingBlocked. |
| `proceeds` | `float` | Optional | Gets or sets Proceeds. |
| `cost_unit_id` | `int` | Optional | Gets or sets CostUnitId. |
| `loading_relation_id` | `string` | Optional | Gets or sets LoadingRelationId. |
| `unloading_relation_id` | `string` | Optional | Gets or sets UnloadingRelationId. |
| `original_sender_relation_id` | `string` | Optional | Gets or sets OriginalSenderRelationId. |
| `final_recipient_relation_relation_id` | `string` | Optional | Gets or sets FinalRecipientRelationRelationId. |
| `short_texts` | [`List of LISPublicOrderShortText`](../../doc/models/lis-public-order-short-text.md) | Optional | Gets or sets ShortTexts. |
| `long_texts` | [`List of LISPublicOrderLongText`](../../doc/models/lis-public-order-long-text.md) | Optional | Gets or sets LongTexts. |
| `coded_texts` | [`List of LISPublicOrderCodedText`](../../doc/models/lis-public-order-coded-text.md) | Optional | Gets or sets CodedTexts. |
| `debit_form_type` | `int` | Optional | Gets or sets DebitFormType. |
| `exchange_rate_date` | `datetime` | Optional | Gets or sets the exchange rate date. |
| `debit_own_form_type` | `int` | Optional | Gets or sets DebitOwnFormType. |
| `cost_center` | `int` | Optional | Gets or sets CostCenter. |
| `account_table` | `int` | Optional | Gets or sets AccountTable. |
| `charge_number` | `string` | Optional | Gets or sets ChargeNumber. |
| `dsi_number` | `string` | Optional | Gets or sets DSINumber. |
| `loading_area_id` | `string` | Optional | Gets or sets LoadingAreaId. |
| `unloading_area_id` | `string` | Optional | Gets or sets UnloadingAreaId. |
| `route_info` | [`LISPublicRouteInfo`](../../doc/models/lis-public-route-info.md) | Optional | Only the basic route informations. |
| `additional_charging_no` | `int` | Optional | Gets or sets AdditionalChargingNo. |
| `base_order_id` | `int` | Optional | Gets or sets BaseOrderId. |
| `base_order_no` | `int` | Optional | Gets or sets BaseOrderNo. |
| `position_no` | `string` | Optional | Gets or sets PositionNo. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `created_by` | `string` | Optional | Gets or sets CreatedBy. |
| `created_on` | `datetime` | Optional | Gets or sets CreatedOn. |
| `company_id` | `int` | Optional | Gets or sets CompanyId. |
| `division_id` | `int` | Optional | Gets or sets DivisionId. |
| `department_id` | `int` | Optional | Gets or sets DepartmentId. |
| `sub_division_id` | `int` | Optional | Gets or sets SubDivisionId. |
| `sub_department_id` | `int` | Optional | Gets or sets SubDepartmentId. |
| `accounting_company` | `int` | Optional | Gets or sets AccountingCompany. |
| `accounting_division` | `int` | Optional | Gets or sets AccountingDivision. |
| `accounting_department` | `int` | Optional | Gets or sets AccountingDepartment. |
| `order_id` | `int` | Optional | Gets or sets OrderId. |
| `order_type` | [`OrderType2Enum`](../../doc/models/order-type-2-enum.md) | Optional | Gets or sets OrderType. |
| `delete_state` | [`DeleteStateEnum`](../../doc/models/delete-state-enum.md) | Optional | Gets or sets DeleteState. |
| `original_order_type` | [`OriginalOrderTypeEnum`](../../doc/models/original-order-type-enum.md) | Optional | Gets or sets OriginalOrderType. |
| `order_input_type` | [`OrderInputType1Enum`](../../doc/models/order-input-type-1-enum.md) | Optional | Gets or sets OrderInputType. |
| `order_no` | `int` | Optional | Gets or sets OrderNo. |
| `order_sub_no` | `int` | Optional | Gets or sets OrderSubNo. |
| `order_date` | `datetime` | Optional | Gets or sets OrderDate. |
| `delivery_date` | `datetime` | Optional | Gets or sets DeliveryDate. |
| `order_text` | `string` | Optional | Gets or sets OrderText. |
| `picking_no` | `string` | Optional | Gets or sets PickingNo. |
| `reference_no` | `string` | Optional | Gets or sets ReferenceNo. |
| `delivery_no` | `string` | Optional | Gets or sets DeliveryNo. |
| `traffic_mode_id` | `string` | Optional | Gets or sets TrafficModeId. |
| `order_category` | `string` | Optional | Gets or sets OrderCategory. |
| `ld_booking_flag` | [`LdBookingFlagEnum`](../../doc/models/ld-booking-flag-enum.md) | Optional | Gets or sets LDBookingFlag. |
| `transportation_route_id` | `int` | Optional | Gets or sets TransportationRouteId. |
| `direct_delivery` | [`DirectDeliveryEnum`](../../doc/models/direct-delivery-enum.md) | Optional | Gets or sets DirectDelivery. |
| `debit_lump_sum` | [`List of LISPublicOrderLumpSum`](../../doc/models/lis-public-order-lump-sum.md) | Optional | Gets or sets the debit lump sum. |
| `credit_lump_sum` | [`List of LISPublicOrderLumpSum`](../../doc/models/lis-public-order-lump-sum.md) | Optional | Gets or sets the credit lump sum. |
| `extended_fields` | [`LISPublicExtendedDataTableRecord`](../../doc/models/lis-public-extended-data-table-record.md) | Optional | This class represents a row within an extended table. Therefor it holds a<br>collection of {LIS.NetSped.PublicServiceLayer.Models.Customer.ExtTables.LISPublicExtendedDataField}. |
| `carrier_condition_type` | [`CarrierConditionType2Enum`](../../doc/models/carrier-condition-type-2-enum.md) | Optional | Gets or sets the type of the carrier condition. |
| `carrier_sales_tax_code` | `string` | Optional | Gets or sets the carrier sales tax code. |
| `dangerous_goods` | [`List of LISPublicOrderDGood`](../../doc/models/lis-public-order-d-good.md) | Optional | Gets or sets the dangerous goods. |
| `service_order_template_id` | `int` | Optional | Gets or sets the service order template identifier. |
| `debit_condition_temporary_identifier` | `string` | Optional | Gets or sets the condition temporary identifier. |
| `credit_condition_temporary_identifier` | `string` | Optional | Gets or sets the credit condition temporary identifier. |
| `dossier_condition_temporary_identifier` | `string` | Optional | - |
| `has_manual_freight_payer_condition` | `bool` | Optional | Gets or sets a value indicating whether this instance has manual condition. |
| `has_manual_carrier_condition` | `bool` | Optional | Gets or sets a value indicating whether this instance has manual condition. |
| `debit_print_currency` | `string` | Optional | Gets or sets the debit print currency. |
| `order_source_area` | [`OrderSourceAreaEnum`](../../doc/models/order-source-area-enum.md) | Optional | Gets or sets the order source area. |
| `tour` | [`LISPublicOrderTour`](../../doc/models/lis-public-order-tour.md) | Optional | A base class for all order data contracts. |
| `invoice_data` | [`List of LISPublicOrderInvoiceData`](../../doc/models/lis-public-order-invoice-data.md) | Optional | Gets or sets the invoice data. |
| `dossier_no` | `string` | Optional | Gets or sets the dossier no. |
| `harbour_id` | `int` | Optional | Gets or sets the harbour identifier. |
| `log_model_id` | `int` | Optional | Gets or sets the log model identifier. |
| `driving_time` | `int` | Optional | Gets or sets the driving time. |
| `term_of_payment_id` | `int` | Optional | Gets or sets the term of payment identifier. |
| `inbound_bordero_no` | `string` | Optional | Gets or sets the inbound bordero no. |
| `owner` | `string` | Optional | Gets or sets the owner. |
| `has_time_table` | `bool` | Optional | Gets or sets a value indicating whether this instance has time table. |
| `carrier_for_last_shipment` | `int` | Optional | / |
| `shipment_id_for_carrier_in_address_list` | `int` | Optional | - |
| `ssc_cs` | [`List of LISPublicSSCC`](../../doc/models/lis-public-sscc.md) | Optional | Lists the SSCCs for the order |
| `is_new` | `bool` | Optional | Gets or sets a value indicating whether this entity will be inserted or updated. |
| `original_hash_snapshot` | `string` | Optional | Gets or sets the original hash snapshot. |
| `original_snapshot` | `string` | Optional | Gets or sets the original snapshot. |
| `current_snapshot` | `string` | Optional | Gets or sets the current snapshot. |

## Example (as JSON)

```json
{
  "aggregates": {
    "weight": 131.92,
    "chargeableWeight": 206.9,
    "cubicDecimeter": 104.66,
    "loadingMeter": 17.44,
    "squareMeter": 46.98
  },
  "addresses": [
    {
      "customerId": 80,
      "contactPersonId": 140,
      "addressType": "DeparturePort"
    },
    {
      "customerId": 81,
      "contactPersonId": 139,
      "addressType": "DestinationPort"
    }
  ],
  "addressRoles": [
    {
      "orderId": 94,
      "sequentialNo": 96,
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy0",
      "customerId": 42
    },
    {
      "orderId": 95,
      "sequentialNo": 95,
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy1",
      "customerId": 43
    },
    {
      "orderId": 96,
      "sequentialNo": 94,
      "changedOn": "2016-03-13T12:52:32.123Z",
      "changedBy": "changedBy2",
      "customerId": 44
    }
  ],
  "details": [
    {
      "units": [
        {
          "unitType": "Unkown",
          "unitId": "unitId4",
          "quantity": 186.6,
          "createdOn": "2016-03-13T12:52:32.123Z",
          "createdBy": "createdBy8"
        },
        {
          "unitType": "Pallette",
          "unitId": "unitId3",
          "quantity": 186.61,
          "createdOn": "2016-03-13T12:52:32.123Z",
          "createdBy": "createdBy7"
        }
      ],
      "orderId": 55,
      "detailId": 139,
      "reference": "reference1",
      "content": "content9"
    },
    {
      "units": [
        {
          "unitType": "Pallette",
          "unitId": "unitId3",
          "quantity": 186.61,
          "createdOn": "2016-03-13T12:52:32.123Z",
          "createdBy": "createdBy7"
        },
        {
          "unitType": "Package",
          "unitId": "unitId2",
          "quantity": 186.62,
          "createdOn": "2016-03-13T12:52:32.123Z",
          "createdBy": "createdBy6"
        },
        {
          "unitType": "Quantity",
          "unitId": "unitId1",
          "quantity": 186.63,
          "createdOn": "2016-03-13T12:52:32.123Z",
          "createdBy": "createdBy5"
        }
      ],
      "orderId": 56,
      "detailId": 140,
      "reference": "reference2",
      "content": "content0"
    },
    {
      "units": [
        {
          "unitType": "Package",
          "unitId": "unitId2",
          "quantity": 186.62,
          "createdOn": "2016-03-13T12:52:32.123Z",
          "createdBy": "createdBy6"
        }
      ],
      "orderId": 57,
      "detailId": 141,
      "reference": "reference3",
      "content": "content1"
    }
  ],
  "appointments": [
    {
      "appointmentType": "Fix",
      "loadingType": "Loading",
      "dateFrom": "2016-03-13T12:52:32.123Z",
      "timeFrom": "2016-03-13T12:52:32.123Z",
      "dateTill": "2016-03-13T12:52:32.123Z"
    },
    {
      "appointmentType": "TrailerETA",
      "loadingType": "Delivery",
      "dateFrom": "2016-03-13T12:52:32.123Z",
      "timeFrom": "2016-03-13T12:52:32.123Z",
      "dateTill": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

