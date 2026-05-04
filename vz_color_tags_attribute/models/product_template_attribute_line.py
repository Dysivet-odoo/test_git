from odoo import fields, models


class ProductTemplateAttributeLine(models.Model):
    _inherit = "product.template.attribute.line"

    is_show_attribute = fields.Boolean('Show Attribute', default=False)
    test_test= fields.Boolean("Test")
    test_test2 = fields.Boolean("Test2")