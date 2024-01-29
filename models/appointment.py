# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DentalAppointment(models.Model):
    _name = 'dental.appointment'
    _description = 'Dental Appointment Records'

    name = fields.Many2one(
        'res.partner', 
        string='Patient', 
        required=True
    )
    
    doctor = fields.Many2one(
        'res.partner', 
        string='Doctor'
    )
    
    service = fields.Many2one(
        'dental.service', 
        string='Service'
    )
 
    state = fields.Selection(
        string='State', 
        selection=[
            ('new', 'New'), 
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        ],
        default='new'
    )
 
    date_start = fields.Datetime(
        string='Start Date'
    )
    
    date_end = fields.Datetime(
        string='End Date'
    )
    
    def report_appointment(self):
        report = self.env.ref("dental_care.report_appointment_details")
        return report.report_action(self)