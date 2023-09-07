import frappe

@frappe.whitelist()
def get_professor_names(doctype, txt, searchfield, start, page_len, filters):

		data = frappe.db.get_list('Professors', start=start, page_length= page_len, fields=["name" , "full_name","department"], as_list=True)
		
		return data