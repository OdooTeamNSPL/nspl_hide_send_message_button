/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Chatter } from "@mail/core/web/chatter";
import { useService } from "@web/core/utils/hooks";

patch(Chatter.prototype, {
    setup() {
        super.setup();
        this.user = useService("user");
        this._hideSendMessage = false;
        this.checkGroup();
    },

    async checkGroup() {
        const hasGroup = await this.user.hasGroup("nspl_hide_send_message_button.group_hide_send_message");
        this._hideSendMessage = hasGroup;
        this.render(); // re-render once group check is done
    },

    get hideSendMessage() {
        return this._hideSendMessage;
    },
});
