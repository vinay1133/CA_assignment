# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import get_all


class Professors(Document):
	
	def before_save(self):
		full_name = self.first_name
		if self.middle_name:
			full_name = full_name + " " + self.middle_name
		if self.last_name:
			full_name = full_name + " " + self.last_name
		
		self.full_name = full_name
	
	def validate(self):
		#check for existing HODs if form is marked with is_hod
		if self.is_hod:
			Doctype = "Professors"
			filters = {
					"is_hod": 1,
					"department": self.department
			}
			if get_all(Doctype, filters=filters):
				frappe.throw('Cannot have more than one HOD')