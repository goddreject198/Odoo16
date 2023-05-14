from odoo import api,fields,models

class Test(models.Model):
    _name = "test.module"
    _description = "Test Module"

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    num = fields.Integer(string='Num')