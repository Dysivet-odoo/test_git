from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            order.order_line.write({'product_custom_template_attribute_value_ids': [(6, 0, order.order_line.product_id.attribute_line_ids.mapped('custom_value_id').ids)]})
        return res
    
    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        for line in self.order_line:
            line.product_custom_template_attribute_value_ids.write({'test_test2': True})
        return res
    
    def _prepare_delivery_move_data(self):
        res = super()._prepare_delivery_move_data()
        for line in self.order_line:
            line.product_custom_template_attribute_value_ids.write({'test_test2': True})
        return res
