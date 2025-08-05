/** @odoo-module **/

import { Chatter } from "@mail/chatter/web_portal/chatter";
import { patch } from "@web/core/utils/patch";
import { user } from "@web/core/user";
import { onWillStart } from "@odoo/owl";

patch(Chatter.prototype, {
    setup() {
        super.setup();
        this._hideSendMessage = false;

        onWillStart(async () => {
            this._hideSendMessage = await user.hasGroup(
                "nspl_hide_send_message_button.group_hide_send_message"
            );
        });
    },

    get hideSendMessage() {
        return this._hideSendMessage;
    },
});
