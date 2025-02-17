from odoo import api, models, fields

class Hospitalpatients(models.Model):
    _name = "hospital.patient"
    _description = "hospital.type"

    name = fields.Char(string="Patient Name")
    age =fields.Integer(string="Patient Age")
    gender = fields.Selection([('male', 'male'), ('female', 'female')], string="Gender")
    phone = fields.Char(string="Phone Number")
    mobile = fields.Char(string="Mobile Number")
