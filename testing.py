def mark_as_paid(self):
    if not hasattr(self, "current_invoice_id"):
        self.ui.show_message(
            "Please select an invoice first",
            "No Invoice Selected",
            style=1
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Payment",
        "Mark this invoice as PAID?\n(No payment record will be added)"
    )

    if not confirm:
        return

    from services.invoice_service import update_invoice_status

    success = update_invoice_status(self.current_invoice_id, "PAID")

    if success:
        self.ui.show_message("Invoice marked as PAID successfully")
        self.load_invoice_details(self.current_invoice_id)
        self.load_invoices()
    else:
        self.ui.show_message("Failed to update invoice status", style=2)