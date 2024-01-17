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
    
    


    
