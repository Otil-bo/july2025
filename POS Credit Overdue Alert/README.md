# POS Credit Overdue Alert

This module adds an alert in the Point of Sale (POS) when the selected customer has **overdue receivables** that exceed zero. The popup shows the total overdue amount and asks the cashier to confirm before completing the sale.

## Installation

1. Copy the folder `pos_credit_overdue_alert` into your Odoo `addons` directory.
2. Update apps list and install **POS Credit Overdue Alert**.
3. Ensure your user has access to customer credit information.

## Usage

- In the POS, select a customer with unpaid, overdue invoices.
- When you press **Payment**, a confirmation dialog appears indicating the overdue amount.
- The cashier can decide to proceed (`Continuar`) or cancel the order.

## Technical Notes

- The overdue amount is computed from unpaid receivable lines whose maturity date is **before today**.
- The value is stored on the partner in the `overdue_credit` computed field.
- The POS frontend receives `overdue_credit` via the default partner model export.

Tested on Odoo **16.0 Community**.