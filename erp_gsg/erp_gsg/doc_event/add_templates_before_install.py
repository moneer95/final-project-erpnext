import frappe

@frappe.whitelist()
def before_install():
    # task 3
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




    # task 9
    salary_component = frappe.new_doc("Salary Component")
    salary_component.salary_component = "Housing Allowance GSG"
    salary_component.salary_component_abbr = "HGSG"
    salary_component.type = "Earning"
    salary_component.is_flexible_benefit = 0
    salary_component.is_deduction = 0
    salary_component.is_tax_applicable = 1
    salary_component.is_income_tax_applicable = 1
    salary_component.is_statutory = 0
    salary_component.is_payroll_entry = 1
    salary_component.is_basic = 0
    salary_component.dependent_on_salary_slab = 0
    salary_component.include_in_net_pay = 1
    salary_component.rounding_adjustment = "Round Down"
    salary_component.rounding_precision = 2
    salary_component.insert(ignore_permissions=True)
    salary_component.save()
