# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'BSA-Co-curricular'
pattern = re.compile(r'^\d{4}-\d{4}$')

class BSACocurricular(Document):
	def autoname(self):
		self.name = f'AI3c_{self.professor}_{self.academic_year}_{self.semester}'

	def before_save(self):
		marks_dict = compute_marks(self)
		self.quality_relevance = marks_dict['quality_relevance']
		self.obtained_marks = marks_dict['total_marks']

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')

		feedback = self.feedback_received
		attendees = self.no_of_attendees
		students = self.total_no_of_students_on_roll
		if feedback > attendees:
			frappe.throw('Number of feedbacks must be less then number of attendees.')
		if attendees > students:
			frappe.throw('Number of attendees must be less than number of students')



def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list(Doctype, filters= filters, pluck = field)
	if len(similar_docs) == 0:
		dict['name_value'] = base_name + '_0'
		return dict
	if len(similar_docs) == 1:
		form_num = int(similar_docs[0][-1])
		new_num = form_num + 1
		dict['name_value'] = f"{base_name}_{new_num}"
	elif len(similar_docs) == 2:
			frappe.throw(f'Maximum limit of 2 for AI3c forms for the academic year {academic_year} has been reached, kindly delete existing forms to create more')
	else:
			frappe.throw(f'Something went wrong')
	return dict

def compute_marks(self):
		marksDict = {'quality_relevance': None,'total_marks': None}

	    #feedback
		feedback = self.feedback_received
		attendees = self.no_of_attendees
		students = self.total_no_of_students_on_roll
		if(feedback >= 2.5) :
			wtg1 = attendees/students
			marksDict['quality_relevance'] = wtg1
		else:
			marksDict['quality_relevance'] = 0

		#events
		international = self.international * 1.5 
		national = self.national * 1.3
		statelevel =self.state_level * 1.2
		interclg = self.intercollegiate_city_level * 1.1
		interdep = self.inter_departmental * 1
		withinclass = self.within_class * 0.5
		mark1 = international*national*statelevel*interclg*interdep*withinclass
		

		#awards
		internationalA = self.international_a * 2
		nationalA = self.national_a * 1.8
		statelevelA = self.state_level_a * 1.6
		interclgA = self.intercollegiate * 1.4
		mark2 = internationalA*nationalA*statelevelA*interclgA

		#mapping
		map_out = self.mapping
		mapdict = {'Strongly to PO(1.5)': 1.5, 'Moderately to PO(1)': 1, 'Moderately to CO(0.8)': 0.8, 'Neither mapping to PO nor CO (0)': 0}
		mark3 = mapdict.get(map_out, 0) 
		frappe.msgprint(f'mark={mark3}')


		wtg = mark1+mark2+mark3
		marks = wtg*75
		marksDict['total_marks'] = marks
		return marksDict

def sumDocs(current_frm, method):
 filters = {
  "name": ["like", current_frm.name[:-2] + "%"]
 }
 field = 'name'
 similar_docs = frappe.get_list("BSA-Co-curricular", filters= filters, pluck = field)
 if len(similar_docs) == 2:
          for doc_name in similar_docs:
               if doc_name != current_frm.name:
                     old_doc_name = doc_name # current form
          e_doc = frappe.get_doc(Doctype, old_doc_name) # purana wala form
          e_score = e_doc.obtained_marks # old score
          sum_score = e_score+current_frm.obtained_marks # current_frm is current form, e_score is purana wale ka marks
          e_doc.db_set('self_appraisal_score', sum_score , commit = True)
          current_frm.db_set('self_appraisal_score', sum_score , commit = True)

		


