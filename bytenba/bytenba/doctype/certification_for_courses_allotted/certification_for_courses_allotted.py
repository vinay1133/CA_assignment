# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Certificationforcoursesallotted(Document):
	pass


@frappe.whitelist()
def get_professor_names(doctype, txt, searchfield, start, page_len, filters):

		data = frappe.db.get_list('Professors', start=start, page_length= page_len, fields=["name" , "full_name","department"], as_list=True)
		
		return data

