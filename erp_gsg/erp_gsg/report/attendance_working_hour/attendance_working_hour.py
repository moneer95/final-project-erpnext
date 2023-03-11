# Copyright (c) 2023, monir and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_data(filters):
	attendances = frappe.get_all("Attendance",
								 ["name", "attendance_date", "employee_name", "check_in", "check_out", "department"],
								 filters=filters)

	data = []
	for attendance in attendances:
		check_in = frappe.utils.get_datetime(attendance.check_in)
		check_out = frappe.utils.get_datetime(attendance.check_out)
		working_hours = (check_out - check_in).total_seconds() / 3600 if check_out and check_in else 0
		view_attendance_link = f'<a href="/app/attendance/{attendance.name}" target="_blank">View Attendance</a>'
		row = [attendance.attendance_date, attendance.employee_name, attendance.check_in, attendance.check_out,
			   working_hours, attendance.department, view_attendance_link]
		data.append(row)

	return data

def get_columns():
	return [
		{"fieldname": 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
		{"fieldname": 'employee_name', 'label': 'Employee Name', 'fieldtype': 'Data'},
		{"fieldname": 'check_in', 'label': 'Check IN', 'fieldtype': 'Time'},
		{"fieldname": 'check_out', 'label': 'Check Out', 'fieldtype': 'Time'},
		{"fieldname": 'working_hours', 'label': 'Working Hours', 'fieldtype': 'Float'},
		{"fieldname": 'department', 'label': 'Department', 'fieldtype': 'Link', 'options': 'Department'},
		{"fieldname": 'view_attendance	', 'label': 'View Attendance Form', 'fieldtype': 'Html'},
	]