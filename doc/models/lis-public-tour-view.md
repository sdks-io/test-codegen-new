
# LIS Public Tour View

Represents an entity class. This class depends on the database table #*V__Tour

## Structure

`LISPublicTourView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cash_payment` | `string` | Optional | Gets or sets the CashPayment property. This property depends on the database field Bar. |
| `is_credit_invoiced` | `int` | Optional | Gets or sets the IsCreditInvoiced property. This property depends on the database field FakGs. |
| `is_invoice_invoiced` | `int` | Optional | Gets or sets the IsInvoiceInvoiced property. This property depends on the database field FakRe. |
| `tour_id` | `int` | Optional | Gets or sets the TourId property. This property depends on the database field TourIntNr. |
| `tour_no` | `int` | Optional | Gets or sets the TourNo property. This property depends on the database field TourNr. |
| `company` | `int` | Optional | Gets or sets the Company property. This property depends on the database field Firma. |
| `net_load` | `int` | Optional | Gets or sets the NL property. This property depends on the database field NL. |
| `division` | `int` | Optional | Gets or sets the Division property. This property depends on the database field Abt. |
| `invoice_credit_identifier` | `string` | Optional | Gets or sets the InvoiceCreditIdentifier property. This property depends on the database field TourDK. |
| `changed_on` | `datetime` | Optional | Gets or sets the ChangedOn property. This property depends on the database field AendDat. |
| `changed_by` | `string` | Optional | Gets or sets the ChangedBy property. This property depends on the database field AendUs. |
| `carrier_id` | `int` | Optional | Gets or sets the CarrierId property. This property depends on the database field FFNr. |
| `carrier_condition_type` | [`CarrierConditionType1Enum`](../../doc/models/carrier-condition-type-1-enum.md) | Optional | Gets or sets the CarrierConditionType property. This property depends on the database field FFKond. |
| `carrier_optimization_type` | [`CarrierOptimizationTypeEnum`](../../doc/models/carrier-optimization-type-enum.md) | Optional | Gets or sets the CarrierOptimizationType property. This property depends on the database field FFOptKz. |
| `carrier_optimization_no` | `int` | Optional | Gets or sets the CarrierOptimizationNo property. This property depends on the database field FFOptNr. |
| `carrier_main_carriage_type` | [`CarrierMainCarriageTypeEnum`](../../doc/models/carrier-main-carriage-type-enum.md) | Optional | Gets or sets the CarrierMainCarriageType property. This property depends on the database field FFHLKz. |
| `carrier_sales_tax_code` | `string` | Optional | Gets or sets the CarrierSalesTaxCode property. This property depends on the database field FFUC. |
| `tour_date_from` | `datetime` | Optional | Gets or sets the DateFrom property. This property depends on the database field TourDatum. |
| `lorry_id` | `string` | Optional | Gets or sets the LorryId property. This property depends on the database field KfzZugID. |
| `trailer_id` | `string` | Optional | Gets or sets the TrailerId property. This property depends on the database field KfzAnhID. |
| `vehile_group` | `string` | Optional | Gets or sets the VehileGroup property. This property depends on the database field KfzZugGrp. |
| `swap_body_id_1` | `string` | Optional | Gets or sets the SwapBodyId1 property. This property depends on the database field WBruecke1. |
| `swap_body_id_2` | `string` | Optional | Gets or sets the WBruecke2 property. This property depends on the database field WBruecke2. |
| `driver_id` | `int` | Optional | Gets or sets the DriverId property. This property depends on the database field FahID. |
| `co_driver_id` | `int` | Optional | Gets or sets the CoDriverId property. This property depends on the database field BFahID. |
| `weight` | `float` | Optional | Gets or sets the Weight property. This property depends on the database field TatsGew. |
| `chargeable_weight` | `float` | Optional | Gets or sets the ChargeableWeight property. This property depends on the database field FpflGew. |
| `packages` | `int` | Optional | Gets or sets the Packages property. This property depends on the database field ColliAnz. |
| `pallets` | `int` | Optional | Gets or sets the Pallets property. This property depends on the database field PalAnz. |
| `orders` | `int` | Optional | Gets or sets the Orders property. This property depends on the database field AnzAuftr. |
| `storage_places` | `int` | Optional | Gets or sets the StoragePlaces property. This property depends on the database field SPAnz. |
| `dispatch_branch_office` | `int` | Optional | Gets or sets the DispatchBranchOffice property. This property depends on the database field AbgNL. |
| `state` | `int` | Optional | Gets or sets the State property. This property depends on the database field Status. |
| `proceeds` | `float` | Optional | Gets or sets the Proceeds property. This property depends on the database field Erloes. |
| `charges` | `float` | Optional | Gets or sets the Charges property. This property depends on the database field Kosten. |
| `permit_id` | `string` | Optional | Gets or sets the PermitId property. This property depends on the database field Gen. |
| `is_locked` | `string` | Optional | Gets or sets the IsLocked property. This property depends on the database field fLocked. |
| `locked_by` | `string` | Optional | Gets or sets the LockedBy property. This property depends on the database field LockUs. |
| `is_cargo_manifest_printed` | `string` | Optional | Gets or sets the IsCargoManifestPrinted property. This property depends on the database field DruBord. |
| `is_cartage_note_printed` | `string` | Optional | Gets or sets the IsCartageNotePrinted property. This property depends on the database field DruRollk. |
| `is_pallet_note_printed` | `string` | Optional | Gets or sets the IsPalletNotePrinted property. This property depends on the database field DruPal. |
| `is_invoice_printed` | `int` | Optional | Gets or sets the IsInvoicePrinted property. This property depends on the database field DruRe. |
| `is_credit_note_printed` | `int` | Optional | Gets or sets the IsCreditNotePrinted property. This property depends on the database field DruGs. |
| `consignees` | `int` | Optional | Gets or sets the Consignees property. This property depends on the database field AnzEmp. |
| `division_id` | `int` | Optional | Gets or sets the DivisionId property. This property depends on the database field HAbtID. |
| `declared_value` | `float` | Optional | Gets or sets the DeclaredValue property. This property depends on the database field Warenwert. |
| `main_carriage_country_code` | `string` | Optional | Gets or sets the MainCarriageCountryCode property. This property depends on the database field HLLKZ. |
| `main_carriage_sequence` | `int` | Optional | Gets or sets the MainCarriageSequence property. This property depends on the database field HLLfdNr. |
| `main_carriage_weight` | `float` | Optional | Gets or sets the MainCarriageWeight property. This property depends on the database field HLGew. |
| `pieces` | `int` | Optional | Gets or sets the Pieces property. This property depends on the database field MEAnz. |
| `cubic_decimeter` | `float` | Optional | Gets or sets the CubicDecimeter property. This property depends on the database field CDMAnz. |
| `loading_meter` | `float` | Optional | Gets or sets the LoadingMeter property. This property depends on the database field LMAnz. |
| `square_meter` | `float` | Optional | Gets or sets the SquareMeter property. This property depends on the database field QMAnz. |
| `disposition_text` | `string` | Optional | Gets or sets the DispositionText property. This property depends on the database field TxtDispo. |
| `remark_1` | `string` | Optional | Gets or sets the Remark1 property. This property depends on the database field TxtBemerk1. |
| `remark_2` | `string` | Optional | Gets or sets the Remark2 property. This property depends on the database field TxtBemerk2. |
| `tourd_delibery_date` | `datetime` | Optional | Gets or sets the DateTill property. This property depends on the database field TourEntDat. |
| `tour_kind` | `int` | Optional | Gets or sets the TourKind property. This property depends on the database field TourArt. |
| `dangerous_goods` | `string` | Optional | Gets or sets the TourGefahr property. This property depends on the database field TourGefahr. |
| `reefer_cargo` | `string` | Optional | Gets or sets the TourKuehl property. This property depends on the database field TourKuehl. |
| `start_time` | `datetime` | Optional | Gets or sets the TimeFrom property. This property depends on the database field TourZeit. |
| `delivery_end_date` | `datetime` | Optional | Gets or sets the EntBisDat property. This property depends on the database field EntBisDat. |
| `delivery_end_time` | `datetime` | Optional | Gets or sets the TimeTill property. This property depends on the database field EntBisZeit. |
| `is_loading_list_printed` | `string` | Optional | Gets or sets the IsLoadingListPrinted property. This property depends on the database field DruLadeL. |
| `tour_sections` | `int` | Optional | Gets or sets the TourSections property. This property depends on the database field AnzDis. |
| `first_loading_order_id` | `int` | Optional | Gets or sets the FirstLoadingOrderId property. This property depends on the database field BAufIntNr. |
| `last_unloading_order_id` | `int` | Optional | Gets or sets the LastUnloadingOrderId property. This property depends on the database field EAufIntNr. |
| `loading_customer_id` | `int` | Optional | Gets or sets the LoadingCustomerId property. This property depends on the database field BelNr. |
| `loading_country_code` | `string` | Optional | Gets or sets the LoadingCountryCode property. This property depends on the database field BelLKZ. |
| `loading_locality_id` | `int` | Optional | Gets or sets the LoadingLocalityId property. This property depends on the database field BelID. |
| `loading_zip` | `string` | Optional | Gets or sets the LoadingZip property. This property depends on the database field BelPLZ. |
| `loading_city` | `string` | Optional | Gets or sets the LoadingCity property. This property depends on the database field BelOrt. |
| `consignee_id` | `int` | Optional | Gets or sets the ConsigneeId property. This property depends on the database field EmpNr. |
| `unloading_country_code` | `string` | Optional | Gets or sets the UnloadingCountryCode property. This property depends on the database field EmgLKZ. |
| `unloading_locality_id` | `int` | Optional | Gets or sets the UnloadingLocalityId property. This property depends on the database field EmgID. |
| `unloading_zip` | `string` | Optional | Gets or sets the UnloadingZip property. This property depends on the database field EmgPLZ. |
| `unloading_city` | `string` | Optional | Gets or sets the UnloadingCity property. This property depends on the database field EmgOrt. |
| `dispatch_information` | `int` | Optional | Gets or sets the DispatchInformation property. This property depends on the database field DispoInfo4. |
| `driving_time` | `int` | Optional | Gets or sets the DrivingTime property. This property depends on the database field Fahrtzeit. |
| `calculated_charges` | `float` | Optional | Gets or sets the CalculatedCharges property. This property depends on the database field KalkKosten. |
| `distance` | `float` | Optional | Gets or sets the Distance property. This property depends on the database field KMLast. |
| `distance_toll` | `float` | Optional | Gets or sets the DistanceToll property. This property depends on the database field KMMaut. |
| `distance_empty` | `float` | Optional | Gets or sets the DistanceEmpty property. This property depends on the database field KMLeer. |
| `distance_toll_empty` | `float` | Optional | Gets or sets the DistanceTollEmpty property. This property depends on the database field KMLeerMaut. |
| `proportional_credit_net_amount` | `float` | Optional | Gets or sets the ProportionalCreditNetAmount property. This property depends on the database field GsNettoAnt. |
| `proportional_calculated_invoice_amount` | `float` | Optional | Gets or sets the ProportionalCalculatedInvoiceAmount property. This property depends on the database field ReKalkAnt. |
| `tour_description` | `string` | Optional | Gets or sets the TourBez property. This property depends on the database field TourBez. |
| `tour_type` | [`TourTypeEnum`](../../doc/models/tour-type-enum.md) | Optional | Gets or sets the TourAufArt property. This property depends on the database field TourAufArt. |
| `distance_state` | [`DistanceStateEnum`](../../doc/models/distance-state-enum.md) | Optional | Gets or sets the DistanceState property. This property depends on the database field KMStatus. |
| `are_locations_fixed` | `string` | Optional | Gets or sets the AreLocationsFixed property. This property depends on the database field OrteFix. |
| `calender_job_series_group_id` | `int` | Optional | Gets or sets the CJSGrpID property. This property depends on the database field CJSGrpID. |
| `packages_sum` | `float` | Optional | Gets or sets the ColliAnzSu property. This property depends on the database field ColliAnzSu. |
| `paletts_sum` | `float` | Optional | Gets or sets the PalAnzSum property. This property depends on the database field PalAnzSum. |
| `pallett_spaces_count` | `float` | Optional | Gets or sets the PallettSpacesCount property. This property depends on the database field SpAnzSum. |
| `pieces_sum` | `float` | Optional | Gets or sets the MeAnzSum property. This property depends on the database field MeAnzSum. |
| `shipping_units` | `float` | Optional | Gets or sets the ShippingUnits property. This property depends on the database field NVEAnzSum. |
| `data_exchange_state` | `int` | Optional | Gets or sets the DataExchangeState property. This property depends on the database field DFUStatus. |
| `data_exchange_state_date` | `datetime` | Optional | Gets or sets the DataExchangeStateDate property. This property depends on the database field DFUStatDat. |
| `utilised_storage_places` | `string` | Optional | Gets or sets the UtilisedStoragePlaces property. This property depends on the database field ALSPKz. |
| `utilised_storage_places_percentage` | `float` | Optional | Gets or sets the UtilisedStoragePlacesPercentage property. This property depends on the database field ALSPPrz. |
| `utilised_load_capacity` | `string` | Optional | Gets or sets the UtilisedLoadCapacity property. This property depends on the database field ALNLKz. |
| `utilised_load_capacity_percentage` | `float` | Optional | Gets or sets the UtilisedLoadCapacityPercentage property. This property depends on the database field ALNLPrz. |
| `department_id` | `int` | Optional | Gets or sets the DepartmentId property. This property depends on the database field HBerID. |
| `carrier_maximum_loading_places` | `float` | Optional | Gets or sets the CarrierMaximumLoadingPlaces property. This property depends on the database field FFMaxSP. |
| `carrier_maximum_weight` | `float` | Optional | Gets or sets the CarrierMaximumWeight property. This property depends on the database field FFMaxTGew. |
| `carrier_group_id` | `string` | Optional | Gets or sets the CarrierGroupId property. This property depends on the database field FFGruppe. |
| `traffic_mode` | `string` | Optional | Gets or sets the TrafficMode property. This property depends on the database field VerkArt. |
| `requested_storage_places` | `float` | Optional | Gets or sets the RequestedStoragePlaces property. This property depends on the database field SpAnzFrei. |
| `requested_weight` | `float` | Optional | Gets or sets the RequestedWeight property. This property depends on the database field TatGewFrei. |
| `internal_cost_allocation_mode` | [`InternalCostAllocationModeEnum`](../../doc/models/internal-cost-allocation-mode-enum.md) | Optional | Gets or sets the InternalCostAllocationMode property. This property depends on the database field ILVModus. |
| `internal_cost_allocation_state` | [`InternalCostAllocationStateEnum`](../../doc/models/internal-cost-allocation-state-enum.md) | Optional | Gets or sets the InternalCostAllocationState property. This property depends on the database field ILVZust. |
| `cancellation_state` | [`CancellationStateEnum`](../../doc/models/cancellation-state-enum.md) | Optional | Gets or sets the CancellationState property. This property depends on the database field DelKz. |
| `short_telematic_message` | `string` | Optional | Gets or sets the ShortTelematicMessage property. This property depends on the database field TMMsgMC. |
| `target_weight` | `float` | Optional | Gets or sets the TargetWeight property. This property depends on the database field SolTGewSum. |
| `calculated_wheel_time` | `int` | Optional | Gets or sets the CalculatedWheelTime property. This property depends on the database field CalcLenkZ. |
| `invoicing_result` | `int` | Optional | Gets or sets the InvoicingResult property. This property depends on the database field FakResult. |
| `fencing` | `int` | Optional | Gets or sets the Fencing property. This property depends on the database field Fencing. |
| `route_id` | `int` | Optional | Gets or sets the RouteId property. This property depends on the database field RoutIntNr. |
| `provider_string` | `string` | Optional | Gets or sets the KmMethode property. This property depends on the database field KmMethode. |
| `actual_distance` | `float` | Optional | Gets or sets the ActualDistance property. This property depends on the database field KMIstLast. |
| `actual_distance_empty` | `float` | Optional | Gets or sets the ActualDistanceEmpty property. This property depends on the database field KMIstLeer. |
| `route_state` | [`RouteStateEnum`](../../doc/models/route-state-enum.md) | Optional | Gets or sets the RouteState property. This property depends on the database field RouStatus. |
| `working_days_on_weekdays` | `float` | Optional | Gets or sets the WorkingDaysOnWeekdays property. This property depends on the database field ETWerk. |
| `working_days_on_holidays` | `float` | Optional | Gets or sets the WorkingDaysOnHolidays property. This property depends on the database field ETFeier. |
| `requested_loading_meter` | `float` | Optional | Gets or sets the RequestedLoadingMeter property. This property depends on the database field LMAnzFrei. |
| `planned_by` | `string` | Optional | Gets or sets the PlannedBy property. This property depends on the database field DispoUS. |
| `created_on` | `datetime` | Optional | Gets or sets the CreatedOn property. This property depends on the database field ErstDat. |
| `created_by` | `string` | Optional | Gets or sets the CreatedBy property. This property depends on the database field ErstUS. |
| `position_number` | `string` | Optional | Gets or sets the PositionNumber property. This property depends on the database field LPosNr. |
| `locking_history_id` | `int` | Optional | Gets or sets the LockingHistoryId property. This property depends on the database field TLockHiNr. |
| `tour_information_1` | `int` | Optional | Gets or sets the TourInformation1 property. This property depends on the database field TourInfo1. |
| `tour_information_2` | `int` | Optional | Gets or sets the TourInformation2 property. This property depends on the database field TourInfo2. |
| `tour_information_3` | `int` | Optional | Gets or sets the TourInformation3 property. This property depends on the database field TourInfo3. |
| `tour_information_4` | `int` | Optional | Gets or sets the TourInformation4 property. This property depends on the database field TourInfo4. |
| `tour_information_5` | `int` | Optional | Gets or sets the TourInformation5 property. This property depends on the database field TourInfo5. |
| `tour_information_6` | `int` | Optional | Gets or sets the TourInformation6 property. This property depends on the database field TourInfo6. |
| `tour_information_7` | `int` | Optional | Gets or sets the TourInformation7 property. This property depends on the database field TourInfo7. |
| `tour_information_8` | `int` | Optional | Gets or sets the TourInformation8 property. This property depends on the database field TourInfo8. |
| `tour_information_9` | `int` | Optional | Gets or sets the TourInformation9 property. This property depends on the database field TourInfo9. |
| `tour_information_10` | `int` | Optional | Gets or sets the TourInformation10 property. This property depends on the database field TourInfo10. |
| `pre_order_planning_no` | `string` | Optional | Gets or sets the PreOrderPlanningNo property. This property depends on the database field VDisNrExt. |
| `pre_order_planning_id` | `int` | Optional | Gets or sets the PreOrderPlanningId property. This property depends on the database field VDisIntNr. |
| `dispatch_stop` | `int` | Optional | Gets or sets the DispatchStop property. This property depends on the database field AbfStopp. |
| `security_tag_1` | `string` | Optional | Gets or sets the SecurityTag1 property. This property depends on the database field Plombe1. |
| `security_tag_2` | `string` | Optional | Gets or sets the SecurityTag2 property. This property depends on the database field Plombe2. |
| `lorry_license_plate` | `string` | Optional | Gets or sets the LorryLicensePlate property. This property depends on the database field KfzPolKz. |
| `trailer_license_plate` | `string` | Optional | Gets or sets the TrailerLicensePlate property. This property depends on the database field AnhPolKz. |
| `lorry_telephone` | `string` | Optional | Gets or sets the LorryTelephone property. This property depends on the database field KfzTel. |
| `freight_net_portion` | `float` | Optional | Gets or sets the FrachtNettoAnt property. This property depends on the database field FrachtNettoAnt. |
| `terms_of_payment` | `string` | Optional | Gets or sets the TermsOfPayment property. This property depends on the database field ZahlBed. |
| `od_workday_trailer` | `float` | Optional | Gets or sets the ETWerkAnh property. This property depends on the database field ETWerkAnh. |
| `od_holiday_trailer` | `float` | Optional | Gets or sets the ETFeierAnh property. This property depends on the database field ETFeierAnh. |
| `fill_type` | [`FillTypeEnum`](../../doc/models/fill-type-enum.md) | Optional | Gets or sets the TFuellTyp property. This property depends on the database field TFuellTyp. |
| `additional_date` | `datetime` | Optional | Gets or sets the AdditionalDate property. This property depends on the database field dtmHilf1. |
| `dispatch_lock_clearance` | `int` | Optional | Gets or sets the AbfFreigabe property. This property depends on the database field AbfFreigabe. |
| `source_area` | `int` | Optional | Gets or sets the SourceArea property. This property depends on the database field SourceArea. |
| `time_table_item_id` | `int` | Optional | Gets or sets the TimeTableItemId property. This property depends on the database field TimeTableItemId. |
| `calculated_ca_amount` | `float` | Optional | Gets or sets the SumAntReLV property. This property depends on the database field SumAntReLV. |
| `time_table_item_type` | [`TimeTableItemTypeEnum`](../../doc/models/time-table-item-type-enum.md) | Optional | Gets or sets the TimeTableItemType property. This property depends on the database field TimeTableItemType. |
| `utc_code` | `int` | Optional | Gets or sets the UTCCode property. This property depends on the database field UTCCode. |
| `process_state` | [`ProcessStateEnum`](../../doc/models/process-state-enum.md) | Optional | Gets or sets the ProcessState property. This property depends on the database field ProcessState. |
| `tour_inf_sym_tour_id` | `int` | Optional | Gets or sets the TourInfSymTourIntNr property. This property depends on the database field TourInfSymTourIntNr. |
| `t_info_symbol_1` | `int` | Optional | Gets or sets the TInfoSymbol1 property. This property depends on the database field TInfoSymbol1. |
| `t_info_symbol_2` | `int` | Optional | Gets or sets the TInfoSymbol2 property. This property depends on the database field TInfoSymbol2. |
| `t_info_symbol_3` | `int` | Optional | Gets or sets the TInfoSymbol3 property. This property depends on the database field TInfoSymbol3. |
| `t_info_symbol_4` | `int` | Optional | Gets or sets the TInfoSymbol4 property. This property depends on the database field TInfoSymbol4. |
| `t_info_symbol_5` | `int` | Optional | Gets or sets the TInfoSymbol5 property. This property depends on the database field TInfoSymbol5. |
| `t_info_symbol_6` | `int` | Optional | Gets or sets the TInfoSymbol6 property. This property depends on the database field TInfoSymbol6. |
| `t_info_symbol_7` | `int` | Optional | Gets or sets the TInfoSymbol7 property. This property depends on the database field TInfoSymbol7. |
| `t_info_symbol_8` | `int` | Optional | Gets or sets the TInfoSymbol8 property. This property depends on the database field TInfoSymbol8. |
| `t_info_symbol_9` | `int` | Optional | Gets or sets the TInfoSymbol9 property. This property depends on the database field TInfoSymbol9. |
| `t_info_symbol_10` | `int` | Optional | Gets or sets the TInfoSymbol10 property. This property depends on the database field TInfoSymbol10. |
| `t_info_symbol_11` | `int` | Optional | Gets or sets the TInfoSymbol11 property. This property depends on the database field TInfoSymbol11. |
| `t_info_symbol_12` | `int` | Optional | Gets or sets the TInfoSymbol12 property. This property depends on the database field TInfoSymbol12. |
| `t_info_symbol_13` | `int` | Optional | Gets or sets the TInfoSymbol13 property. This property depends on the database field TInfoSymbol13. |
| `t_info_symbol_14` | `int` | Optional | Gets or sets the TInfoSymbol14 property. This property depends on the database field TInfoSymbol14. |
| `t_info_symbol_15` | `int` | Optional | Gets or sets the TInfoSymbol15 property. This property depends on the database field TInfoSymbol15. |
| `t_info_symbol_16` | `int` | Optional | Gets or sets the TInfoSymbol16 property. This property depends on the database field TInfoSymbol16. |
| `t_info_symbol_17` | `int` | Optional | Gets or sets the TInfoSymbol17 property. This property depends on the database field TInfoSymbol17. |
| `t_info_symbol_18` | `int` | Optional | Gets or sets the TInfoSymbol18 property. This property depends on the database field TInfoSymbol18. |
| `t_info_symbol_19` | `int` | Optional | Gets or sets the TInfoSymbol19 property. This property depends on the database field TInfoSymbol19. |
| `t_info_symbol_20` | `int` | Optional | Gets or sets the TInfoSymbol20 property. This property depends on the database field TInfoSymbol20. |
| `t_info_symbol_21` | `int` | Optional | Gets or sets the TInfoSymbol21 property. This property depends on the database field TInfoSymbol21. |
| `t_info_symbol_22` | `int` | Optional | Gets or sets the TInfoSymbol22 property. This property depends on the database field TInfoSymbol22. |
| `t_info_symbol_23` | `int` | Optional | Gets or sets the TInfoSymbol23 property. This property depends on the database field TInfoSymbol23. |
| `t_info_symbol_24` | `int` | Optional | Gets or sets the TInfoSymbol24 property. This property depends on the database field TInfoSymbol24. |
| `t_info_symbol_25` | `int` | Optional | Gets or sets the TInfoSymbol25 property. This property depends on the database field TInfoSymbol25. |
| `t_info_symbol_26` | `int` | Optional | Gets or sets the TInfoSymbol26 property. This property depends on the database field TInfoSymbol26. |
| `t_info_symbol_27` | `int` | Optional | Gets or sets the TInfoSymbol27 property. This property depends on the database field TInfoSymbol27. |
| `t_info_symbol_28` | `int` | Optional | Gets or sets the TInfoSymbol28 property. This property depends on the database field TInfoSymbol28. |
| `t_info_symbol_29` | `int` | Optional | Gets or sets the TInfoSymbol29 property. This property depends on the database field TInfoSymbol29. |
| `t_info_symbol_30` | `int` | Optional | Gets or sets the TInfoSymbol30 property. This property depends on the database field TInfoSymbol30. |
| `t_info_symbol_31` | `int` | Optional | Gets or sets the TInfoSymbol31 property. This property depends on the database field TInfoSymbol31. |
| `t_info_symbol_32` | `int` | Optional | Gets or sets the TInfoSymbol32 property. This property depends on the database field TInfoSymbol32. |
| `t_info_symbol_33` | `int` | Optional | Gets or sets the TInfoSymbol33 property. This property depends on the database field TInfoSymbol33. |
| `t_info_symbol_34` | `int` | Optional | Gets or sets the TInfoSymbol34 property. This property depends on the database field TInfoSymbol34. |
| `t_info_symbol_35` | `int` | Optional | Gets or sets the TInfoSymbol35 property. This property depends on the database field TInfoSymbol35. |
| `t_info_symbol_36` | `int` | Optional | Gets or sets the TInfoSymbol36 property. This property depends on the database field TInfoSymbol36. |
| `t_info_symbol_37` | `int` | Optional | Gets or sets the TInfoSymbol37 property. This property depends on the database field TInfoSymbol37. |
| `t_info_symbol_38` | `int` | Optional | Gets or sets the TInfoSymbol38 property. This property depends on the database field TInfoSymbol38. |
| `t_info_symbol_39` | `int` | Optional | Gets or sets the TInfoSymbol39 property. This property depends on the database field TInfoSymbol39. |
| `t_info_symbol_40` | `int` | Optional | Gets or sets the TInfoSymbol40 property. This property depends on the database field TInfoSymbol40. |
| `t_info_symbol_41` | `int` | Optional | Gets or sets the TInfoSymbol41 property. This property depends on the database field TInfoSymbol41. |
| `t_info_symbol_42` | `int` | Optional | Gets or sets the TInfoSymbol42 property. This property depends on the database field TInfoSymbol42. |
| `t_info_symbol_43` | `int` | Optional | Gets or sets the TInfoSymbol43 property. This property depends on the database field TInfoSymbol43. |
| `t_info_symbol_44` | `int` | Optional | Gets or sets the TInfoSymbol44 property. This property depends on the database field TInfoSymbol44. |
| `t_info_symbol_45` | `int` | Optional | Gets or sets the TInfoSymbol45 property. This property depends on the database field TInfoSymbol45. |
| `t_info_symbol_46` | `int` | Optional | Gets or sets the TInfoSymbol46 property. This property depends on the database field TInfoSymbol46. |
| `t_info_symbol_47` | `int` | Optional | Gets or sets the TInfoSymbol47 property. This property depends on the database field TInfoSymbol47. |
| `t_info_symbol_48` | `int` | Optional | Gets or sets the TInfoSymbol48 property. This property depends on the database field TInfoSymbol48. |
| `t_info_symbol_49` | `int` | Optional | Gets or sets the TInfoSymbol49 property. This property depends on the database field TInfoSymbol49. |
| `t_info_symbol_50` | `int` | Optional | Gets or sets the TInfoSymbol50 property. This property depends on the database field TInfoSymbol50. |
| `t_info_symbol_51` | `int` | Optional | Gets or sets the TInfoSymbol51 property. This property depends on the database field TInfoSymbol51. |
| `t_info_symbol_52` | `int` | Optional | Gets or sets the TInfoSymbol52 property. This property depends on the database field TInfoSymbol52. |
| `t_info_symbol_53` | `int` | Optional | Gets or sets the TInfoSymbol53 property. This property depends on the database field TInfoSymbol53. |
| `t_info_symbol_54` | `int` | Optional | Gets or sets the TInfoSymbol54 property. This property depends on the database field TInfoSymbol54. |
| `t_info_symbol_55` | `int` | Optional | Gets or sets the TInfoSymbol55 property. This property depends on the database field TInfoSymbol55. |
| `t_info_symbol_56` | `int` | Optional | Gets or sets the TInfoSymbol56 property. This property depends on the database field TInfoSymbol56. |
| `t_info_symbol_57` | `int` | Optional | Gets or sets the TInfoSymbol57 property. This property depends on the database field TInfoSymbol57. |
| `t_info_symbol_58` | `int` | Optional | Gets or sets the TInfoSymbol58 property. This property depends on the database field TInfoSymbol58. |
| `t_info_symbol_59` | `int` | Optional | Gets or sets the TInfoSymbol59 property. This property depends on the database field TInfoSymbol59. |
| `t_info_symbol_60` | `int` | Optional | Gets or sets the TInfoSymbol60 property. This property depends on the database field TInfoSymbol60. |

## Example (as JSON)

```json
{
  "cashPayment": "cashPayment6",
  "isCreditInvoiced": 88,
  "isInvoiceInvoiced": 0,
  "tourId": 112,
  "tourNo": 72
}
```

