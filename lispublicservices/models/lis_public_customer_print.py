# -*- coding: utf-8 -*-

"""
lispublicservices

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from lispublicservices.api_helper import APIHelper


class LISPublicCustomerPrint(object):

    """Implementation of the 'LISPublicCustomerPrint' model.

    The LISCustomerPrint data contract.

    Attributes:
        customer_id (int): Gets or sets CustomerId.
        group (int): Gets or sets Group.
        print_base (int): Gets or sets PrintBase.
        print_name (string): Gets or sets PrintName.
        contact_person_seq_no (int): Gets or sets ContactPersonSeqNo.
        changed_on (datetime): Gets or sets ChangedOn.
        changed_by (string): Gets or sets ChangedBy.
        employee_seq_no (int): Gets or sets EmployeeSeqNo.
        print_enabled (bool): Gets or sets PrintOriginalEnabled.
        print_original_enabled (bool): Gets or sets the print original
            enabled.
        print_copy_enabled (bool): TODO: type description here.
        fax_original_enabled (bool): Gets or sets FaxOriginalEnabled.
        send_mail_original_enabled (bool): Gets or sets
            SendMailOriginalEnabled.
        output_original_enabled (bool): Gets or sets OutputOriginalEnabled.
        blank_template_enabled (bool): Gets or sets BlankTemplateEnabled.
        number_of_copies (int): Gets or sets NumberOfCopies.
        override_print (bool): Gets or sets OverridePrint.
        dms_print_assigned (bool): Gets or sets DMSPrintAssigned.
        mail_cc (int): Gets or sets MailCC.
        mail_cc_text (string): Gets or sets MailCCText.
        subject_number (int): Gets or sets SubjectNumber.
        subject_text (string): Gets or sets SubjectText.
        changed_by_user (bool): Gets or sets a value indicating whether
            [changed by user].
        track_changes (bool): Gets or sets TrackChanges.
        has_changes (bool): Gets or sets HasChanges.
        additional_print (string): Gets or sets the additional print.
        additional_print_2 (string): Gets or sets the additional print 2.
        csv_view (string): Gets or sets a value indicating whether [CSV
            view].
        is_additional_print_created_by_repeat (bool): Gets or sets the is
            additional print created by repeat.
        is_preview_document_enabled (bool): Gets or sets a value indicating
            whether this instance is preview document enabled.
        is_mail_on_repeating_print_enabled (bool): Gets or sets a value
            indicating whether this instance is mail on repeating print
            enabled.
        ordered_account (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_id": 'customerId',
        "group": 'group',
        "print_base": 'printBase',
        "print_name": 'printName',
        "contact_person_seq_no": 'contactPersonSeqNo',
        "changed_on": 'changedOn',
        "changed_by": 'changedBy',
        "employee_seq_no": 'employeeSeqNo',
        "print_enabled": 'printEnabled',
        "print_original_enabled": 'printOriginalEnabled',
        "print_copy_enabled": 'printCopyEnabled',
        "fax_original_enabled": 'faxOriginalEnabled',
        "send_mail_original_enabled": 'sendMailOriginalEnabled',
        "output_original_enabled": 'outputOriginalEnabled',
        "blank_template_enabled": 'blankTemplateEnabled',
        "number_of_copies": 'numberOfCopies',
        "override_print": 'overridePrint',
        "dms_print_assigned": 'dmsPrintAssigned',
        "mail_cc": 'mailCC',
        "mail_cc_text": 'mailCCText',
        "subject_number": 'subjectNumber',
        "subject_text": 'subjectText',
        "changed_by_user": 'changedByUser',
        "track_changes": 'trackChanges',
        "has_changes": 'hasChanges',
        "additional_print": 'additionalPrint',
        "additional_print_2": 'additionalPrint2',
        "csv_view": 'csvView',
        "is_additional_print_created_by_repeat": 'isAdditionalPrintCreatedByRepeat',
        "is_preview_document_enabled": 'isPreviewDocumentEnabled',
        "is_mail_on_repeating_print_enabled": 'isMailOnRepeatingPrintEnabled',
        "ordered_account": 'orderedAccount'
    }

    _optionals = [
        'customer_id',
        'group',
        'print_base',
        'print_name',
        'contact_person_seq_no',
        'changed_on',
        'changed_by',
        'employee_seq_no',
        'print_enabled',
        'print_original_enabled',
        'print_copy_enabled',
        'fax_original_enabled',
        'send_mail_original_enabled',
        'output_original_enabled',
        'blank_template_enabled',
        'number_of_copies',
        'override_print',
        'dms_print_assigned',
        'mail_cc',
        'mail_cc_text',
        'subject_number',
        'subject_text',
        'changed_by_user',
        'track_changes',
        'has_changes',
        'additional_print',
        'additional_print_2',
        'csv_view',
        'is_additional_print_created_by_repeat',
        'is_preview_document_enabled',
        'is_mail_on_repeating_print_enabled',
        'ordered_account',
    ]

    def __init__(self,
                 customer_id=APIHelper.SKIP,
                 group=APIHelper.SKIP,
                 print_base=APIHelper.SKIP,
                 print_name=APIHelper.SKIP,
                 contact_person_seq_no=APIHelper.SKIP,
                 changed_on=APIHelper.SKIP,
                 changed_by=APIHelper.SKIP,
                 employee_seq_no=APIHelper.SKIP,
                 print_enabled=APIHelper.SKIP,
                 print_original_enabled=APIHelper.SKIP,
                 print_copy_enabled=APIHelper.SKIP,
                 fax_original_enabled=APIHelper.SKIP,
                 send_mail_original_enabled=APIHelper.SKIP,
                 output_original_enabled=APIHelper.SKIP,
                 blank_template_enabled=APIHelper.SKIP,
                 number_of_copies=APIHelper.SKIP,
                 override_print=APIHelper.SKIP,
                 dms_print_assigned=APIHelper.SKIP,
                 mail_cc=APIHelper.SKIP,
                 mail_cc_text=APIHelper.SKIP,
                 subject_number=APIHelper.SKIP,
                 subject_text=APIHelper.SKIP,
                 changed_by_user=APIHelper.SKIP,
                 track_changes=APIHelper.SKIP,
                 has_changes=APIHelper.SKIP,
                 additional_print=APIHelper.SKIP,
                 additional_print_2=APIHelper.SKIP,
                 csv_view=APIHelper.SKIP,
                 is_additional_print_created_by_repeat=APIHelper.SKIP,
                 is_preview_document_enabled=APIHelper.SKIP,
                 is_mail_on_repeating_print_enabled=APIHelper.SKIP,
                 ordered_account=APIHelper.SKIP):
        """Constructor for the LISPublicCustomerPrint class"""

        # Initialize members of the class
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if group is not APIHelper.SKIP:
            self.group = group 
        if print_base is not APIHelper.SKIP:
            self.print_base = print_base 
        if print_name is not APIHelper.SKIP:
            self.print_name = print_name 
        if contact_person_seq_no is not APIHelper.SKIP:
            self.contact_person_seq_no = contact_person_seq_no 
        if changed_on is not APIHelper.SKIP:
            self.changed_on = APIHelper.RFC3339DateTime(changed_on) if changed_on else None 
        if changed_by is not APIHelper.SKIP:
            self.changed_by = changed_by 
        if employee_seq_no is not APIHelper.SKIP:
            self.employee_seq_no = employee_seq_no 
        if print_enabled is not APIHelper.SKIP:
            self.print_enabled = print_enabled 
        if print_original_enabled is not APIHelper.SKIP:
            self.print_original_enabled = print_original_enabled 
        if print_copy_enabled is not APIHelper.SKIP:
            self.print_copy_enabled = print_copy_enabled 
        if fax_original_enabled is not APIHelper.SKIP:
            self.fax_original_enabled = fax_original_enabled 
        if send_mail_original_enabled is not APIHelper.SKIP:
            self.send_mail_original_enabled = send_mail_original_enabled 
        if output_original_enabled is not APIHelper.SKIP:
            self.output_original_enabled = output_original_enabled 
        if blank_template_enabled is not APIHelper.SKIP:
            self.blank_template_enabled = blank_template_enabled 
        if number_of_copies is not APIHelper.SKIP:
            self.number_of_copies = number_of_copies 
        if override_print is not APIHelper.SKIP:
            self.override_print = override_print 
        if dms_print_assigned is not APIHelper.SKIP:
            self.dms_print_assigned = dms_print_assigned 
        if mail_cc is not APIHelper.SKIP:
            self.mail_cc = mail_cc 
        if mail_cc_text is not APIHelper.SKIP:
            self.mail_cc_text = mail_cc_text 
        if subject_number is not APIHelper.SKIP:
            self.subject_number = subject_number 
        if subject_text is not APIHelper.SKIP:
            self.subject_text = subject_text 
        if changed_by_user is not APIHelper.SKIP:
            self.changed_by_user = changed_by_user 
        if track_changes is not APIHelper.SKIP:
            self.track_changes = track_changes 
        if has_changes is not APIHelper.SKIP:
            self.has_changes = has_changes 
        if additional_print is not APIHelper.SKIP:
            self.additional_print = additional_print 
        if additional_print_2 is not APIHelper.SKIP:
            self.additional_print_2 = additional_print_2 
        if csv_view is not APIHelper.SKIP:
            self.csv_view = csv_view 
        if is_additional_print_created_by_repeat is not APIHelper.SKIP:
            self.is_additional_print_created_by_repeat = is_additional_print_created_by_repeat 
        if is_preview_document_enabled is not APIHelper.SKIP:
            self.is_preview_document_enabled = is_preview_document_enabled 
        if is_mail_on_repeating_print_enabled is not APIHelper.SKIP:
            self.is_mail_on_repeating_print_enabled = is_mail_on_repeating_print_enabled 
        if ordered_account is not APIHelper.SKIP:
            self.ordered_account = ordered_account 

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

        customer_id = dictionary.get("customerId") if dictionary.get("customerId") else APIHelper.SKIP
        group = dictionary.get("group") if dictionary.get("group") else APIHelper.SKIP
        print_base = dictionary.get("printBase") if dictionary.get("printBase") else APIHelper.SKIP
        print_name = dictionary.get("printName") if dictionary.get("printName") else APIHelper.SKIP
        contact_person_seq_no = dictionary.get("contactPersonSeqNo") if dictionary.get("contactPersonSeqNo") else APIHelper.SKIP
        changed_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("changedOn")).datetime if dictionary.get("changedOn") else APIHelper.SKIP
        changed_by = dictionary.get("changedBy") if dictionary.get("changedBy") else APIHelper.SKIP
        employee_seq_no = dictionary.get("employeeSeqNo") if dictionary.get("employeeSeqNo") else APIHelper.SKIP
        print_enabled = dictionary.get("printEnabled") if "printEnabled" in dictionary.keys() else APIHelper.SKIP
        print_original_enabled = dictionary.get("printOriginalEnabled") if "printOriginalEnabled" in dictionary.keys() else APIHelper.SKIP
        print_copy_enabled = dictionary.get("printCopyEnabled") if "printCopyEnabled" in dictionary.keys() else APIHelper.SKIP
        fax_original_enabled = dictionary.get("faxOriginalEnabled") if "faxOriginalEnabled" in dictionary.keys() else APIHelper.SKIP
        send_mail_original_enabled = dictionary.get("sendMailOriginalEnabled") if "sendMailOriginalEnabled" in dictionary.keys() else APIHelper.SKIP
        output_original_enabled = dictionary.get("outputOriginalEnabled") if "outputOriginalEnabled" in dictionary.keys() else APIHelper.SKIP
        blank_template_enabled = dictionary.get("blankTemplateEnabled") if "blankTemplateEnabled" in dictionary.keys() else APIHelper.SKIP
        number_of_copies = dictionary.get("numberOfCopies") if dictionary.get("numberOfCopies") else APIHelper.SKIP
        override_print = dictionary.get("overridePrint") if "overridePrint" in dictionary.keys() else APIHelper.SKIP
        dms_print_assigned = dictionary.get("dmsPrintAssigned") if "dmsPrintAssigned" in dictionary.keys() else APIHelper.SKIP
        mail_cc = dictionary.get("mailCC") if dictionary.get("mailCC") else APIHelper.SKIP
        mail_cc_text = dictionary.get("mailCCText") if dictionary.get("mailCCText") else APIHelper.SKIP
        subject_number = dictionary.get("subjectNumber") if dictionary.get("subjectNumber") else APIHelper.SKIP
        subject_text = dictionary.get("subjectText") if dictionary.get("subjectText") else APIHelper.SKIP
        changed_by_user = dictionary.get("changedByUser") if "changedByUser" in dictionary.keys() else APIHelper.SKIP
        track_changes = dictionary.get("trackChanges") if "trackChanges" in dictionary.keys() else APIHelper.SKIP
        has_changes = dictionary.get("hasChanges") if "hasChanges" in dictionary.keys() else APIHelper.SKIP
        additional_print = dictionary.get("additionalPrint") if dictionary.get("additionalPrint") else APIHelper.SKIP
        additional_print_2 = dictionary.get("additionalPrint2") if dictionary.get("additionalPrint2") else APIHelper.SKIP
        csv_view = dictionary.get("csvView") if dictionary.get("csvView") else APIHelper.SKIP
        is_additional_print_created_by_repeat = dictionary.get("isAdditionalPrintCreatedByRepeat") if "isAdditionalPrintCreatedByRepeat" in dictionary.keys() else APIHelper.SKIP
        is_preview_document_enabled = dictionary.get("isPreviewDocumentEnabled") if "isPreviewDocumentEnabled" in dictionary.keys() else APIHelper.SKIP
        is_mail_on_repeating_print_enabled = dictionary.get("isMailOnRepeatingPrintEnabled") if "isMailOnRepeatingPrintEnabled" in dictionary.keys() else APIHelper.SKIP
        ordered_account = dictionary.get("orderedAccount") if dictionary.get("orderedAccount") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer_id,
                   group,
                   print_base,
                   print_name,
                   contact_person_seq_no,
                   changed_on,
                   changed_by,
                   employee_seq_no,
                   print_enabled,
                   print_original_enabled,
                   print_copy_enabled,
                   fax_original_enabled,
                   send_mail_original_enabled,
                   output_original_enabled,
                   blank_template_enabled,
                   number_of_copies,
                   override_print,
                   dms_print_assigned,
                   mail_cc,
                   mail_cc_text,
                   subject_number,
                   subject_text,
                   changed_by_user,
                   track_changes,
                   has_changes,
                   additional_print,
                   additional_print_2,
                   csv_view,
                   is_additional_print_created_by_repeat,
                   is_preview_document_enabled,
                   is_mail_on_repeating_print_enabled,
                   ordered_account)
