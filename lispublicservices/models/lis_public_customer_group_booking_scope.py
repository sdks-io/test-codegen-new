# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicCustomerGroupBookingScope(object):

    """Implementation of the 'LISPublicCustomerGroupBookingScope' model.

    The LISCustomerGroupBookingScope data contract.

    Attributes:
        create_foreign_credit_voucher_number_flag (bool): Gets or sets
            CreateForeignCreditVoucherNumberFlag.
        create_foreign_debit_voucher_number_flag (bool): Gets or sets
            CreateForeignDebitVoucherNumberFlag.
        switch_debit_print_to_stat_currency_flag (bool): Gets or sets
            SwitchDebitPrintToStatCurrencyFlag.
        switch_credit_print_to_stat_currency_flag (bool): Gets or sets
            SwitchCreditPrintToStatCurrencyFlag.
        supress_debit_generation_incoming_invoice_flag (bool): Gets or sets
            SupressDebitGenerationIncomingInvoiceFlag.
        supress_debit_generation_invoice_flag (bool): Gets or sets
            SupressDebitGenerationInvoiceFlag.
        supress_debit_generation_special_invoice_flag (bool): Gets or sets
            SupressDebitGenerationSpecialInvoiceFlag.
        supress_credit_generation_incoming_invoice_flag (bool): Gets or sets
            SupressCreditGenerationIncomingInvoiceFlag.
        supress_credit_generation_invoice_flag (bool): Gets or sets
            SupressCreditGenerationInvoiceFlag.
        supress_credit_generation_special_invoice_flag (bool): Gets or sets
            SupressCreditGenerationSpecialInvoiceFlag.
        finance_mandantor_crediting (int): Gets or sets
            FinanceMandantorCrediting.
        finance_mandantor_debiting (int): Gets or sets
            FinanceMandantorDebiting.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "create_foreign_credit_voucher_number_flag": 'createForeignCreditVoucherNumberFlag',
        "create_foreign_debit_voucher_number_flag": 'createForeignDebitVoucherNumberFlag',
        "switch_debit_print_to_stat_currency_flag": 'switchDebitPrintToStatCurrencyFlag',
        "switch_credit_print_to_stat_currency_flag": 'switchCreditPrintToStatCurrencyFlag',
        "supress_debit_generation_incoming_invoice_flag": 'supressDebitGenerationIncomingInvoiceFlag',
        "supress_debit_generation_invoice_flag": 'supressDebitGenerationInvoiceFlag',
        "supress_debit_generation_special_invoice_flag": 'supressDebitGenerationSpecialInvoiceFlag',
        "supress_credit_generation_incoming_invoice_flag": 'supressCreditGenerationIncomingInvoiceFlag',
        "supress_credit_generation_invoice_flag": 'supressCreditGenerationInvoiceFlag',
        "supress_credit_generation_special_invoice_flag": 'supressCreditGenerationSpecialInvoiceFlag',
        "finance_mandantor_crediting": 'financeMandantorCrediting',
        "finance_mandantor_debiting": 'financeMandantorDebiting'
    }

    _optionals = [
        'create_foreign_credit_voucher_number_flag',
        'create_foreign_debit_voucher_number_flag',
        'switch_debit_print_to_stat_currency_flag',
        'switch_credit_print_to_stat_currency_flag',
        'supress_debit_generation_incoming_invoice_flag',
        'supress_debit_generation_invoice_flag',
        'supress_debit_generation_special_invoice_flag',
        'supress_credit_generation_incoming_invoice_flag',
        'supress_credit_generation_invoice_flag',
        'supress_credit_generation_special_invoice_flag',
        'finance_mandantor_crediting',
        'finance_mandantor_debiting',
    ]

    def __init__(self,
                 create_foreign_credit_voucher_number_flag=APIHelper.SKIP,
                 create_foreign_debit_voucher_number_flag=APIHelper.SKIP,
                 switch_debit_print_to_stat_currency_flag=APIHelper.SKIP,
                 switch_credit_print_to_stat_currency_flag=APIHelper.SKIP,
                 supress_debit_generation_incoming_invoice_flag=APIHelper.SKIP,
                 supress_debit_generation_invoice_flag=APIHelper.SKIP,
                 supress_debit_generation_special_invoice_flag=APIHelper.SKIP,
                 supress_credit_generation_incoming_invoice_flag=APIHelper.SKIP,
                 supress_credit_generation_invoice_flag=APIHelper.SKIP,
                 supress_credit_generation_special_invoice_flag=APIHelper.SKIP,
                 finance_mandantor_crediting=APIHelper.SKIP,
                 finance_mandantor_debiting=APIHelper.SKIP):
        """Constructor for the LISPublicCustomerGroupBookingScope class"""

        # Initialize members of the class
        if create_foreign_credit_voucher_number_flag is not APIHelper.SKIP:
            self.create_foreign_credit_voucher_number_flag = create_foreign_credit_voucher_number_flag 
        if create_foreign_debit_voucher_number_flag is not APIHelper.SKIP:
            self.create_foreign_debit_voucher_number_flag = create_foreign_debit_voucher_number_flag 
        if switch_debit_print_to_stat_currency_flag is not APIHelper.SKIP:
            self.switch_debit_print_to_stat_currency_flag = switch_debit_print_to_stat_currency_flag 
        if switch_credit_print_to_stat_currency_flag is not APIHelper.SKIP:
            self.switch_credit_print_to_stat_currency_flag = switch_credit_print_to_stat_currency_flag 
        if supress_debit_generation_incoming_invoice_flag is not APIHelper.SKIP:
            self.supress_debit_generation_incoming_invoice_flag = supress_debit_generation_incoming_invoice_flag 
        if supress_debit_generation_invoice_flag is not APIHelper.SKIP:
            self.supress_debit_generation_invoice_flag = supress_debit_generation_invoice_flag 
        if supress_debit_generation_special_invoice_flag is not APIHelper.SKIP:
            self.supress_debit_generation_special_invoice_flag = supress_debit_generation_special_invoice_flag 
        if supress_credit_generation_incoming_invoice_flag is not APIHelper.SKIP:
            self.supress_credit_generation_incoming_invoice_flag = supress_credit_generation_incoming_invoice_flag 
        if supress_credit_generation_invoice_flag is not APIHelper.SKIP:
            self.supress_credit_generation_invoice_flag = supress_credit_generation_invoice_flag 
        if supress_credit_generation_special_invoice_flag is not APIHelper.SKIP:
            self.supress_credit_generation_special_invoice_flag = supress_credit_generation_special_invoice_flag 
        if finance_mandantor_crediting is not APIHelper.SKIP:
            self.finance_mandantor_crediting = finance_mandantor_crediting 
        if finance_mandantor_debiting is not APIHelper.SKIP:
            self.finance_mandantor_debiting = finance_mandantor_debiting 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        create_foreign_credit_voucher_number_flag = dictionary.get("createForeignCreditVoucherNumberFlag") if "createForeignCreditVoucherNumberFlag" in dictionary.keys() else APIHelper.SKIP
        create_foreign_debit_voucher_number_flag = dictionary.get("createForeignDebitVoucherNumberFlag") if "createForeignDebitVoucherNumberFlag" in dictionary.keys() else APIHelper.SKIP
        switch_debit_print_to_stat_currency_flag = dictionary.get("switchDebitPrintToStatCurrencyFlag") if "switchDebitPrintToStatCurrencyFlag" in dictionary.keys() else APIHelper.SKIP
        switch_credit_print_to_stat_currency_flag = dictionary.get("switchCreditPrintToStatCurrencyFlag") if "switchCreditPrintToStatCurrencyFlag" in dictionary.keys() else APIHelper.SKIP
        supress_debit_generation_incoming_invoice_flag = dictionary.get("supressDebitGenerationIncomingInvoiceFlag") if "supressDebitGenerationIncomingInvoiceFlag" in dictionary.keys() else APIHelper.SKIP
        supress_debit_generation_invoice_flag = dictionary.get("supressDebitGenerationInvoiceFlag") if "supressDebitGenerationInvoiceFlag" in dictionary.keys() else APIHelper.SKIP
        supress_debit_generation_special_invoice_flag = dictionary.get("supressDebitGenerationSpecialInvoiceFlag") if "supressDebitGenerationSpecialInvoiceFlag" in dictionary.keys() else APIHelper.SKIP
        supress_credit_generation_incoming_invoice_flag = dictionary.get("supressCreditGenerationIncomingInvoiceFlag") if "supressCreditGenerationIncomingInvoiceFlag" in dictionary.keys() else APIHelper.SKIP
        supress_credit_generation_invoice_flag = dictionary.get("supressCreditGenerationInvoiceFlag") if "supressCreditGenerationInvoiceFlag" in dictionary.keys() else APIHelper.SKIP
        supress_credit_generation_special_invoice_flag = dictionary.get("supressCreditGenerationSpecialInvoiceFlag") if "supressCreditGenerationSpecialInvoiceFlag" in dictionary.keys() else APIHelper.SKIP
        finance_mandantor_crediting = dictionary.get("financeMandantorCrediting") if dictionary.get("financeMandantorCrediting") else APIHelper.SKIP
        finance_mandantor_debiting = dictionary.get("financeMandantorDebiting") if dictionary.get("financeMandantorDebiting") else APIHelper.SKIP
        # Return an object of this model
        return cls(create_foreign_credit_voucher_number_flag,
                   create_foreign_debit_voucher_number_flag,
                   switch_debit_print_to_stat_currency_flag,
                   switch_credit_print_to_stat_currency_flag,
                   supress_debit_generation_incoming_invoice_flag,
                   supress_debit_generation_invoice_flag,
                   supress_debit_generation_special_invoice_flag,
                   supress_credit_generation_incoming_invoice_flag,
                   supress_credit_generation_invoice_flag,
                   supress_credit_generation_special_invoice_flag,
                   finance_mandantor_crediting,
                   finance_mandantor_debiting)
