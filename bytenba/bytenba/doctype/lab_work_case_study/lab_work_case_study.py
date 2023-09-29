# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

Doctype="Lab work-Case study"
pattern = re.compile(r'^\d{4}-\d{4}$')
mapping_mapping = {"Strongly to CO":1, "Moderately to CO":0.8, "Not mapped to CO":0}

class LabworkCasestudy(Document):

    def before_save(self):
          marks_obtained(self)
     
    """method to autoname your document"""
    def autoname(self):
     base_name = f'AI4_{self.academic_year}_{self.professor}'
     data = renameDoc(base_name, self.academic_year)
     if data['name_value']:
          self.name = data['name_value']
     else:
          frappe.throw("Failed to generate a unique name.")
       
    def validate(self):
            """validation for MMS"""
            mms_a="Uploading videos of published case studies"
            mms_b="Case study published including last 6 months"
            mms_a_val = self.mms_a
            if mms_a_val!=1.5:
                 frappe.throw(f"Value for {mms_a} should be: 1.5")
            mms_b_val = self.mms_b
            if mms_b_val!=1:
                 frappe.throw(f"Value for {mms_b} should be: 1")
            
            """validation for Engineering"""
            engg_a="Uploading videos of new experiments/PBL prepared during the PA evaluation period"
            engg_b="Use of new tools/simulators/virtual lab"
            engg_c="Quality of PB statements"
            engg_d="Continuous assessment"
            engg_a_val = self.engg_a
            if engg_a_val<0 or engg_a_val>1.5:
                 frappe.throw(f"Value for {engg_a} should be between: 0 to 1.5")
            engg_b_val = self.engg_b
            if engg_b_val<0 or engg_b_val>1.25:
                 frappe.throw(f"Value for {engg_b} should be between: 0 to 1.25")
            engg_c_val = self.engg_c
            if engg_c_val<0 or engg_c_val>1:
                 frappe.throw(f"Value for {engg_c} should be between: 0 to 1")
            engg_d_val = self.engg_d
            if engg_d_val<0 or engg_d_val>1:
                 frappe.throw(f"Value for {engg_d} should be between: 0 to 1")
          
            """Validation for academic year"""
            academic_yr_str = self.academic_year
            if not re.match(pattern, academic_yr_str):
                   frappe.throw('Academic year must be of the form like 2022-2023')


def marks_obtained(self):
     """Product of weightages"""
     mms_a_val=self.mms_a
     mms_b_val=self.mms_b
     engg_a_val=self.engg_a
     engg_b_val=self.engg_b
     engg_c_val=self.engg_c
     engg_d_val=self.engg_d
     mapping_param = mapping_mapping.get(self.mapping_opts,0)
     prod_of_wts = mms_a_val*mms_b_val*engg_a_val*engg_b_val*engg_c_val*engg_d_val*mapping_param

     """Marks Obtained"""
     marks_obt = 100*prod_of_wts  
     self.marks_gained=marks_obt    
     return marks_obt

def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Lab work-Case study", filters= filters, pluck = field)
	if len(similar_docs) == 0:
		dict['name_value'] = base_name + '_0'
		return dict
	if len(similar_docs) == 1:
		form_num = int(similar_docs[0][-1])
		new_num = form_num + 1
		dict['name_value'] = f"{base_name}_{new_num}"
	elif len(similar_docs) == 2:
			frappe.throw(f'Maximum limit of 2 for AI4 forms for the academic year {academic_year} has been reached, kindly delete existing forms to create more')
	else:
			frappe.throw(f'Something went wrong')
	return dict

def avgDocs(current_frm, method):
	filters = {
		"name": ["like", current_frm.name[:-2] + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Lab work-Case study", filters= filters, pluck = field)
	if len(similar_docs) == 2:
          for doc_name in similar_docs:
               if doc_name != current_frm.name:
                     old_doc_name = doc_name # current form
          e_doc = frappe.get_doc(Doctype, old_doc_name) # purana wala form
          e_score = e_doc.marks_gained # old score
          avg_score=(e_score+current_frm.marks_gained)/2 # current_frm is current form, e_score is purana wale ka marks
          e_doc.db_set('self_appraisal_score', avg_score , commit = True)
          current_frm.db_set('self_appraisal_score', avg_score , commit = True)
          