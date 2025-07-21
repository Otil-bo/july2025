odoo.define('pos_credit_limit_alert.credit_limit_alert', function (require) {
    const models = require('point_of_sale.models');
    const rpc = require('web.rpc');
    const OrderSuper = models.Order.prototype;

    models.Order = models.Order.extend({
        initialize: function () {
            OrderSuper.initialize.apply(this, arguments);
            if (this.pos.get_client()) {
                this.check_credit_limit(this.pos.get_client());
            }
        },

        set_client: function (client) {
            this._super(client);
            if (client) {
                this.check_credit_limit(client);
            }
        },

        check_credit_limit: function (client) {
            rpc.query({
                model: 'res.partner',
                method: 'check_credit_limit',
                args: [client.id],
            }).then(function (result) {
                if (result.warning) {
                    alert(result.message);
                }
            });
        }
    });
});