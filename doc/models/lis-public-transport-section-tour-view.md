
# LIS Public Transport Section Tour View

Represents an entity class. This class depends on the database table #*V__TransSectionTour

## Structure

`LISPublicTransportSectionTourView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `traffic_mode_id` | `int` | Optional | Gets or sets the TrafficModeId property. This property depends on the database field Id. |
| `id_2` | `int` | Optional | Gets or sets the Id2 property. This property depends on the database field Id2. |
| `order_no` | `int` | Optional | Gets or sets the OrderNo property. This property depends on the database field AufNr. |
| `order_sub_number` | `int` | Optional | Gets or sets the OrderSubNumber property. This property depends on the database field AufUnterNr. |
| `order_input_type` | [`OrderInputTypeEnum`](../../doc/models/order-input-type-enum.md) | Optional | Gets or sets the OrderInputType property. This property depends on the database field ErfTyp. |
| `order_type` | [`OrderTypeEnum`](../../doc/models/order-type-enum.md) | Optional | Gets or sets the AufArt property. This property depends on the database field AufArt. |
| `tour_id` | `int` | Optional | Gets or sets the TourId property. This property depends on the database field TourIntNr. |
| `shipment_sequence` | `int` | Optional | Gets or sets the SVLfdNr property. This property depends on the database field SVLfdNr. |
| `shipment_mode` | `int` | Optional | Gets or sets the SVModus property. This property depends on the database field SVModus. |
| `division_id` | `int` | Optional | Gets or sets the DivisionId property. This property depends on the database field HAbtId. |
| `department_id` | `int` | Optional | Gets or sets the DepartmentId property. This property depends on the database field HBerId. |
| `bordero_id` | `int` | Optional | Gets or sets the BorderoId property. This property depends on the database field BordIntNr. |
| `bordero_id_extern` | `int` | Optional | Gets or sets the BordIntExt property. This property depends on the database field BordIntExt. |
| `tour_sequential_no` | `int` | Optional | Gets or sets the TourSequentialNo property. This property depends on the database field TourLfdNr. |
| `loading_customer_id` | `int` | Optional | Gets or sets the LoadingCustomerId property. This property depends on the database field BelNr. |
| `loading_locality_id` | `int` | Optional | Gets or sets the LoadingLocalityId property. This property depends on the database field BelId. |
| `loading_country_code` | `string` | Optional | Gets or sets the LoadingCountryCode property. This property depends on the database field BelLKZ. |
| `loading_zip` | `string` | Optional | Gets or sets the LoadingZip property. This property depends on the database field BelPlz. |
| `loading_city` | `string` | Optional | Gets or sets the LoadingCity property. This property depends on the database field BelOrt. |
| `loading_degt` | `string` | Optional | Gets or sets the BelDEGT property. This property depends on the database field BelDEGT. |
| `community_code` | `int` | Optional | Gets or sets the BelGTB property. This property depends on the database field BelGTB. |
| `loading_bsl` | `string` | Optional | Gets or sets the BelBSL property. This property depends on the database field BelBSL. |
| `consignee_id` | `int` | Optional | Gets or sets the ConsigneeId property. This property depends on the database field EmpNr. |
| `unloading_locality_id` | `int` | Optional | Gets or sets the UnloadingLocalityId property. This property depends on the database field EmgId. |
| `unloading_country_code` | `string` | Optional | Gets or sets the UnloadingCountryCode property. This property depends on the database field EmgLKZ. |
| `unloading_zip` | `string` | Optional | Gets or sets the UnloadingZip property. This property depends on the database field EmgPLZ. |
| `unloading_city` | `string` | Optional | Gets or sets the UnloadingCity property. This property depends on the database field EmgOrt. |
| `consignee_degt` | `string` | Optional | Gets or sets the EmgDEGT property. This property depends on the database field EmgDEGT. |
| `consignee_gtb` | `int` | Optional | Gets or sets the EmgGTB property. This property depends on the database field EmgGTB. |
| `consignee_bsl` | `string` | Optional | Gets or sets the EmgBSL property. This property depends on the database field EmgBSL. |
| `loading_date_from` | `datetime` | Optional | Gets or sets the BelVonDat property. This property depends on the database field BelVonDat. |
| `loading_time_from` | `datetime` | Optional | Gets or sets the BelVonZeit property. This property depends on the database field BelVonZeit. |
| `delivery_end_date` | `datetime` | Optional | Gets or sets the BelBisDat property. This property depends on the database field BelBisDat. |
| `delivery_end_time` | `datetime` | Optional | Gets or sets the BelBisZeit property. This property depends on the database field BelBisZeit. |
| `delvery_date_from` | `datetime` | Optional | Gets or sets the EntVonDat property. This property depends on the database field EntVonDat. |
| `delivery_time_from` | `datetime` | Optional | Gets or sets the EntVonZeit property. This property depends on the database field EntVonZeit. |
| `delivery_till_date` | `datetime` | Optional | Gets or sets the EntBisDat property. This property depends on the database field EntBisDat. |
| `delivery_till_time` | `datetime` | Optional | Gets or sets the TimeTill property. This property depends on the database field EntBisZeit. |
| `loading_dt_fix_from` | `datetime` | Optional | Gets or sets the BelFix property. This property depends on the database field BelFix. |
| `loading_dt_fix_till` | `datetime` | Optional | Gets or sets the BelFixBis property. This property depends on the database field BelFixBis. |
| `delivery_dt_fix_from` | `datetime` | Optional | Gets or sets the EntFix property. This property depends on the database field EntFix. |
| `delivery_dt_fix_till` | `datetime` | Optional | Gets or sets the EntFixBis property. This property depends on the database field EntFixBis. |
| `loading_dt_target_from` | `datetime` | Optional | Gets or sets the BelSollVon property. This property depends on the database field BelSollVon. |
| `loading_dt_target_till` | `datetime` | Optional | Gets or sets the BelSollBis property. This property depends on the database field BelSollBis. |
| `delivery_dt_target_from` | `datetime` | Optional | Gets or sets the EntSollVon property. This property depends on the database field EntSollVon. |
| `delivery_dt_target_till` | `datetime` | Optional | Gets or sets the EntSollBis property. This property depends on the database field EntSollBis. |
| `weight` | `float` | Optional | Gets or sets the Weight property. This property depends on the database field TatsGew. |
| `chargeable_weight` | `float` | Optional | Gets or sets the ChargeableWeight property. This property depends on the database field FpflGew. |
| `cubic_decimeter` | `float` | Optional | Gets or sets the CubicDecimeter property. This property depends on the database field CDMAnz. |
| `loading_meter` | `float` | Optional | Gets or sets the LoadingMeter property. This property depends on the database field LMAnz. |
| `square_meter` | `float` | Optional | Gets or sets the SquareMeter property. This property depends on the database field QMAnz. |
| `pallett_spaces_count` | `float` | Optional | Gets or sets the PallettSpacesCount property. This property depends on the database field SPAnzSum. |
| `target_weight` | `float` | Optional | Gets or sets the TargetWeight property. This property depends on the database field SolTGewSum. |
| `pallettes_count_sum` | `float` | Optional | Gets or sets the PalAnzSum property. This property depends on the database field PalAnzSum. |
| `packages_count_sum` | `float` | Optional | Gets or sets the ColliAnzSu property. This property depends on the database field ColliAnzSu. |
| `pieces_count_sum` | `float` | Optional | Gets or sets the MeAnzSum property. This property depends on the database field MeAnzSum. |
| `shipping_units` | `float` | Optional | Gets or sets the ShippingUnits property. This property depends on the database field NVEAnzSum. |
| `hazardous_good_qualified` | `string` | Optional | Gets or sets the HazardousGoodQualified property. This property depends on the database field Gefahrgut. |
| `reefer_cargo` | `string` | Optional | Gets or sets the ReeferCargo property. This property depends on the database field Kuehlgut. |
| `declared_value` | `float` | Optional | Gets or sets the DeclaredValue property. This property depends on the database field Warenwert. |
| `calculated_amount` | `float` | Optional | Gets or sets the CalculatedAmount property. This property depends on the database field ReNettoAnt. |
| `number_of_orders` | `int` | Optional | Gets or sets the NumberOfOrders property. This property depends on the database field AnzAuf. |
| `distance` | `float` | Optional | Gets or sets the KM property. This property depends on the database field Km. |
| `distance_section` | `float` | Optional | Gets or sets the KMGFT property. This property depends on the database field KmGFT. |
| `distance_load` | `float` | Optional | Gets or sets the Distance property. This property depends on the database field KmLast. |
| `distance_toll` | `float` | Optional | Gets or sets the DistanceToll property. This property depends on the database field KmMaut. |
| `distance_empty` | `float` | Optional | Gets or sets the DistanceEmpty property. This property depends on the database field KmLeer. |
| `distance_toll_empty` | `float` | Optional | Gets or sets the DistanceTollEmpty property. This property depends on the database field KmLeerMaut. |
| `dispo_approval` | `int` | Optional | Gets or sets the DispoApproval property. This property depends on the database field DispoApproval. |
| `sl_order_info_symbol_order_id` | `int` | Optional | Gets or sets the SLAufInfSymAufIntNr property. This property depends on the database field SLAufInfSymAufIntNr. |
| `info_symbol_1` | `int` | Optional | Gets or sets the InfoSymbol1 property. This property depends on the database field InfoSymbol1. |
| `info_symbol_2` | `int` | Optional | Gets or sets the InfoSymbol2 property. This property depends on the database field InfoSymbol2. |
| `info_symbol_3` | `int` | Optional | Gets or sets the InfoSymbol3 property. This property depends on the database field InfoSymbol3. |
| `info_symbol_4` | `int` | Optional | Gets or sets the InfoSymbol4 property. This property depends on the database field InfoSymbol4. |
| `info_symbol_5` | `int` | Optional | Gets or sets the InfoSymbol5 property. This property depends on the database field InfoSymbol5. |
| `info_symbol_6` | `int` | Optional | Gets or sets the InfoSymbol6 property. This property depends on the database field InfoSymbol6. |
| `info_symbol_7` | `int` | Optional | Gets or sets the InfoSymbol7 property. This property depends on the database field InfoSymbol7. |
| `info_symbol_8` | `int` | Optional | Gets or sets the InfoSymbol8 property. This property depends on the database field InfoSymbol8. |
| `info_symbol_9` | `int` | Optional | Gets or sets the InfoSymbol9 property. This property depends on the database field InfoSymbol9. |
| `info_symbol_10` | `int` | Optional | Gets or sets the InfoSymbol10 property. This property depends on the database field InfoSymbol10. |
| `info_symbol_11` | `int` | Optional | Gets or sets the InfoSymbol11 property. This property depends on the database field InfoSymbol11. |
| `info_symbol_12` | `int` | Optional | Gets or sets the InfoSymbol12 property. This property depends on the database field InfoSymbol12. |
| `info_symbol_13` | `int` | Optional | Gets or sets the InfoSymbol13 property. This property depends on the database field InfoSymbol13. |
| `info_symbol_14` | `int` | Optional | Gets or sets the InfoSymbol14 property. This property depends on the database field InfoSymbol14. |
| `info_symbol_15` | `int` | Optional | Gets or sets the InfoSymbol15 property. This property depends on the database field InfoSymbol15. |
| `info_symbol_16` | `int` | Optional | Gets or sets the InfoSymbol16 property. This property depends on the database field InfoSymbol16. |
| `info_symbol_17` | `int` | Optional | Gets or sets the InfoSymbol17 property. This property depends on the database field InfoSymbol17. |
| `info_symbol_18` | `int` | Optional | Gets or sets the InfoSymbol18 property. This property depends on the database field InfoSymbol18. |
| `info_symbol_19` | `int` | Optional | Gets or sets the InfoSymbol19 property. This property depends on the database field InfoSymbol19. |
| `info_symbol_20` | `int` | Optional | Gets or sets the InfoSymbol20 property. This property depends on the database field InfoSymbol20. |
| `info_symbol_21` | `int` | Optional | Gets or sets the InfoSymbol21 property. This property depends on the database field InfoSymbol21. |
| `info_symbol_22` | `int` | Optional | Gets or sets the InfoSymbol22 property. This property depends on the database field InfoSymbol22. |
| `info_symbol_23` | `int` | Optional | Gets or sets the InfoSymbol23 property. This property depends on the database field InfoSymbol23. |
| `info_symbol_24` | `int` | Optional | Gets or sets the InfoSymbol24 property. This property depends on the database field InfoSymbol24. |
| `info_symbol_25` | `int` | Optional | Gets or sets the InfoSymbol25 property. This property depends on the database field InfoSymbol25. |
| `info_symbol_26` | `int` | Optional | Gets or sets the InfoSymbol26 property. This property depends on the database field InfoSymbol26. |
| `info_symbol_27` | `int` | Optional | Gets or sets the InfoSymbol27 property. This property depends on the database field InfoSymbol27. |
| `info_symbol_28` | `int` | Optional | Gets or sets the InfoSymbol28 property. This property depends on the database field InfoSymbol28. |
| `info_symbol_29` | `int` | Optional | Gets or sets the InfoSymbol29 property. This property depends on the database field InfoSymbol29. |
| `info_symbol_30` | `int` | Optional | Gets or sets the InfoSymbol30 property. This property depends on the database field InfoSymbol30. |
| `info_symbol_31` | `int` | Optional | Gets or sets the InfoSymbol31 property. This property depends on the database field InfoSymbol31. |
| `info_symbol_32` | `int` | Optional | Gets or sets the InfoSymbol32 property. This property depends on the database field InfoSymbol32. |
| `info_symbol_33` | `int` | Optional | Gets or sets the InfoSymbol33 property. This property depends on the database field InfoSymbol33. |
| `info_symbol_34` | `int` | Optional | Gets or sets the InfoSymbol34 property. This property depends on the database field InfoSymbol34. |
| `info_symbol_35` | `int` | Optional | Gets or sets the InfoSymbol35 property. This property depends on the database field InfoSymbol35. |
| `info_symbol_36` | `int` | Optional | Gets or sets the InfoSymbol36 property. This property depends on the database field InfoSymbol36. |
| `info_symbol_37` | `int` | Optional | Gets or sets the InfoSymbol37 property. This property depends on the database field InfoSymbol37. |
| `info_symbol_38` | `int` | Optional | Gets or sets the InfoSymbol38 property. This property depends on the database field InfoSymbol38. |
| `info_symbol_39` | `int` | Optional | Gets or sets the InfoSymbol39 property. This property depends on the database field InfoSymbol39. |
| `info_symbol_40` | `int` | Optional | Gets or sets the InfoSymbol40 property. This property depends on the database field InfoSymbol40. |
| `info_symbol_41` | `int` | Optional | Gets or sets the InfoSymbol41 property. This property depends on the database field InfoSymbol41. |
| `info_symbol_42` | `int` | Optional | Gets or sets the InfoSymbol42 property. This property depends on the database field InfoSymbol42. |
| `info_symbol_43` | `int` | Optional | Gets or sets the InfoSymbol43 property. This property depends on the database field InfoSymbol43. |
| `info_symbol_44` | `int` | Optional | Gets or sets the InfoSymbol44 property. This property depends on the database field InfoSymbol44. |
| `info_symbol_45` | `int` | Optional | Gets or sets the InfoSymbol45 property. This property depends on the database field InfoSymbol45. |
| `info_symbol_46` | `int` | Optional | Gets or sets the InfoSymbol46 property. This property depends on the database field InfoSymbol46. |
| `info_symbol_47` | `int` | Optional | Gets or sets the InfoSymbol47 property. This property depends on the database field InfoSymbol47. |
| `info_symbol_48` | `int` | Optional | Gets or sets the InfoSymbol48 property. This property depends on the database field InfoSymbol48. |
| `info_symbol_49` | `int` | Optional | Gets or sets the InfoSymbol49 property. This property depends on the database field InfoSymbol49. |
| `info_symbol_50` | `int` | Optional | Gets or sets the InfoSymbol50 property. This property depends on the database field InfoSymbol50. |
| `info_symbol_51` | `int` | Optional | Gets or sets the InfoSymbol51 property. This property depends on the database field InfoSymbol51. |
| `info_symbol_52` | `int` | Optional | Gets or sets the InfoSymbol52 property. This property depends on the database field InfoSymbol52. |
| `info_symbol_53` | `int` | Optional | Gets or sets the InfoSymbol53 property. This property depends on the database field InfoSymbol53. |
| `info_symbol_54` | `int` | Optional | Gets or sets the InfoSymbol54 property. This property depends on the database field InfoSymbol54. |
| `info_symbol_55` | `int` | Optional | Gets or sets the InfoSymbol55 property. This property depends on the database field InfoSymbol55. |
| `info_symbol_56` | `int` | Optional | Gets or sets the InfoSymbol56 property. This property depends on the database field InfoSymbol56. |
| `info_symbol_57` | `int` | Optional | Gets or sets the InfoSymbol57 property. This property depends on the database field InfoSymbol57. |
| `info_symbol_58` | `int` | Optional | Gets or sets the InfoSymbol58 property. This property depends on the database field InfoSymbol58. |
| `info_symbol_59` | `int` | Optional | Gets or sets the InfoSymbol59 property. This property depends on the database field InfoSymbol59. |
| `info_symbol_60` | `int` | Optional | Gets or sets the InfoSymbol60 property. This property depends on the database field InfoSymbol60. |
| `dispatch_calc_load_date_from` | `datetime` | Optional | Gets or sets the DispatchCalcLoadDateFrom property. This property depends on the database field DispatchCalcLoadDateFrom. |
| `dispatch_calc_load_time_from` | `datetime` | Optional | Gets or sets the DispatchCalcLoadTimeFrom property. This property depends on the database field DispatchCalcLoadTimeFrom. |
| `dispatch_calc_load_date_till` | `datetime` | Optional | Gets or sets the DispatchCalcLoadDateTill property. This property depends on the database field DispatchCalcLoadDateTill. |
| `dispatch_calc_load_time_till` | `datetime` | Optional | Gets or sets the DispatchCalcLoadTimeTill property. This property depends on the database field DispatchCalcLoadTimeTill. |
| `dispatch_calc_unload_date_from` | `datetime` | Optional | Gets or sets the DispatchCalcUnloadDateFrom property. This property depends on the database field DispatchCalcUnloadDateFrom. |
| `dispatch_calc_unload_time_from` | `datetime` | Optional | Gets or sets the DispatchCalcUnloadTimeFrom property. This property depends on the database field DispatchCalcUnloadTimeFrom. |
| `dispatch_calc_unload_date_till` | `datetime` | Optional | Gets or sets the DispatchCalcUnloadDateTill property. This property depends on the database field DispatchCalcUnloadDateTill. |
| `dispatch_calc_unload_time_till` | `datetime` | Optional | Gets or sets the DispatchCalcUnloadTimeTill property. This property depends on the database field DispatchCalcUnloadTimeTill. |
| `dispatch_man_load_date_from` | `datetime` | Optional | Gets or sets the DispatchManLoadDateFrom property. This property depends on the database field DispatchManLoadDateFrom. |
| `dispatch_man_load_time_from` | `datetime` | Optional | Gets or sets the DispatchManLoadTimeFrom property. This property depends on the database field DispatchManLoadTimeFrom. |
| `dispatch_man_load_date_till` | `datetime` | Optional | Gets or sets the DispatchManLoadDateTill property. This property depends on the database field DispatchManLoadDateTill. |
| `dispatch_man_load_time_till` | `datetime` | Optional | Gets or sets the DispatchManLoadTimeTill property. This property depends on the database field DispatchManLoadTimeTill. |
| `dispatch_man_unload_date_from` | `datetime` | Optional | Gets or sets the DispatchManUnloadDateFrom property. This property depends on the database field DispatchManUnloadDateFrom. |
| `dispatch_man_unload_time_from` | `datetime` | Optional | Gets or sets the DispatchManUnloadTimeFrom property. This property depends on the database field DispatchManUnloadTimeFrom. |
| `dispatch_man_unload_date_till` | `datetime` | Optional | Gets or sets the DispatchManUnloadDateTill property. This property depends on the database field DispatchManUnloadDateTill. |
| `dispatch_man_unload_time_till` | `datetime` | Optional | Gets or sets the DispatchManUnloadTimeTill property. This property depends on the database field DispatchManUnloadTimeTill. |
| `prev_auf_int_nr` | `int` | Optional | Gets or sets the PrevAufIntNr property. This property depends on the database field PrevAufIntNr. |
| `prev_tour_int_nr` | `int` | Optional | Gets or sets the PrevTourIntNr property. This property depends on the database field PrevTourIntNr. |
| `prev_tour_nr` | `int` | Optional | Gets or sets the PrevTourNr property. This property depends on the database field PrevTourNr. |
| `prev_dispatch_calc_date_till` | `datetime` | Optional | Gets or sets the PrevDispatchCalcDateTill property. This property depends on the database field PrevDispatchCalcDateTill. |
| `prev_dispatch_calc_time_till` | `datetime` | Optional | Gets or sets the PrevDispatchCalcTimeTill property. This property depends on the database field PrevDispatchCalcTimeTill. |
| `loading_sequence_station_no` | `int` | Optional | Gets or sets the LoadingSequenceStationNo property. This property depends on the database field LoadingSequenceStationNo. |
| `unloading_sequence_station_no` | `int` | Optional | Gets or sets the UnloadingSequenceStationNo property. This property depends on the database field UnloadingSequenceStationNo. |

## Example (as JSON)

```json
{
  "trafficModeId": 38,
  "id2": 94,
  "orderNo": 128,
  "orderSubNumber": 158,
  "orderInputType": "NotSet"
}
```

