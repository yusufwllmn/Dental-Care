# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DentalDoctor(models.Model):
    _name = 'dental.doctor'
    _description = 'Dental Doctors Record'

    name = fields.Many2one(
        'res.partner', 
        string='Doctor', 
        required=True
    )
    
    service_id = fields.Many2one(
        'dental.service', 
        string='Service'
    )

    image = fields.Image(
        string='Foto',
        attachment=True                      
    )
    
    is_leave = fields.Boolean(
        string="Paid Leave",
        default=False
    )
    
    def toggle_is_leave(self):
        for doctor in self:
            doctor.is_leave = not doctor.is_leave
