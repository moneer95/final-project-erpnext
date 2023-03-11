// Copyright (c) 2023, monir and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hour"] = {
	"filters": [
		{"fieldname": 'department', 'label': 'Department', 'fieldtype': 'Link', 'options': 'Department'},
		{"fieldname": 'employee_name', 'label': 'Employee Name', 'fieldtype': 'Data'},
		{"fieldname": 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
	]
};
