/** @odoo-module **/
import { PaymentScreen } from "@point_of_sale/app/screens/payment/payment_screen";
import Registries from "@point_of_sale/core/registries";

const PosPaymentScreenCreditAlert = (PaymentScreen) =>
    class extends PaymentScreen {
        async validateOrder(isForceValidate) {
            const partner = this.currentOrder.get_partner();
            if (partner && partner.overdue_credit > 0 && !isForceValidate) {
                const { confirmed } = await this.popup.add(
                    'confirm',
                    {
                        title: this.env._t('Cliente con crédito vencido'),
                        body: this.env._t(
                            'El cliente tiene un crédito vencido de '
                        ) + this.env.services.formatCurrency(partner.overdue_credit) + 
                        this.env._t('. ¿Deseas continuar de todas formas?'),
                    }
                );
                if (!confirmed) {
                    return false;
                }
            }
            return super.validateOrder(...arguments);
        }
    };

Registries.Component.extend(PaymentScreen, PosPaymentScreenCreditAlert);