# Copyright (c) 2023, monir and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ToWhomItConcerns(Document):
	def validate(self):
		# Get the employee ID and company name
		employee_id = self.employee

		# Query the Salary Slip table to get the ID of the most recent salary slip
		salary_slip_id = frappe.db.get_value(
			"Salary Slip",
			filters={
				"employee": employee_id,
				"docstatus": 1  # Only get salary slips with a docstatus of 1 (submitted)
			},
			order_by="creation DESC",  # Get the most recent salary slip based on creation date
			fieldname="name"
		)

		# Use the salary slip ID to get the Salary Slip document
		salary_slip = frappe.get_doc("Salary Slip", salary_slip_id)
		total_salary = 0
		for earning in salary_slip.earnings:
			total_salary += earning.amount

		# assign
		self.salary = total_salary