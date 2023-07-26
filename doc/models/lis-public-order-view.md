
# LIS Public Order View

Represents an entity class. This class depends on the database table #*V__GetKunAufKomplett

## Structure

`LISPublicOrderView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_cost` | `float` | Optional | Gets or sets the Vorkosten property. This property depends on the database field Vorkosten. |
| `is_fbf_printed` | `bool` | Optional | Gets or sets the DruFBF property. This property depends on the database field DruFBF. |
| `is_sped_us_printed` | `bool` | Optional | Gets or sets the DruSpedUS property. This property depends on the database field DruSpedUS. |
| `incoming_bordero_no` | `string` | Optional | Gets or sets the IncomingBorderoNo property. This property depends on the database field BordENr. |
| `sequence_no` | `int` | Optional | Gets or sets the BordELfdNr property. This property depends on the database field BordELfdNr. |
| `order_input_type` | [`OrderInputTypeEnum`](../../doc/models/order-input-type-enum.md) | Optional | Gets or sets the OrderInputType property. This property depends on the database field ErfTyp. |
| `is_cash_payment` | `bool` | Optional | Gets or sets the CashPayment property. This property depends on the database field Bar. |
| `order_id_gs` | `int` | Optional | Gets or sets the AufIntGs property. This property depends on the database field AufIntGs. |
| `cash_on_delivery_vat_free` | `float` | Optional | Gets or sets the CashOnDeliveryVATFree property. This property depends on the database field NachFrei. |
| `shipment_id` | `int` | Optional | Gets or sets the OrderId property. This property depends on the database field AufIntNr. |
| `order_no` | `int` | Optional | Gets or sets the OrderNo property. This property depends on the database field AufNr. |
| `order_sub_number` | `int` | Optional | Gets or sets the OrderSubNumber property. This property depends on the database field AufUnterNr. |
| `company` | `int` | Optional | Gets or sets the Company property. This property depends on the database field Firma. |
| `accounting_division` | `int` | Optional | Gets or sets the NL property. This property depends on the database field NL. |
| `division` | `int` | Optional | Gets or sets the Division property. This property depends on the database field Abt. |
| `changed_on` | `datetime` | Optional | Gets or sets the ChangedOn property. This property depends on the database field AendDat. |
| `changed_by` | `string` | Optional | Gets or sets the ChangedBy property. This property depends on the database field AendUs. |
| `order_type` | [`OrderTypeEnum`](../../doc/models/order-type-enum.md) | Optional | Gets or sets the AufArt property. This property depends on the database field AufArt. |
| `order_text` | `string` | Optional | Gets or sets the AufText property. This property depends on the database field AufText. |
| `remark` | `string` | Optional | Gets or sets the Remark property. This property depends on the database field AufInfo. |
| `order_date` | `datetime` | Optional | Gets or sets the AufDatum property. This property depends on the database field AufDatum. |
| `customer_id` | `int` | Optional | Gets or sets the CustomerId property. This property depends on the database field AufgeberNr. |
| `delivery_number` | `string` | Optional | Gets or sets the DeliveryNote property. This property depends on the database field LiefNr. |
| `delivery_date` | `datetime` | Optional | Gets or sets the LiefDat property. This property depends on the database field LiefDat. |
| `picking_no` | `string` | Optional | Gets or sets the ConsignmentNumber property. This property depends on the database field KommNr. |
| `charge_no` | `string` | Optional | Gets or sets the ChargeNo property. This property depends on the database field ChargeNr. |
| `bordero_id` | `int` | Optional | Gets or sets the BorderoId property. This property depends on the database field BordIntNr. |
| `loading_customer_id` | `int` | Optional | Gets or sets the LoadingCustomerId property. This property depends on the database field BelNr. |
| `loading_country_code` | `string` | Optional | Gets or sets the LoadingCountryCode property. This property depends on the database field BelLKZ. |
| `loading_locality_id` | `int` | Optional | Gets or sets the LoadingLocalityId property. This property depends on the database field BelId. |
| `loading_zip` | `string` | Optional | Gets or sets the LoadingZip property. This property depends on the database field BelPLZ. |
| `loading_city` | `string` | Optional | Gets or sets the LoadingCity property. This property depends on the database field BelOrt. |
| `loadingt_bsl` | `string` | Optional | Gets or sets the BelBSL property. This property depends on the database field BelBSL. |
| `degt` | `string` | Optional | Gets or sets the BelDEGT property. This property depends on the database field BelDEGT. |
| `community_code` | `int` | Optional | Gets or sets the BelGTB property. This property depends on the database field BelGTB. |
| `loading_from_date` | `datetime` | Optional | Gets or sets the BelVonDat property. This property depends on the database field BelVonDat. |
| `loading_from_time` | `datetime` | Optional | Gets or sets the BelVonZeit property. This property depends on the database field BelVonZeit. |
| `loading_till_date` | `datetime` | Optional | Gets or sets the BelBisDat property. This property depends on the database field BelBisDat. |
| `loading_till_time` | `datetime` | Optional | Gets or sets the BelBisZeit property. This property depends on the database field BelBisZeit. |
| `fix_loading_date_from` | `datetime` | Optional | Gets or sets the BelFix property. This property depends on the database field BelFix. |
| `loading_fee` | `int` | Optional | Gets or sets the BelGebNein property. This property depends on the database field BelGebNein. |
| `estimated_loading_date` | `datetime` | Optional | Gets or sets the BelSollVon property. This property depends on the database field BelSollVon. |
| `estimated_loading_till_date` | `datetime` | Optional | Gets or sets the BelSollBis property. This property depends on the database field BelSollBis. |
| `guaranteed_loading_date` | `datetime` | Optional | Gets or sets the BelFixBis property. This property depends on the database field BelFixBis. |
| `loading_rf` | `int` | Optional | Gets or sets the BelRF property. This property depends on the database field BelRF. |
| `bordero_no` | `int` | Optional | Gets or sets the BorderoNo property. This property depends on the database field BordNr. |
| `delivery_area_no` | `int` | Optional | Gets or sets the BelGebNr property. This property depends on the database field BelGebNr. |
| `first_tour_id` | `int` | Optional | Gets or sets the ErsteTourIntNr property. This property depends on the database field ErsteTourIntNr. |
| `first_tour_no` | `int` | Optional | Gets or sets the ErsteTourNr property. This property depends on the database field ErsteTourNr. |
| `tour_id` | `int` | Optional | Gets or sets the TourId property. This property depends on the database field TourIntNr. |
| `tour_no` | `int` | Optional | Gets or sets the TourNo property. This property depends on the database field TourNr. |
| `tour_sequential_no` | `int` | Optional | Gets or sets the TourSequentialNo property. This property depends on the database field TourLfdNr. |
| `internal_bordero_no` | `int` | Optional | Gets or sets the InternalBorderoNo property. This property depends on the database field BordEIntNr. |
| `sender_id` | `int` | Optional | Gets or sets the SenderId property. This property depends on the database field AbsNr. |
| `departure_country_code` | `string` | Optional | Gets or sets the DepartureCountryCode property. This property depends on the database field AbgLKZ. |
| `departure_id` | `int` | Optional | Gets or sets the AbgID property. This property depends on the database field AbgID. |
| `departure_zip` | `string` | Optional | Gets or sets the DepartureZip property. This property depends on the database field AbgPLZ. |
| `departure_city` | `string` | Optional | Gets or sets the DepartureCity property. This property depends on the database field AbgOrt. |
| `sender_bsl` | `string` | Optional | Gets or sets the AbgBSL property. This property depends on the database field AbgBSL. |
| `sender_degt` | `string` | Optional | Gets or sets the AbgDEGT property. This property depends on the database field AbgDEGT. |
| `sender_community_code` | `int` | Optional | Gets or sets the AbgGTB property. This property depends on the database field AbgGTB. |
| `departure_type` | [`DepartureType1Enum`](../../doc/models/departure-type-1-enum.md) | Optional | Gets or sets the AbgKZ property. This property depends on the database field AbgKZ. |
| `direct_delivery` | `bool` | Optional | Gets or sets the Direkt property. This property depends on the database field Direkt. |
| `collecting_vehicle` | `string` | Optional | Gets or sets the AbholKfz property. This property depends on the database field AbholKfz. |
| `consignee_id` | `int` | Optional | Gets or sets the ConsigneeId property. This property depends on the database field EmpNr. |
| `unloading_country_code` | `string` | Optional | Gets or sets the UnloadingCountryCode property. This property depends on the database field EmgLKZ. |
| `unloading_locality_id` | `int` | Optional | Gets or sets the UnloadingLocalityId property. This property depends on the database field EmgID. |
| `unloading_zip` | `string` | Optional | Gets or sets the UnloadingZip property. This property depends on the database field EmgPLZ. |
| `unloading_city` | `string` | Optional | Gets or sets the UnloadingCity property. This property depends on the database field EmgOrt. |
| `consignee_bsl` | `string` | Optional | Gets or sets the EmgBSL property. This property depends on the database field EmgBSL. |
| `consignee_degt` | `string` | Optional | Gets or sets the EmgDEGT property. This property depends on the database field EmgDEGT. |
| `consignee_community_code` | `int` | Optional | Gets or sets the EmgGTB property. This property depends on the database field EmgGTB. |
| `deliver_date_from` | `datetime` | Optional | Gets or sets the EntVonDat property. This property depends on the database field EntVonDat. |
| `delivery_time_from` | `datetime` | Optional | Gets or sets the EntVonZeit property. This property depends on the database field EntVonZeit. |
| `deliver_end_date` | `datetime` | Optional | Gets or sets the EntBisDat property. This property depends on the database field EntBisDat. |
| `delivery_end_time` | `datetime` | Optional | Gets or sets the TimeTill property. This property depends on the database field EntBisZeit. |
| `distance` | `float` | Optional | Gets or sets the KM property. This property depends on the database field KM. |
| `distance_section` | `float` | Optional | Gets or sets the KMGFT property. This property depends on the database field KMGFT. |
| `driving_time` | `int` | Optional | Gets or sets the DrivingTime property. This property depends on the database field Fahrtzeit. |
| `freight_payer_id` | `int` | Optional | Gets or sets the FreightPayerId property. This property depends on the database field FZNr. |
| `freight_payer_condition_type` | `string` | Optional | Gets or sets the FreightPayerConditionType property. This property depends on the database field FZKond. |
| `freight_payer_optimizing_type` | `string` | Optional | Gets or sets the FreightPayerOptimizingType property. This property depends on the database field FZOptKz. |
| `freight_payer_optimizing_no` | `int` | Optional | Gets or sets the FreightPayerOptimizingNo property. This property depends on the database field FZOptNr. |
| `freight_payer_main_carriage` | `string` | Optional | Gets or sets the FreightPayerMainCarriage property. This property depends on the database field FZHLKz. |
| `freight_payer_sales_tax_code` | `string` | Optional | Gets or sets the FreightPayerSalesTaxCode property. This property depends on the database field FZUC. |
| `carrier_id` | `int` | Optional | Gets or sets the CarrierId property. This property depends on the database field FFNr. |
| `carrier_condition_type` | [`CarrierConditionType1Enum`](../../doc/models/carrier-condition-type-1-enum.md) | Optional | Gets or sets the CarrierConditionType property. This property depends on the database field FFKond. |
| `carrier_optimization_type` | [`CarrierOptimizationTypeEnum`](../../doc/models/carrier-optimization-type-enum.md) | Optional | Gets or sets the CarrierOptimizationType property. This property depends on the database field FFOptKz. |
| `carrier_optimization_no` | `int` | Optional | Gets or sets the CarrierOptimizationNo property. This property depends on the database field FFOptNr. |
| `carrier_main_carriage_type` | `string` | Optional | Gets or sets the CarrierMainCarriageType property. This property depends on the database field FFHLKz. |
| `carrier_sales_tax_code` | `string` | Optional | Gets or sets the CarrierSalesTaxCode property. This property depends on the database field FFUC. |
| `traffic_mode` | `string` | Optional | Gets or sets the TrafficMode property. This property depends on the database field VerkArt. |
| `freight_terms` | `string` | Optional | Gets or sets the Freight Terms property. This property depends on the database field Frankatur. |
| `lump_sum` | `float` | Optional | Gets or sets the LumpSum property. This property depends on the database field Pauschale. |
| `cash_on_delivery` | `float` | Optional | Gets or sets the CashOnDelivery property. This property depends on the database field Nach. |
| `cash_on_delivery_sales_tax_code` | `string` | Optional | Gets or sets the CashOnDeliverySalesTaxCode property. This property depends on the database field NachUC. |
| `weight` | `float` | Optional | Gets or sets the Weight property. This property depends on the database field TatsGew. |
| `chargeable_weight` | `float` | Optional | Gets or sets the ChargeableWeight property. This property depends on the database field FpflGew. |
| `packages` | `int` | Optional | Gets or sets the Packages property. This property depends on the database field ColliAnz. |
| `pallets` | `int` | Optional | Gets or sets the Pallets property. This property depends on the database field PalAnz. |
| `storage_places` | `int` | Optional | Gets or sets the StoragePlaces property. This property depends on the database field SPAnz. |
| `destination_forwarder_id` | `int` | Optional | Gets or sets the DestinationForwarderId property. This property depends on the database field EmpSped. |
| `lorry_id` | `string` | Optional | Gets or sets the LorryId property. This property depends on the database field KfzZugID. |
| `proceeds` | `float` | Optional | Gets or sets the Proceeds property. This property depends on the database field Erloes. |
| `charges` | `float` | Optional | Gets or sets the Charges property. This property depends on the database field Kosten. |
| `goods_cd` | `int` | Optional | Gets or sets the WarenKz property. This property depends on the database field WarenKz. |
| `permit_id` | `string` | Optional | Gets or sets the PermitId property. This property depends on the database field Gen. |
| `co_driver_id` | `int` | Optional | Gets or sets the CoDriverId property. This property depends on the database field BFahID. |
| `driver_id` | `int` | Optional | Gets or sets the DriverId property. This property depends on the database field FahID. |
| `trailer_id` | `string` | Optional | Gets or sets the TrailerId property. This property depends on the database field KfzAnhID. |
| `reference_number` | `string` | Optional | Gets or sets the ReferenceNumber property. This property depends on the database field RefNr. |
| `swap_body_id_1` | `string` | Optional | Gets or sets the SwapBodyId1 property. This property depends on the database field WBruecke1. |
| `swap_body_2` | `string` | Optional | Gets or sets the WBruecke2 property. This property depends on the database field WBruecke2. |
| `is_credit_invoiced` | `int` | Optional | Gets or sets the IsCreditInvoiced property. This property depends on the database field FakGs. |
| `hazardous_good_qualified` | `bool` | Optional | Gets or sets the HazardousGoodQualified property. This property depends on the database field Gefahrgut. |
| `cost_center` | `int` | Optional | Gets or sets the CostCenter property. This property depends on the database field Kostenstel. |
| `account_table` | `int` | Optional | Gets or sets the AccountTable property. This property depends on the database field KtoTab. |
| `reefer_cargo` | `bool` | Optional | Gets or sets the ReeferCargo property. This property depends on the database field Kuehlgut. |
| `load_dev_voucher_no` | `int` | Optional | Gets or sets the LmScheinNr property. This property depends on the database field LmScheinNr. |
| `is_invoice_invoiced` | `int` | Optional | Gets or sets the IsInvoiceInvoiced property. This property depends on the database field FakRe. |
| `is_pallet_note_printed` | `bool` | Optional | Gets or sets the IsPalletNotePrinted property. This property depends on the database field DruPal. |
| `original_sender_id` | `int` | Optional | Gets or sets the OriginalSenderId property. This property depends on the database field UrAbsNr. |
| `print_retrieval` | `bool` | Optional | Gets or sets the DruAbhol property. This property depends on the database field DruAbhol. |
| `planned_swap_body_construction` | `string` | Optional | Gets or sets the SollWBAufb property. This property depends on the database field SollWBAufb. |
| `freight_payer_common_rate` | `int` | Optional | Gets or sets the FreightPayerCommonRate property. This property depends on the database field FZAllgKond. |
| `print_nn` | `bool` | Optional | Gets or sets the DruNN property. This property depends on the database field DruNN. |
| `internal_order_no_debitor` | `int` | Optional | Gets or sets the InternalOrderNoDebitor property. This property depends on the database field AufIntRe. |
| `invoicing_indicator` | `int` | Optional | Gets or sets the InvoicingIndicator property. This property depends on the database field ReAbrKz. |
| `rec_adv` | `int` | Optional | Gets or sets the RecAdv property. This property depends on the database field RecAdv. |
| `relation_kind` | [`RelationKindEnum`](../../doc/models/relation-kind-enum.md) | Optional | Gets or sets the FZNahFern property. This property depends on the database field FZNahFern. |
| `is_transport_order_printed` | `bool` | Optional | Gets or sets the DruTRANS property. This property depends on the database field DruTRANS. |
| `is_order_confirmation_printed` | `bool` | Optional | Gets or sets the DruAufBest property. This property depends on the database field DruAufBest. |
| `final_recipient_id` | `int` | Optional | Gets or sets the FinalRecipientId property. This property depends on the database field EndEmpNr. |
| `end_name_1` | `string` | Optional | Gets or sets the EndName1 property. This property depends on the database field EndName1. |
| `receiver_contry_code` | `string` | Optional | Gets or sets the ReceiverContryCode property. This property depends on the database field EndLKZ. |
| `receiver_zip` | `string` | Optional | Gets or sets the ReceiverZip property. This property depends on the database field EndPLZ. |
| `receiver_city` | `string` | Optional | Gets or sets the ReceiverCity property. This property depends on the database field EndOrt. |
| `receiver_street` | `string` | Optional | Gets or sets the ReceiverStreet property. This property depends on the database field EndStr. |
| `cash_on_delivery_currency` | `string` | Optional | Gets or sets the CashOnDeliveryCurrency property. This property depends on the database field WNWaehr. |
| `carriage_forward_currency` | `string` | Optional | Gets or sets the CarriageForwardCurrency property. This property depends on the database field FNWaehr. |
| `border_file_id` | `int` | Optional | Gets or sets the Grenze property. This property depends on the database field Grenze. |
| `distance_till_border` | `float` | Optional | Gets or sets the KMBisGrz property. This property depends on the database field KMBisGrz. |
| `km_after_border` | `float` | Optional | Gets or sets the KMAbGrz property. This property depends on the database field KMAbGrz. |
| `goods_currency` | `string` | Optional | Gets or sets the WWWaehr property. This property depends on the database field WWWaehr. |
| `intra_stat_customer_id` | `int` | Optional | Gets or sets the IntrastatCustomerNo property. This property depends on the database field IntraAkpNr. |
| `are_labels_printed` | `bool` | Optional | Gets or sets the DruAufEtik property. This property depends on the database field DruAufEtik. |
| `division_id` | `int` | Optional | Gets or sets the DivisionId property. This property depends on the database field HAbtID. |
| `harbour` | `int` | Optional | Gets or sets the Harbour property. This property depends on the database field Ladehafen. |
| `dsi_number` | `string` | Optional | Gets or sets the DsiNr property. This property depends on the database field DsiNr. |
| `pieces` | `int` | Optional | Gets or sets the Pieces property. This property depends on the database field MEAnz. |
| `dossier_id` | `int` | Optional | Gets or sets the DosIntNr property. This property depends on the database field DosIntNr. |
| `dossier_no_short` | `string` | Optional | Gets or sets the DosNr property. This property depends on the database field DosNr. |
| `load_dev_booking` | `bool` | Optional | Gets or sets the LoadDevBooking property. This property depends on the database field LmVerb. |
| `declared_value` | `float` | Optional | Gets or sets the DeclaredValue property. This property depends on the database field Warenwert. |
| `pri_ezb` | `bool` | Optional | Gets or sets the DruEZB property. This property depends on the database field DruEZB. |
| `cubic_decimeter` | `float` | Optional | Gets or sets the CubicDecimeter property. This property depends on the database field CDMAnz. |
| `loading_meter` | `float` | Optional | Gets or sets the LoadingMeter property. This property depends on the database field LMAnz. |
| `square_meter` | `float` | Optional | Gets or sets the SquareMeter property. This property depends on the database field QMAnz. |
| `cost_unit` | `int` | Optional | Gets or sets the CostUnit property. This property depends on the database field KTraeger. |
| `original_sender_relation` | `string` | Optional | Gets or sets the OriginalSenderRelation property. This property depends on the database field UrAbsRel. |
| `loading_area_id` | `string` | Optional | Gets or sets the LoadingArea property. This property depends on the database field GBTAbg. |
| `unloading_area_id` | `string` | Optional | Gets or sets the UnloadingArea property. This property depends on the database field GBTEmg. |
| `is_company_paper_printed` | `bool` | Optional | Gets or sets the DruSpedAkt property. This property depends on the database field DruSpedAkt. |
| `order_group` | `string` | Optional | Gets or sets the AufGrp property. This property depends on the database field AufGrp. |
| `dispo_info_1` | `int` | Optional | Gets or sets the DispoInfo1 property. This property depends on the database field DispoInfo1. |
| `dispo_info_2` | `int` | Optional | Gets or sets the DispoInfo2 property. This property depends on the database field DispoInfo2. |
| `dispo_info_3` | `int` | Optional | Gets or sets the DispoInfo3 property. This property depends on the database field DispoInfo3. |
| `dispatch_information` | `int` | Optional | Gets or sets the DispatchInformation property. This property depends on the database field DispoInfo4. |
| `order_category` | `string` | Optional | Gets or sets the AufKlasse property. This property depends on the database field AufKlasse. |
| `is_loading_list_printed` | `bool` | Optional | Gets or sets the IsLoadingListPrinted property. This property depends on the database field DruLadeL. |
| `bord_int_ext` | `int` | Optional | Gets or sets the BordIntExt property. This property depends on the database field BordIntExt. |
| `outra_stat_customer_id` | `int` | Optional | Gets or sets the OutraAkpNr property. This property depends on the database field OutraAkpNr. |
| `unloading_date_fix_from` | `datetime` | Optional | Gets or sets the EntFix property. This property depends on the database field EntFix. |
| `invoice_division_id` | `int` | Optional | Gets or sets the InvoiceDivisionId property. This property depends on the database field ReAbtID. |
| `short_telematic_message` | `string` | Optional | Gets or sets the ShortTelematicMessage property. This property depends on the database field TMMsgMC. |
| `is_freight_payer_invoicing_blocked` | `bool` | Optional | Gets or sets the IsFreightPayerInvoicingBlocked property. This property depends on the database field FZFakSperr. |
| `d_good_id` | `int` | Optional | Gets or sets the AufGGutNr property. This property depends on the database field AufGGutNr. |
| `distance_load` | `float` | Optional | Gets or sets the Distance property. This property depends on the database field KMLast. |
| `distance_toll` | `float` | Optional | Gets or sets the DistanceToll property. This property depends on the database field KMMaut. |
| `distance_empty` | `float` | Optional | Gets or sets the DistanceEmpty property. This property depends on the database field KMLeer. |
| `distance_toll_empty` | `float` | Optional | Gets or sets the DistanceTollEmpty property. This property depends on the database field KMLeerMaut. |
| `container_id` | `int` | Optional | Gets or sets the TMittel property. This property depends on the database field TMittel. |
| `unloading_list_id` | `int` | Optional | Gets or sets the ELadLIntNr property. This property depends on the database field ELadLIntNr. |
| `cargo_insurance` | `string` | Optional | Gets or sets the FZKunVB property. This property depends on the database field FZKunVB. |
| `bonus_lump_sum` | `float` | Optional | Gets or sets the TVPausch property. This property depends on the database field TVPausch. |
| `distance_state` | [`DistanceStateEnum`](../../doc/models/distance-state-enum.md) | Optional | Gets or sets the DistanceState property. This property depends on the database field KMStatus. |
| `sv_mode` | `int` | Optional | Gets or sets the SVModus property. This property depends on the database field SVModus. |
| `palletts` | `float` | Optional | Gets or sets the PalAnzSum property. This property depends on the database field PalAnzSum. |
| `storage_places_sum` | `float` | Optional | Gets or sets the PallettSpacesCount property. This property depends on the database field SpAnzSum. |
| `pieces_sum` | `float` | Optional | Gets or sets the MeAnzSum property. This property depends on the database field MeAnzSum. |
| `shipping_units` | `float` | Optional | Gets or sets the ShippingUnits property. This property depends on the database field NVEAnzSum. |
| `lis_exit` | `int` | Optional | Gets or sets the LisExit property. This property depends on the database field LisExit. |
| `base_order_no` | `int` | Optional | Gets or sets the BasisNr property. This property depends on the database field BasisNr. |
| `base_order_id` | `int` | Optional | Gets or sets the BasisIntNr property. This property depends on the database field BasisIntNr. |
| `invoice_department_id` | `int` | Optional | Gets or sets the InvoiceDepartmentId property. This property depends on the database field ReBerID. |
| `department_id` | `int` | Optional | Gets or sets the DepartmentId property. This property depends on the database field HBerID. |
| `sub_department_id` | `int` | Optional | Gets or sets the UBerID property. This property depends on the database field UBerID. |
| `internal_cost_allocation_mode` | `int` | Optional | Gets or sets the InternalCostAllocationMode property. This property depends on the database field ILVModus. |
| `created_on` | `datetime` | Optional | Gets or sets the CreatedOn property. This property depends on the database field ErstDat. |
| `debit_form_type` | `int` | Optional | Gets or sets the FormType property. This property depends on the database field FormTyp. |
| `own_form_type` | `int` | Optional | Gets or sets the OwnFormType property. This property depends on the database field FormETyp. |
| `currency_print` | `string` | Optional | Gets or sets the CurrencyPrint property. This property depends on the database field WaehrDru. |
| `unloading_date_till_planned` | `datetime` | Optional | Gets or sets the EntSollBis property. This property depends on the database field EntSollBis. |
| `transportation_route_id` | `int` | Optional | Gets or sets the TransportationRoute property. This property depends on the database field ErfDR. |
| `logistic_provider_service_id` | `int` | Optional | Gets or sets the DlSvINr property. This property depends on the database field DlSvINr. |
| `order_id_bord` | `int` | Optional | Gets or sets the AufIntBord property. This property depends on the database field AufIntBord. |
| `bord_int_sub` | `int` | Optional | Gets or sets the BordIntSub property. This property depends on the database field BordIntSub. |
| `order_int_sub` | `int` | Optional | Gets or sets the AufIntSub property. This property depends on the database field AufIntSub. |
| `calculated_amount` | `float` | Optional | Gets or sets the CalculatedAmount property. This property depends on the database field ReNettoAnt. |
| `cont_int_nr` | `int` | Optional | Gets or sets the ContIntNr property. This property depends on the database field ContIntNr. |
| `cancellation_state` | `int` | Optional | Gets or sets the CancellationState property. This property depends on the database field DelKz. |
| `ilv_ori_nr` | `int` | Optional | Gets or sets the ILVOriNr property. This property depends on the database field ILVOriNr. |
| `ilv_abg_nr` | `int` | Optional | Gets or sets the ILVAbgNr property. This property depends on the database field ILVAbgNr. |
| `target_weight` | `float` | Optional | Gets or sets the TargetWeight property. This property depends on the database field SolTGewSum. |
| `exchange_rate_date` | `datetime` | Optional | Gets or sets the WKursDat property. This property depends on the database field WKursDat. |
| `created_by` | `string` | Optional | Gets or sets the CreatedBy property. This property depends on the database field ErstUs. |
| `dispo_info_5` | `int` | Optional | Gets or sets the DispoInfo5 property. This property depends on the database field DispoInfo5. |
| `dispo_info_6` | `int` | Optional | Gets or sets the DispoInfo6 property. This property depends on the database field DispoInfo6. |
| `dispo_info_7` | `int` | Optional | Gets or sets the DispoInfo7 property. This property depends on the database field DispoInfo7. |
| `dispo_info_8` | `int` | Optional | Gets or sets the DispoInfo8 property. This property depends on the database field DispoInfo8. |
| `dispo_info_9` | `int` | Optional | Gets or sets the DispoInfo9 property. This property depends on the database field DispoInfo9. |
| `dispo_inf_10` | `int` | Optional | Gets or sets the DispoInf10 property. This property depends on the database field DispoInf10. |
| `route_id` | `int` | Optional | Gets or sets the RouteId property. This property depends on the database field RoutIntNr. |
| `km_methode` | `string` | Optional | Gets or sets the KmMethode property. This property depends on the database field KmMethode. |
| `last_delivery_date` | `datetime` | Optional | Gets or sets the EntSollVon property. This property depends on the database field EntSollVon. |
| `departure_relation_id` | `string` | Optional | Gets or sets the AbholRel property. This property depends on the database field AbholRel. |
| `final_recipient_relation_relation_id` | `string` | Optional | Gets or sets the EndEmpRel property. This property depends on the database field EndEmpRel. |
| `given_packages` | `float` | Optional | Gets or sets the SollVPESum property. This property depends on the database field SollVPESum. |
| `unloading_date_fix_till` | `datetime` | Optional | Gets or sets the EntFixBis property. This property depends on the database field EntFixBis. |
| `internal_order_no_debitor_3` | `int` | Optional | Gets or sets the InternalOrderNoDebitor3 property. This property depends on the database field AufIntRe3. |
| `order_state` | `int` | Optional | Gets or sets the SLStatus property. This property depends on the database field SLStatus. |
| `pre_order_planning_id` | `int` | Optional | Gets or sets the PreOrderPlanningId property. This property depends on the database field VDisIntNr. |
| `owner` | `string` | Optional | Gets or sets the EigenUS property. This property depends on the database field EigenUS. |
| `dossier_no` | `string` | Optional | Gets or sets the PositionNumber property. This property depends on the database field LPosNr. |
| `logistic_provider_information` | `string` | Optional | Gets or sets the AufDLInfo property. This property depends on the database field AufDLInfo. |
| `pre_order_planning_no` | `string` | Optional | Gets or sets the PreOrderPlanningNo property. This property depends on the database field VDisNrExt. |
| `unloading_container` | `int` | Optional | Gets or sets the EntBeh property. This property depends on the database field EntBeh. |
| `unloading_rf` | `int` | Optional | Gets or sets the EntRF property. This property depends on the database field EntRF. |
| `contact_person_id` | `int` | Optional | Gets or sets the ContactPersonId property. This property depends on the database field AspNr. |
| `original_order_type` | [`OriginalOrderType1Enum`](../../doc/models/original-order-type-1-enum.md) | Optional | Gets or sets the ErstAufArt property. This property depends on the database field ErstAufArt. |
| `additional_charging_no` | `int` | Optional | Gets or sets the AdditionalChargingNo property. This property depends on the database field ZBNr. |
| `log_model_id` | `int` | Optional | Gets or sets the LogModelId property. This property depends on the database field LogModelId. |
| `service_order_template_id` | `int` | Optional | Gets or sets the ServiceOrderTemplateId property. This property depends on the database field ServiceOrderTemplateId. |
| `order_source_area` | `int` | Optional | Gets or sets the SourceArea property. This property depends on the database field SourceArea. |
| `terms_of_payment` | `string` | Optional | Gets or sets the TermsOfPayment property. This property depends on the database field ZahlBed. |

## Example (as JSON)

```json
{
  "initialCost": 169.2,
  "isFBFPrinted": false,
  "isSpedUsPrinted": false,
  "incomingBorderoNo": "incomingBorderoNo0",
  "sequenceNo": 226
}
```

