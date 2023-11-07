import frappe

@frappe.whitelist()
def get_reviewer(session_user):
		user_dept = frappe.db.get_value("Professors", session_user, "department")
		reviewer = frappe.db.get_value('Professors', {"is_hod":1,"department": user_dept}, 'full_name')
		return reviewer
		