from odoo import fields, models


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    color_hex = fields.Char('Color Hex', default='#fcc603')
