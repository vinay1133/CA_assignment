import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf

Doctype = 'Topper Marks'

class TopperMarks(Document):
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'SD3_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = computemarks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')

def computemarks(self):
	all_courses = []
	count = 0

	for course in self.topper_marks_table:
		count += 1
		temp_marks = 0
		
		if course.bucket_100 >= 0:
			temp_marks += 20*course.bucket_100
		else:
			frappe.throw(f"Data in row {count} entered incorrectly")

		if course.bucket_90 >= 0:
			temp_marks += 15*course.bucket_90
		else:
			frappe.throw(f"Data in row {count} entered incorrectly")
		
		if course.bucket_80 >= 0:
			temp_marks += 10*course.bucket_80
		else:
			frappe.throw(f"Data in row {count} entered incorrectly")		

		if course.bucket_70 >= 0:
			temp_marks += 7*course.bucket_70
		else:
			frappe.throw(f"Data in row {count} entered incorrectly")			

		if course.bucket_60 >= 0:
			temp_marks += 5*course.bucket_60
		else:
			frappe.throw(f"Data in row {count} entered incorrectly")

		if course.bucket_60_below>= 0:
			temp_marks += 0*course.bucket_60_below
		else:
			frappe.throw(f"Data in row {count} entered incorrectly")

		course.marks_obtained = temp_marks
		all_courses.append(temp_marks)

	sum = 0
	for i in all_courses:
		sum += i
	
	sap = sum // count
	if sap > 500:
		sap = 500
	
	return sap