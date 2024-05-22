from . import __version__ as app_version

app_name = "knk_hr_esic_pf_challan_report"
app_title = "ESIC and PF Challan Report HR"
app_publisher = "Kanak Infosystems LLP."
app_description = "A frappe custom addon to add option to generate ESIC report and PF Challan Report from ErpNext based on India Compliances."
app_email = "sales@kanakinfosystems.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/knk_hr_esic_pf_challan_report/css/knk_hr_esic_pf_challan_report.css"
# app_include_js = "/assets/knk_hr_esic_pf_challan_report/js/knk_hr_esic_pf_challan_report.js"

# include js, css files in header of web template
# web_include_css = "/assets/knk_hr_esic_pf_challan_report/css/knk_hr_esic_pf_challan_report.css"
# web_include_js = "/assets/knk_hr_esic_pf_challan_report/js/knk_hr_esic_pf_challan_report.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "knk_hr_esic_pf_challan_report/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Payroll Entry" : "public/js/payroll_entry.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "knk_hr_esic_pf_challan_report.utils.jinja_methods",
#	"filters": "knk_hr_esic_pf_challan_report.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "knk_hr_esic_pf_challan_report.install.before_install"
# after_install = "knk_hr_esic_pf_challan_report.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "knk_hr_esic_pf_challan_report.uninstall.before_uninstall"
# after_uninstall = "knk_hr_esic_pf_challan_report.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "knk_hr_esic_pf_challan_report.utils.before_app_install"
# after_app_install = "knk_hr_esic_pf_challan_report.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "knk_hr_esic_pf_challan_report.utils.before_app_uninstall"
# after_app_uninstall = "knk_hr_esic_pf_challan_report.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "knk_hr_esic_pf_challan_report.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"Payroll Entry": "knk_hr_esic_pf_challan_report.overrides.custom_payroll_entry"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"knk_hr_esic_pf_challan_report.tasks.all"
#	],
#	"daily": [
#		"knk_hr_esic_pf_challan_report.tasks.daily"
#	],
#	"hourly": [
#		"knk_hr_esic_pf_challan_report.tasks.hourly"
#	],
#	"weekly": [
#		"knk_hr_esic_pf_challan_report.tasks.weekly"
#	],
#	"monthly": [
#		"knk_hr_esic_pf_challan_report.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "knk_hr_esic_pf_challan_report.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "knk_hr_esic_pf_challan_report.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "knk_hr_esic_pf_challan_report.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["knk_hr_esic_pf_challan_report.utils.before_request"]
# after_request = ["knk_hr_esic_pf_challan_report.utils.after_request"]

# Job Events
# ----------
# before_job = ["knk_hr_esic_pf_challan_report.utils.before_job"]
# after_job = ["knk_hr_esic_pf_challan_report.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"knk_hr_esic_pf_challan_report.auth.validate"
# ]
