# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DentalService(models.Model):
    _name = 'dental.service'
    _description = 'Dental Service Records'
    
    name = fields.Char(
        "Name", 
        required=True 
    )
    
    floor = fields.Integer(
        "Floor"
    )
    
    room = fields.Char(
        "Room"
    )
    
    doctor_count = fields.Integer(
        "Doctor Count",
        compute='_compute_doctor_count'
    )
    
    doctor_ids = fields.One2many(
        'dental.doctor',
        'service_id',
        string = 'Doctors'
    )
    
    @api.depends('doctor_ids')
    def _compute_doctor_count(self):
        doctor_group = self.env['dental.doctor'].read_group(domain=[], fields=['service_id'], groupby=['service_id'])
        
        for doctor in doctor_group:
            service_id = doctor.get('service_id')[0]
            service_rec = self.browse(service_id)
            service_rec.doctor_count = doctor['service_id_count']
            self -= service_rec
        self.doctor_count = 0
            
    def action_view_service(self):
        return {
            'name': ('Doctors'),
            'res_model': 'dental.doctor',
            'view_mode': 'list,form',
            'context': {'default_service_id' : self.id},
            'domain': [('service_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }