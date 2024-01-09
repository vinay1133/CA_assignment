import frappe
import re

def standard_validation(self):

  #check for existing record
	existing_record = frappe.db.exists(self.doctype, {'name': self.name})
	if existing_record and existing_record != self.name:
		frappe.throw('There already exists such a record in the database')
	
  #check academic year pattern
	pattern_for_ay = r'^20(2[4-9]|[3-9][0-9])$'
	if not re.match(pattern_for_ay, self.academic_year):
			frappe.throw("Academic year must be of the form like 2024")
	
  #get faculty information
	info = frappe.db.get_list('Professors', fields = ["select_reviewer", "full_name", "department", "faculty_designation"], filters={'name': ['=', self.owner]}, as_list=True, ignore_permissions = True)
	#validate Faculty information provided
	if not self.reviewer == info[0][0]:
		frappe.throw('Error at reviewer')
	if not self.professor == info[0][1]:
		frappe.throw('Error at full name')
	if not self.department == info[0][2]:
		frappe.throw('Error at department')
	if not self.designation == info[0][3]:
		frappe.throw('Error at faculty designation')		
  
  #prohibit form alteration post approval by user
	roles = frappe.get_roles(frappe.session.user)
	is_reviewer = True if 'reviewer' in roles else False
	is_admin = True if 'Administrator' in roles else False
	if self.approved == 1 and not is_reviewer and not is_admin:
		frappe.throw("Cannot modify document post approval")
		

def validate_delete(doc,method):

	roles = frappe.get_roles(frappe.session.user)
	is_admin = True if 'Administrator' in roles else False
	if doc.approved == 1 and not is_admin:
		frappe.throw('Cannot delete document post approval')
