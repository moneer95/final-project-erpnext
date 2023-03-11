import frappe
from erpnext.stock.doctype.stock_entry.stock_entry_utils import make_stock_entry


@frappe.whitelist()
def make_stock_entry_after_material_request(doc, method):
    if doc.material_request_type == "Material Issue":
        for item in doc.items:
            stock_entry = make_stock_entry(
                item_code=item.item_code,
                target=item.warehouse,
                qty=item.qty,
                rate=item.rate,
            )
            frappe.msgprint(f'{stock_entry} created')

