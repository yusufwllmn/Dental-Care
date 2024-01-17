# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DentalDoctor(models.Model):
    _name = 'dental.doctor'
    _description = 'Dental Doctors Record'

    doctor = fields.Many2one(
        'res.partner', 
        string='Doctor', 
        required=True
    )
    
    service_id = fields.Many2one(
        'dental.service', 
        string='Service'
    )