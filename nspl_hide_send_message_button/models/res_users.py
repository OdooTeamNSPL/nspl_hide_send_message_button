from odoo import models, fields , api


class ResUsers(models.Model):
    _inherit = "res.users"

    hide_send_message_button = fields.Boolean("Hide Send Message Button")

    # def get_user_context(self):
    #     res = super().get_user_context()
    #     res['hide_send_message_button'] = self.hide_send_message_button
    #     return res
    #
    # @api.model
    # def load_views(self, *args, **kwargs):
    #     res = super().load_views(*args, **kwargs)
    #     self.env.user._context = dict(self.env.user._context)
    #     self.env.user._context['hide_send_message_button'] = self.env.user.hide_send_message_button
    #     return res
    # models/res_users.py

    def get_user_context(self):
        ctx = super().get_user_context()
        ctx['has_hide_group'] = self.has_group('nspl_hide_send_message_button.group_hide_send_message')
        return ctx
