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
    
    date_start = fields.Datetime(
        string='Start Date'
    )
    
    date_end = fields.Datetime(
        string='End Date'
    )