from odoo import models, fields, Command, api


class StockMove(models.Model):
    _inherit = 'stock.move'
    

    product_custom_template_attribute_value_ids = fields.Many2many(
        string='Custom Attribute Values',
        comodel_name='product.template.attribute.value',
        relation='stock_move_custom_ptav_rel',
        column1='move_id',
        column2='ptav_id',
        compute="_compute_variant_tags",
        store=True,
    )
    test = fields.Char(string='Test', compute="_compute_test", store=True)
    test2 = fields.Char(string='Test2')
    test3 = fields.Char(string='Test3')

    @api.depends(
        'product_id',
        'product_id.product_template_attribute_value_ids',
        'product_id.product_tmpl_id.attribute_line_ids.is_show_attribute',
        'product_id.product_tmpl_id.attribute_line_ids.value_ids',
        'product_id.product_tmpl_id.attribute_line_ids.product_template_value_ids',
    )
    def _compute_variant_tags(self):
        for rec in self:
            # all_template_line_attributes_ids = rec.product_id.product_tmpl_id.valid_product_template_attribute_line_ids

            res_ids = set()
            # one_value_line_attribute_ids = all_template_line_attributes_ids.filtered(lambda x: x.is_show_attribute and len(x.value_ids) == 1)
            # if one_value_line_attribute_ids:
            #     res_ids.update(one_value_line_attribute_ids.mapped('product_template_value_ids').ids)
            
            res_ids.update(rec.product_id.product_template_attribute_value_ids.filtered(lambda x: x.attribute_line_id.is_show_attribute).ids)
            rec.product_custom_template_attribute_value_ids = [Command.set(list(res_ids))]