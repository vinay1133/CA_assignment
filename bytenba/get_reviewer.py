import frappe

@frappe.whitelist()
def get_reviewer(session_user):
		user_dept = frappe.db.get_value("User", session_user, "department")
		reviewer = frappe.db.get_value("Department", user_dept, "hod")
		return reviewer
		