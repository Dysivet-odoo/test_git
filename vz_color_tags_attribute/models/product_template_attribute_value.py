from odoo import fields, models


class ProductTemplateAttributeValue(models.Model):
    _inherit = "product.template.attribute.value"

    color_hex = fields.Char(related="product_attribute_value_id.color_hex", string="Color Hex")
