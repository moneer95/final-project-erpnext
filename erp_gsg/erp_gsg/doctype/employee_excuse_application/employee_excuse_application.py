# Copyright (c) 2023, monir and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
from frappe.utils import time_diff



class EmployeeExcuseApplication(Document):
	def validate(self):
		current_month = datetime.datetime.now().month
		excuse_month = datetime.datetime.strptime(self.excuse_date, '%Y-%m-%d').month

		excuse_hours = time_diff(self.to_time, self.from_time)
		excuse_balance = frappe.get_doc("Employee", self.employee).excuse_hours_balance

		diff_from_to = time_diff(self.to_time, self.from_time)


		if current_month == excuse_month:
			if diff_from_to > datetime.timedelta(0):
				if datetime.timedelta(excuse_balance) >= excuse_hours:
					# change the excuse_balance reference to time delta object
					excuse_balance_timedelta = datetime.timedelta(hours=excuse_balance)
					# subtract the balance
					excuse_balance = excuse_balance_timedelta - excuse_hours
					# convert to hours
					excuse_balance = excuse_balance.total_seconds()/3600
					# assign value
					#frappe.get_doc("Employee", self.employee).excuse_hours_balance = float(excuse_balance)
					employee = frappe.get_doc("Employee", self.employee)
					employee.set("excuse_hours_balance", float(excuse_balance))
					employee.save(ignore_permissions=True)
					frappe.db.commit()
					# reload the Employee document to make sure changes are visible
					employee.reload()

					# check if the field has been updated
					frappe.msgprint(f'excuse_hours_balance: {employee.excuse_hours_balance}')

				else:
					frappe.throw(f'your excuse balance is {excuse_balance} you exceeded it!')
			else:
				frappe.throw("to date must be bigger that from date")
		else:
			frappe.throw("you must excuse in current month")