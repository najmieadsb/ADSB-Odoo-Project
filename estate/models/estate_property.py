from odoo import fields,models
from dateutil.relativedelta import relativedelta
from datetime import date

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Test Model"

    name = fields.Char(required = False)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self:date.today() + relativedelta(months = 3))
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly=True, copy=False )
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
   # FIXED: Selection field with proper 2-element tuples
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    active = fields.Boolean(default = True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')
    ], 
    required=True , copy= False, default= 'new'
    )
