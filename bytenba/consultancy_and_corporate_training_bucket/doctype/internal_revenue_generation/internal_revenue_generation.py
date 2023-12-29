import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re
import math as m

Doctype = 'Internal revenue generation'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Internalrevenuegeneration(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'CB1_{self.CurrOwner}_{self.academic_year}_{self.semester}'
		# self.name = f'CB1_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')

		#validation post approval
		roles = frappe.get_roles()
		current_user_is_reviewer = True if 'reviewer' in roles else False
		current_user_is_admin = True if 'Administrator' in roles else False
		#if user is not admin or not a reviewer then he cannot change the form post form approval
		if not current_user_is_admin and not current_user_is_reviewer and self.approved == 1:
			frappe.throw("""Modifcation of document is not permitted since document has been approved""")
	

def compute_marks(self):

	match = re.search(pattern_for_wtg, self.col1)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	match = re.search(pattern_for_wtg, self.col2)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')			

	marks_obtained = m.floor(val1*val2*375)
	
	return marks_obtained