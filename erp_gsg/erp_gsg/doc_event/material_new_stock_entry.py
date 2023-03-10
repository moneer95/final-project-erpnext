import frappe

@frappe.whitelist()
def make_stock_entry_after_material_request(doc, method):
    frappe.throw("djbd")
    if doc.material_request_type == "Material Issue":
        # create a new Sales Order with one item row
        stock_entry = frappe.new_doc("Stock Entry")
        stock_entry.stock_entry_type = "Material Issue"
        stock_entry.to_warehouse = doc.set_warehouse
        stock_entry.material_request = doc.name

        items_in_material_erquest = []

        for item in doc.items:
            items_in_material_erquest.append(
                {
                    "item_code": item.item_code,
                    "qty": item.qty,
                    "s_warehouse": item.from_warehouse
                }
            )

        stock_entry.items = items_in_material_erquest

        # save the Stock Entry
        stock_entry.insert()
        stock_entry.save()

