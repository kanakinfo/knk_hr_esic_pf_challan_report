// Copyright (c) 2024, Kanak InfoSystems LLP and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["ESIC Report"] = {
	"filters": [
		{
			fieldname: "payroll_entry",
			label: __("Payroll Entry"),
			fieldtype: "Link",
			options: 'Payroll Entry',
		},
	],
};
