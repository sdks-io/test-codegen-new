
# LIS Public Customer Base View

Represents an entity class. This class depends on the database table

## Structure

`LISPublicCustomerBaseView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Optional | Gets or sets the CustomerId property. This property depends on the database field KundenNr. |
| `customer_short` | `string` | Optional | Gets or sets the CustomerShort property. This property depends on the database field KunShort. |
| `name_1` | `string` | Optional | Gets or sets the Name1 property. This property depends on the database field Name1. |
| `name_2` | `string` | Optional | Gets or sets the Name2 property. This property depends on the database field Name2. |
| `name_3` | `string` | Optional | Gets or sets the Name3 property. This property depends on the database field Name3. |
| `street` | `string` | Optional | Gets or sets the Street property. This property depends on the database field Strasse. |
| `country_code` | `string` | Optional | Gets or sets the CountryCode property. This property depends on the database field LKZ. |
| `zip_code` | `string` | Optional | Gets or sets the ZipCode property. This property depends on the database field PLZ. |
| `city_code` | `string` | Optional | Gets or sets the LKZPLZ property. This property depends on the database field LKZPLZ. |
| `city` | `string` | Optional | Gets or sets the City property. This property depends on the database field Ort. |
| `city_district` | `string` | Optional | Gets or sets the CityDistrict property. This property depends on the database field Ortsteil. |
| `i_loc_nr` | `string` | Optional | Gets or sets the iLocNr property. This property depends on the database field iLocNr. |
| `phone` | `string` | Optional | Gets or sets the Phone property. This property depends on the database field Tel. |
| `vehicle_phone` | `string` | Optional | Gets or sets the VehiclePhone property. This property depends on the database field TelAuto. |
| `fax` | `string` | Optional | Gets or sets the Fax property. This property depends on the database field Fax. |
| `administrator` | `string` | Optional | Gets or sets the Administrator property. This property depends on the database field Sachbearb. |
| `homepage` | `string` | Optional | Gets or sets the Homepage property. This property depends on the database field Homepage. |
| `email` | `string` | Optional | Gets or sets the email property. This property depends on the database field eMail. |
| `end_customer` | `int` | Optional | Gets or sets the EndKunde property. This property depends on the database field EndKunde. |
| `ust_id` | `string` | Optional | Gets or sets the UstId property. This property depends on the database field UstId. |
| `tax_id` | `string` | Optional | Gets or sets the SteuerNr property. This property depends on the database field SteuerNr. |
| `l_st_name_1` | `string` | Optional | Gets or sets the LStName1 property. This property depends on the database field LstName1. |
| `l_st_name_2` | `string` | Optional | Gets or sets the LStName2 property. This property depends on the database field LstName2. |
| `l_st_name_3` | `string` | Optional | Gets or sets the LStName3 property. This property depends on the database field LstName3. |
| `lst_street` | `string` | Optional | Gets or sets the LStStrasse property. This property depends on the database field LstStrasse. |
| `lst_country_code` | `string` | Optional | Gets or sets the LstLKZ property. This property depends on the database field LstLKZ. |
| `lst_zip_code` | `string` | Optional | Gets or sets the LstPLZ property. This property depends on the database field LstPLZ. |
| `lst_country_code_zip` | `string` | Optional | Gets or sets the LstLKZPLZ property. This property depends on the database field LstLKZPLZ. |
| `lst_city` | `string` | Optional | Gets or sets the LstOrt property. This property depends on the database field LstOrt. |
| `lst_city_district` | `string` | Optional | Gets or sets the LstOrtsteil property. This property depends on the database field LstOrtsteil. |
| `account_table` | `int` | Optional | Gets or sets the AccountTable property. This property depends on the database field KtoTab. |
| `cost_center` | `int` | Optional | Gets or sets the CostCenter property. This property depends on the database field KStelle. |
| `cost_unit` | `int` | Optional | Gets or sets the CostUnit property. This property depends on the database field KTraeger. |
| `sales_tax_code` | `string` | Optional | Gets or sets the SalesTaxCode property. This property depends on the database field UC. |
| `is_invoicing_blocked_for_new_orders` | `string` | Optional | Gets or sets the FakSperr property. This property depends on the database field FakSperr. |
| `blocked_until` | `datetime` | Optional | Gets or sets the BlockedUntil property. This property depends on the database field SperrDat. |
| `invoice_division_id` | `int` | Optional | Gets or sets the InvoiceDivisionId property. This property depends on the database field ReAbtID. |
| `invoice_department_id` | `int` | Optional | Gets or sets the InvoiceDepartmentId property. This property depends on the database field ReBerID. |
| `km_methode` | `string` | Optional | Gets or sets the KmMethode property. This property depends on the database field KmMethode. |
| `condition_type` | `string` | Optional | Gets or sets the ReKond property. This property depends on the database field ReKond. |
| `credit_condition_type` | `string` | Optional | Gets or sets the GsKond property. This property depends on the database field GSKond. |
| `optimization_type` | `string` | Optional | Gets or sets the ReOptKz property. This property depends on the database field ReOptKz. |
| `credit_optimization_type` | `string` | Optional | Gets or sets the GsOptKz property. This property depends on the database field GSOptKz. |
| `cargo_insurance` | `string` | Optional | Gets or sets the ReKunVB property. This property depends on the database field ReKunVB. |
| `gs_customer_insurance` | `string` | Optional | Gets or sets the GsKunVB property. This property depends on the database field GsKunVB. |
| `general_condition_customer_id` | `int` | Optional | Gets or sets the ReAllgKond property. This property depends on the database field ReAllgKond. |
| `general_creditor` | `int` | Optional | Gets or sets the GsAllgKond property. This property depends on the database field GsAllgKond. |
| `print_debit` | `string` | Optional | Gets or sets the ReDruck property. This property depends on the database field ReDruck. |
| `print_credit` | `string` | Optional | Gets or sets the GsDruck property. This property depends on the database field GSDruck. |
| `debit_form_type` | `int` | Optional | Gets or sets the ReFormTyp property. This property depends on the database field ReFormTyp. |
| `credit_form_type` | `int` | Optional | Gets or sets the GsFormTyp property. This property depends on the database field GsFormTyp. |
| `special_invoice_debit_form_type` | `int` | Optional | Gets or sets the SFReFormTyp property. This property depends on the database field SFReFormTyp. |
| `special_invoice_credit_form_type` | `int` | Optional | Gets or sets the SFGsFormTyp property. This property depends on the database field SFGsFormTyp. |
| `debit_print_currency` | `string` | Optional | Gets or sets the ReWKurz property. This property depends on the database field ReWKurz. |
| `credit_print_currency` | `string` | Optional | Gets or sets the GsWKurz property. This property depends on the database field GSWKurz. |
| `aggregated_print_debit` | `string` | Optional | Gets or sets the ReSammel property. This property depends on the database field ReSammel. |
| `aggregated_print_credit` | `string` | Optional | Gets or sets the GsSammel property. This property depends on the database field GSSammel. |
| `differing_voucher_recipient_debit` | `int` | Optional | Gets or sets the ReFANr property. This property depends on the database field ReFANr. |
| `differing_voucher_recipient_credit` | `int` | Optional | Gets or sets the GsFANr property. This property depends on the database field GSFANr. |
| `incoming_debit` | `string` | Optional | Gets or sets the ReEinBeleg property. This property depends on the database field ReEinBeleg. |
| `incoming_credit` | `string` | Optional | Gets or sets the GsEinBeleg property. This property depends on the database field GSEinBeleg. |
| `creditor_account_number` | `int` | Optional | Gets or sets the KtoKre property. This property depends on the database field KtoKre. |
| `debitor_account_number` | `int` | Optional | Gets or sets the KtoDeb property. This property depends on the database field KtoDeb. |
| `creditor_account` | `string` | Optional | Gets or sets the KtoKreA property. This property depends on the database field KtoKreA. |
| `debitor_account` | `string` | Optional | Gets or sets the KtoDebA property. This property depends on the database field KtoDebA. |
| `debit_booking` | `int` | Optional | Gets or sets the ReVerbuchD property. This property depends on the database field ReVerbuchD. |
| `credit_booking` | `int` | Optional | Gets or sets the GsVerbuchD property. This property depends on the database field GSVerbuchD. |
| `group` | `string` | Optional | Gets or sets the Gruppe property. This property depends on the database field Gruppe. |
| `created_on` | `datetime` | Optional | Gets or sets the CreatedOn property. This property depends on the database field ErstDat. |
| `created_by` | `string` | Optional | Gets or sets the CreatedBy property. This property depends on the database field ErstUs. |
| `changed_on` | `datetime` | Optional | Gets or sets the ChangedOn property. This property depends on the database field AendDat. |
| `changed_by` | `string` | Optional | Gets or sets the ChangedBy property. This property depends on the database field AendUs. |
| `business` | `string` | Optional | Gets or sets the Branche property. This property depends on the database field Branche. |
| `code` | `string` | Optional | Gets or sets the Code property. This property depends on the database field Code. |
| `terms_of_payment` | `int` | Optional | Gets or sets the TermsOfPayment property. This property depends on the database field ZahlBed. |
| `limit_debit` | `int` | Optional | Gets or sets the KreditLimi property. This property depends on the database field KreditLimi. |
| `no_dunning` | `int` | Optional | Gets or sets the NoMahn property. This property depends on the database field NoMahn. |
| `print_schedule` | `string` | Optional | Gets or sets the LmKtoAnh property. This property depends on the database field LmKtoAnh. |
| `mprint` | `string` | Optional | Gets or sets the LmKtoDruck property. This property depends on the database field LmKtoDruck. |
| `ledger_account` | `string` | Optional | Gets or sets the LmGegenKto property. This property depends on the database field LmGegenKto. |
| `reminder` | `string` | Optional | Gets or sets the LmAnmahn property. This property depends on the database field LmAnMahn. |
| `bank_code` | `string` | Optional | Gets or sets the BvBLZ property. This property depends on the database field BvBLZ. |
| `bank_account_number` | `string` | Optional | Gets or sets the BvKtoNr property. This property depends on the database field BvKtoNr. |
| `international_bank_account_number` | `string` | Optional | Gets or sets the BvIBAN property. This property depends on the database field BvIBAN. |
| `swift_code` | `string` | Optional | Gets or sets the BvSWIFT property. This property depends on the database field BvSWIFT. |
| `bank_name` | `string` | Optional | Gets or sets the BvBankname property. This property depends on the database field BvBankname. |
| `print_co_2_emissions` | `int` | Optional | Gets or sets the AntCO2Dru property. This property depends on the database field AntCO2Dru. |
| `average_emissions` | `float` | Optional | Gets or sets the EmiCO2 property. This property depends on the database field EmiCO2. |
| `fuel_type` | `int` | Optional | Gets or sets the FuelType property. This property depends on the database field FuelType. |
| `av_consumption` | `float` | Optional | Gets or sets the AVConsumption property. This property depends on the database field AVConsumption. |
| `object_id` | `uuid\|string` | Optional | - |
| `is_new` | `bool` | Optional | - |
| `original_hash_snapshot` | `string` | Optional | - |
| `original_snapshot` | `object` | Optional | - |
| `current_snapshot` | `object` | Optional | - |
| `meta_info` | [`LISMetaInfoCollection`](../../doc/models/lis-meta-info-collection.md) | Optional | - |

## Example (as JSON)

```json
{
  "objectId": "00000000-0000-0000-0000-000000000000",
  "customerId": 114,
  "customerShort": "customerShort0",
  "name1": "name10",
  "name2": "name24",
  "name3": "name34"
}
```

