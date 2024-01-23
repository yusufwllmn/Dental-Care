# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DentalPatient(models.Model):
    _name = 'dental.patient'
    _description = 'Dental Patient Records'

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
    
    emergency_number = fields.Char(
        related='name.phone', 
        string='Emergency Number', 
        readonly=True
    )
    
    image = fields.Binary(
        string='Foto',
        attachment=True                      
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
    
    date_of_birth = fields.Date(
        string='Date of Birth'
    )
    
    blood_type = fields.Selection(
        string='Blood Type',
        selection=[
            ('A', 'A'),
            ('B', 'B'),
            ('AB', 'AB'),
            ('O', 'O')
        ]
    )
    
    height = fields.Float(
        string='Height'
    )
    
    weight = fields.Float(
        string='Weight'
    )
    
    is_vaccinated = fields.Boolean(
        string='Is Vaccinated'
    )
    
    vaccine_name = fields.Char(
        string='Vaccine Name'
    )