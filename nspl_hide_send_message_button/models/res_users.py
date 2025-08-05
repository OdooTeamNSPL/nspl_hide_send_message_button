from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = "res.users"

    hide_send_message = fields.Boolean("Hide Send Message Button")

    @api.model
    def _get_user_context(self):
        res = super()._get_user_context()
        res['hide_send_message'] = self.hide_send_message
        return res
