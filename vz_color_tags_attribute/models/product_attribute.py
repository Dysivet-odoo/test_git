from odoo import fields, models


class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    is_show_attribute = fields.Boolean('Show Attribute for all products', default=False)

    def write(self, vals):
        res = super().write(vals)
        if 'is_show_attribute' in vals:
            for rec in self:
                rec.attribute_line_ids.write({'is_show_attribute': rec.is_show_attribute})
        return res  
    
    def create(self, vals):
        res = super().create(vals)
        if 'is_show_attribute' in vals:
            res.attribute_line_ids.write({'is_show_attribute': res.is_show_attribute})
        return res