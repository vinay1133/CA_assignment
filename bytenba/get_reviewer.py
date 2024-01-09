import frappe

@frappe.whitelist()
def get_reviewer(session_user):
		# user_dept = frappe.db.get_value("Professors", session_user, "department")
		# reviewer = frappe.db.get_value('Professors', {"is_hod":1,"department": user_dept}, 'full_name')
		# return reviewer
		
		# user_dept = frappe.db.get_value("Professors", session_user, "department")
		# reviewer = frappe.db.get_value('Professors', {"is_hod":1,"department": user_dept}, 'full_name')
		# professor_full_name = frappe.db.get_value('Professors', session_user, 'full_name')
		# return [reviewer, professor_full_name]
		data = frappe.db.get_list('Professors', fields = ["select_reviewer", "full_name"], filters={'name': ['=', session_user]}, as_list=True, ignore_permissions = True)

		return data[0]


@frappe.whitelist()
def get_reviewer_names(doctype, txt, searchfield, start, page_len, filters):
		data = frappe.db.get_list('Has Role', start=start, page_length= page_len, fields=["parent"], filters = {'role': ['=', 'reviewer']}, as_list=True)
		return data