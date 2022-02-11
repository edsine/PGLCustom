# -*- coding: utf-8 -*-

from odoo import models, fields


# class pgl-custom(models.Model):
#     _name = 'pgl-custom.pgl-custom'
#     _description = 'pgl-custom.pgl-custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    project_category = fields.Selection([
        ('public_sector', 'Public Sector'),
        ('private_sector', 'Private Sector'),
    ], required=True)


class Hr(models.Model):

    _inherit = 'hr.employee'

    # General

    title = fields.Selection([
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms')
    ], required=True)

    # End General

    # Dependant

    name_of_children = fields.Char()

    # End Dependant

    # Emergency
    emergency_relationship = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])

    emergency_relationship_2 = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])

    emergency_contact_2 = fields.Char()
    emergency_phone = fields.Char()

    # End Emergency

    # Education

    edu_name_of_institution_1 = fields.Char()
    edu_subject_study_1 = fields.Char()
    edu_qualification_1 = fields.Char()
    edu_start_date_1 = fields.Date()
    edu_end_date_1 = fields.Date()

    edu_name_of_institution_2 = fields.Char()
    edu_subject_study_2 = fields.Char()
    edu_qualification_2 = fields.Char()
    edu_start_date_2 = fields.Date()
    edu_end_date_2 = fields.Date()

    edu_name_of_institution_3 = fields.Char()
    edu_subject_study_3 = fields.Char()
    edu_qualification_3 = fields.Char()
    edu_start_date_3 = fields.Date()
    edu_end_date_3 = fields.Date()

    edu_name_of_institution_4 = fields.Char()
    edu_subject_study_4 = fields.Char()
    edu_qualification_4 = fields.Char()
    edu_start_date_4 = fields.Date()
    edu_end_date_4 = fields.Date()

    # End Education

    # Professional Qualifications

    prof_name_of_institution_1 = fields.Char()
    prof_certificate_obtained_1 = fields.Char()
    prof_class_of_certification_1 = fields.Char()
    prof_start_date_1 = fields.Date()
    prof_end_date_1 = fields.Date()

    prof_name_of_institution_2 = fields.Char()
    prof_certificate_obtained_2 = fields.Char()
    prof_class_of_certification_2 = fields.Char()
    prof_start_date_2 = fields.Date()
    prof_end_date_2 = fields.Date()

    prof_name_of_institution_3 = fields.Char()
    prof_certificate_obtained_3 = fields.Char()
    prof_class_of_certification_3 = fields.Char()
    prof_start_date_3 = fields.Date()
    prof_end_date_3 = fields.Date()

    prof_name_of_institution_4 = fields.Char()
    prof_certificate_obtained_4 = fields.Char()
    prof_class_of_certification_4 = fields.Char()
    prof_start_date_4 = fields.Date()
    prof_end_date_4 = fields.Date()

    # End Professional Qualifications

    # Employment History

    emp_history_organization_1 = fields.Char()
    emp_history_role_1 = fields.Char()
    emp_history_contact_name_1 = fields.Char()
    emp_history_phone_number_1 = fields.Char()
    emp_history_start_date_1 = fields.Date()
    emp_history_end_date_1 = fields.Date()
    emp_reason_for_leaving_1 = fields.Char()

    emp_history_organization_2 = fields.Char()
    emp_history_role_2 = fields.Char()
    emp_history_contact_name_2 = fields.Char()
    emp_history_phone_number_2 = fields.Char()
    emp_history_start_date_2 = fields.Date()
    emp_history_end_date_2 = fields.Date()
    emp_reason_for_leaving_2 = fields.Char()

    emp_history_organization_3 = fields.Char()
    emp_history_role_3 = fields.Char()
    emp_history_contact_name_3 = fields.Char()
    emp_history_phone_number_3 = fields.Char()
    emp_history_start_date_3 = fields.Date()
    emp_history_end_date_3 = fields.Date()
    emp_reason_for_leaving_3 = fields.Char()

    emp_history_organization_4 = fields.Char()
    emp_history_role_4 = fields.Char()
    emp_history_contact_name_4 = fields.Char()
    emp_history_phone_number_4 = fields.Char()
    emp_history_start_date_4 = fields.Date()
    emp_history_end_date_4 = fields.Date()
    emp_reason_for_leaving_4 = fields.Char()

    working_relatives = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])
    working_relatives_name_1 = fields.Char()
    working_relatives_relationship_1 = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])
    working_relatives_name_2 = fields.Char()
    working_relatives_relationship_2 = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])

    # End Employment History

    # Security

    months_lived = fields.Integer()
    years_lived = fields.Integer()

    conviction = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])
    conviction_details = fields.Char()

    driving_license = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])

    work_in_other_states = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])

    background_check = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
    ])

    # End Security

    # References

    reference_name_1 = fields.Char()
    reference_phone_number_1 = fields.Char()
    references_relationship_1 = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])
    years_known_1 = fields.Integer()
    best_call_time_1 = fields.Selection([
        ('AM', 'AM'),
        ('PM', 'PM'),
    ])

    reference_name_2 = fields.Char()
    reference_phone_number_2 = fields.Char()
    references_relationship_2 = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])
    years_known_2 = fields.Integer()
    best_call_time_2 = fields.Selection([
        ('AM', 'AM'),
        ('PM', 'PM'),
    ])

    reference_name_3 = fields.Char()
    reference_phone_number_3 = fields.Char()
    references_relationship_3 = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    ])
    years_known_3 = fields.Integer()
    best_call_time_3 = fields.Selection([
        ('AM', 'AM'),
        ('PM', 'PM'),
    ])

    # End References
    
    
    # Guarantor
    
    guarantor_name = fields.Char()
    guarantor_nin = fields.Integer()
    guarantor_address = fields.Char()
    guarantor_phone = fields.Char()
    guarantor_email = fields.Char()
    guarantor_current_emp_buss = fields.Char()
    guarantor_emp_buss_address = fields.Char()
    guarantor_job_title = fields.Char()
    
    
    
    # End Guarantor
