app_name = "csis"
app_title = "Customer Solution Integrated System"
app_publisher = "RND Solusi Pratama - Lead by Robi Tejo Surasko"
app_description = "Apps for direct communication with customer trough multimedia like call and messaging"
app_email = "admin@rndsolusi.co.id"
app_license = "unlicense"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
 add_to_apps_screen = [
 	{
 		"name": "csis",
 		"logo": "/assets/csis/logo.png",
 		"title": "Customer Solution Integrated System",
 		"route": "/csis",
 		"has_permission": "csis.api.permission.has_app_permission"
 	}
 ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/csis/css/csis.css"
# app_include_js = "/assets/csis/js/csis.js"

# include js, css files in header of web template
# web_include_css = "/assets/csis/css/csis.css"
# web_include_js = "/assets/csis/js/csis.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "csis/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "csis/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

website_route_rules = [
	{"from_route": "/csis/<path:app_path>", "to_route": "crm"},
]


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "csis.utils.jinja_methods",
# 	"filters": "csis.utils.jinja_filters"
# }

# Installation
# ------------

 before_install = "csis.install.before_install"
 after_install = "csis.install.after_install"

# Uninstallation
# ------------

 before_uninstall = "csis.uninstall.before_uninstall"
# after_uninstall = "csis.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "csis.utils.before_app_install"
# after_app_install = "csis.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "csis.utils.before_app_uninstall"
# after_app_uninstall = "csis.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "csis.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

override_doctype_class = {
	"Contact": "crm.overrides.contact.CustomContact",
	"Email Template": "crm.overrides.email_template.CustomEmailTemplate",
}


# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
	"Contact": {
		"validate": ["crm.api.contact.validate"],
	},
	"ToDo": {
		"after_insert": ["crm.api.todo.after_insert"],
		"on_update": ["crm.api.todo.on_update"],
	},
	"Comment": {
		"on_update": ["crm.api.comment.on_update"],
	},
	"WhatsApp Message": {
		"validate": ["crm.api.whatsapp.validate"],
		"on_update": ["crm.api.whatsapp.on_update"],
	},
	"CRM Deal": {
		"on_update": [
			"crm.fcrm.doctype.erpnext_crm_settings.erpnext_crm_settings.create_customer_in_erpnext"
		],
	},
	"User": {
		"before_validate": ["crm.api.demo.validate_user"],
		"validate_reset_password": ["crm.api.demo.validate_reset_password"],
	},
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"csis.tasks.all"
# 	],
# 	"daily": [
# 		"csis.tasks.daily"
# 	],
# 	"hourly": [
# 		"csis.tasks.hourly"
# 	],
# 	"weekly": [
# 		"csis.tasks.weekly"
# 	],
# 	"monthly": [
# 		"csis.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "csis.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "csis.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "csis.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["csis.utils.before_request"]
# after_request = ["csis.utils.after_request"]

# Job Events
# ----------
# before_job = ["csis.utils.before_job"]
# after_job = ["csis.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"csis.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

after_migrate = ["crm.fcrm.doctype.fcrm_settings.fcrm_settings.after_migrate"]

standard_dropdown_items = [
	{
		"name1": "app_selector",
		"label": "Apps",
		"type": "Route",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "toggle_theme",
		"label": "Toggle theme",
		"type": "Route",
		"icon": "moon",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "settings",
		"label": "Settings",
		"type": "Route",
		"icon": "settings",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "logout",
		"label": "Log out",
		"type": "Route",
		"icon": "log-out",
		"route": "#",
		"is_standard": 1,
	},
]
