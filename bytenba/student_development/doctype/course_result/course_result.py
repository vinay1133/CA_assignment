import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
# import re

Doctype = 'Course Result'
# pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class CourseResult(Document):
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'SD2_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = computemarks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')

def computemarks(self):
		sum = 0
		count = 0
		for item in self.course_result_table:
			if item.course_result < 0 or item.course_result > 100:
				frappe.throw('Course Result percentage entered incorrectly')
			else:
				count +=1
				if item.course_result > 80:
					temp_marks = 700
				elif 70 < item.course_result <= 80:
					temp_marks = 590
				elif 60 < item.course_result <= 70:
					temp_marks = 470
				elif 50 < item.course_result <= 60:
					temp_marks = 350
				elif 40 < item.course_result <= 50:
					temp_marks = 240
				elif item.course_result < 40:
					temp_marks = 0
				else:
					frappe.throw('Something went wrong')
				sum+= temp_marks
				item.marks_obtained = temp_marks
		
				return sum // count
			