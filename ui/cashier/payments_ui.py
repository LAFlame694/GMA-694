def record_payment(self):
    if not hasattr(self, "current_invoice_id") or not self.current_invoice_id:
        self.ui.show_message(
            "Please select an invoice first",
            "No Invoice Selected",
            style=1
        )
        return

    amount_text = self.payment_entry.get().strip()

    if not amount_text:
        self.ui.show_message(
            "Please enter payment amount",
            "Missing Amount",
            style=1
        )
        return

    try:
        amount = float(amount_text)
        if amount <= 0:
            raise ValueError
    except ValueError:
        self.ui.show_message(
            "Enter a valid positive number",
            "Invalid Amount",
            style=2
        )
        return

    # ✅ use existing service
    from services.payment_service import add_payment

    try:
        paid_total, balance, status = add_payment(
            self.current_invoice_id,
            amount
        )
    except Exception as e:
        self.ui.show_message(
            "Failed to record payment",
            "Error",
            style=2
        )
        return

    # success
    self.ui.show_message(
        f"Payment recorded successfully\n"
        f"Status: {status}\n"
        f"Balance: KES {balance:.2f}"
    )

    self.payment_entry.delete(0, tk.END)

    # 🔄 refresh UI
    self.load_invoice_details(self.current_invoice_id)
    self.load_invoices()