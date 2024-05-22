# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

import erpnext

from hrms.payroll.doctype.salary_slip.salary_slip import (
	PayrollEntry
)

class CustomPayrollEntry(Document):

	@frappe.whitelist(allow_guest=True)
	def create_pf_details(payroll_entry):
		salary_slips = frappe.get_all("Salary Slip", pluck="name", filters={"payroll_entry": payroll_entry})
		payroll_entry_doc = frappe.get_doc("Payroll Entry", payroll_entry)
		payroll_entry_doc.custom_pf_challan_done = True
		content = ""
		for slp in salary_slips:
			salary_slip_doc = frappe.get_doc('Salary Slip', slp)
			employee = salary_slip_doc.employee
			uan = salary_slip_doc.custom_uan_number
			absent_days = salary_slip_doc.total_working_days - salary_slip_doc.payment_days
			gross = salary_slip_doc.gross_pay
			basic = 15000
			employee_contribution = 0.0
			employer_contribution_1 = 0.0
			employer_contribution_2 = 0.0
			for ddct in salary_slip_doc.earnings:
				if ddct.salary_component == "Basic":
					if ddct.amount < 15000:
						basic = round(ddct.amount)
				if ddct.salary_component == "PF (Employer's Contribution)":
					employer_contribution_1 = round(basic * 0.0833)
					employer_contribution_2 = round(basic * 0.0367)
			for ddct in salary_slip_doc.deductions:
				if ddct.salary_component == "PF (Employee's Contribution)":
					employee_contribution = round(ddct.amount)
			if employee_contribution > 0.0:
				content += """#~#{0}#~#{1}#~#{2}#~#{3}#~#{4}#~#{5}#~#{6}#~#{7}#~#{8}#~#{9}#~#0#~# \n""".format(employee,uan,gross,basic,basic,basic,employee_contribution,employer_contribution_1,employer_contribution_2,absent_days)
		file_doc = frappe.get_doc(
		    {
			"doctype": "File",
			"file_name": ("PF Challan- '%s'" % payroll_entry),
			"attached_to_doctype": 'Payroll Entry',
			"attached_to_name": payroll_entry,
			"content": content,
			"folder": "Home"
		  }
		)
		file_doc.save()