# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DentalDoctor(models.Model):
    _name = 'dental.doctor'
    _description = 'Dental Doctors Record'

    name = fields.Char(
        related='doctor_id.name',
        string='Doctor', 
        required=True,
        readonly=False
    )
    
    doctor_id = fields.Many2one(
        'res.partner', 
        string='Doctor', 
        required=True
    )
    
    service_id = fields.Many2one(
        'dental.service', 
        string='Service'
    )
    
    image = fields.Binary(
        string='Foto',
        attachment=True                      
    )
    
    active = fields.Boolean(
        string="Active",
        default=True
    )
    
    def toggle_active(self):
        for doctor in self:
            doctor.active = not doctor.active