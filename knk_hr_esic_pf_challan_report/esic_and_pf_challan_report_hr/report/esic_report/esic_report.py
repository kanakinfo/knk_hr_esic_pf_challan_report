# Copyright (c) 2024, Kanak InfoSystems LLP and contributors
# For license information, please see license.txt

import frappe
import json
from frappe import _

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data


def get_columns(filters):
	columns = [
		{
			"fieldname": "ip_number",
			"label": "IP Number",
			"fieldtype": "Data",
			"width": 240,
		},
		{
			"fieldname": "employee",
			"label": "Employee Name",
			"fieldtype": "Link",
			"options": "Employee",
			"width": 300,
		},
		{
			"fieldname": "payment_days",
			"label": "No of Days for which wages paid/payable during the month",
			"fieldtype": "Float",
			"width": 100,
		},
		{
			"fieldname": "total_monthly_wages",
			"fieldtype": "Float",
			"label": "Total Monthly Wages",
			"width": 200,
		},
	]
	return columns

def get_data(filters):
	if not (filters.payroll_entry):
		frappe.throw(_("Please select a Payroll Entry."))
	data = []
	payroll_entry = filters.payroll_entry
	salary_slips = frappe.get_all("Salary Slip", pluck="name", filters={"payroll_entry": payroll_entry})
	for slp in salary_slips:
		salary_slip_doc = frappe.get_doc('Salary Slip', slp)
		employee = salary_slip_doc.employee
		esic = salary_slip_doc.custom_ipn_number
		payment_days = salary_slip_doc.payment_days
		basic_hra = 0.0
		for ddct in salary_slip_doc.earnings:
			if ddct.salary_component == "Basic":
				basic_hra += round(ddct.amount)
			if ddct.salary_component == "House Rent Allowance":
				basic_hra += round(ddct.amount)
		if esic != None:
			data.append([esic, employee, payment_days, basic_hra])
	data = tuple(tuple(x) for x in list(data))
	return data