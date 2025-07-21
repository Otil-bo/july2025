odoo.define('pos_credit_limit_alert.pos_credit_limit', function (require) {
    "use strict";

    const PosModel = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');

    const PosCreditLimit = (PosModel) => class extends PosModel {
        async _flush_orders() {
            const partner = this.get_client();

            if (partner) {
                const res = await this.rpc({
                    model: 'res.partner',
                    method: 'check_partner_credit',
                    args: [partner.id],
                });

                if (!res.allowed) {
                    await Gui.showPopup('ErrorPopup', {
                        title: 'Límite de Crédito Excedido',
                        body: res.message,
                    });
                    return false;
                }
            }

            return super._flush_orders();
        }
    };

    Registries.Model.extend(PosModel, PosCreditLimit);

    return PosModel;
});
