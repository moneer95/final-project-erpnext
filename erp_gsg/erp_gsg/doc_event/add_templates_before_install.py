import frappe

@frappe.whitelist()
def before_install():
    taxes_and_charges_template = {
        "doctype": "Purchase Taxes and Charges Template",
        "taxes": [
            {
                "charge_type": "On Net Total",
                "account_head": "5118 - Expenses Included In Valuation - M",
                "description": "Sales Tax - 16%",
                "rate": 16
            }
        ],
        "company": frappe.defaults.get_global_default("company"),
        "is_default": 1
    }

    sales_taxes_and_charges_template = {
        "doctype": "Sales Taxes and Charges Template",
        "taxes": [
            {
                "charge_type": "On Net Total",
                "account_head": "5207 - Marketing Expenses - M",
                "description": "Sales Tax - 16%",
                "rate": 16
            }
        ],
        "company": frappe.defaults.get_global_default("company"),
        "is_default": 1
    }

    try:
        frappe.get_doc(taxes_and_charges_template).insert()
        frappe.get_doc(sales_taxes_and_charges_template).insert()
    except frappe.DuplicateEntryError:
        frappe.msgprint("DuplicateEntryError!")
