from odoo import models, fields, Command, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    product_custom_template_attribute_value_ids = fields.Many2many(
        string='Custom Attribute Values',
        comodel_name='product.template.attribute.value',
        relation='purchase_order_line_custom_ptav_rel',
        column1='order_line_id',
        column2='ptav_id',
        compute="_compute_variant_tags",
        store=True,
    )
    test_test2 = fields.Boolean("Test2")

    @api.depends(
        'product_id',
        'product_template_attribute_value_ids',
        'product_template_attribute_value_ids.attribute_line_id.is_show_attribute',
        'product_no_variant_attribute_value_ids',
        'product_no_variant_attribute_value_ids.attribute_line_id.is_show_attribute',
    )
    def _compute_variant_tags(self):
        for rec in self:
            res_ids = set()
            product_template_ids = rec.product_template_attribute_value_ids.filtered(lambda x: x.attribute_line_id.is_show_attribute)
            if product_template_ids:
                res_ids |= set(product_template_ids.ids)
            product_no_variant_ids = rec.product_no_variant_attribute_value_ids.filtered(lambda x: x.attribute_line_id.is_show_attribute)
            if product_no_variant_ids:
                res_ids |= set(product_no_variant_ids.ids)
            rec.product_custom_template_attribute_value_ids = [Command.set(list(res_ids))]