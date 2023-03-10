import frappe

@frappe.whitelist()
def reset_excuse_hours_balance():
    employees = frappe.get_all('Employee', filters={'status': 'Active'})
    for employee in employees:
        employee_doc = frappe.get_doc('Employee', employee.name)
        department = employee_doc.department
        department_doc = frappe.get_doc('Department', department)
        default_excuse_hours = department_doc.excuse_hours_allowed
        employee_doc.excuse_hours_balance = default_excuse_hours
        employee_doc.save()
