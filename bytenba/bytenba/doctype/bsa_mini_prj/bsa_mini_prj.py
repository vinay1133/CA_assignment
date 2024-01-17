# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'
Doctype = 'BSA-Mini Prj'

class BSAMiniPrj(Document):
    def before_save(self):
        self.self_appraisal_score = compute_marks(self)
	
    def autoname(self):
        self.name = f'AI3.4_{self.owner}_{self.academic_year}_{self.semester}'

    def validate(self):
        validation.standard_validation(self)

def compute_marks(self):

    match = re.search(pattern_for_wtg, self.type_of_guide)
    if match:
        val1 = float(match.group(1).strip())
    else:
        frappe.throw('Error Fetching Field Weightages')			

    match = re.search(pattern_for_wtg, self.type_of_organistion_of_industry_coguide)
    if match:
        val2 = float(match.group(1).strip())
    else:
        frappe.throw('Error Fetching Field Weightages')

    match = re.search(pattern_for_wtg, self.type_of_project)
    if match:
        val3 = float(match.group(1).strip())
    else:
        frappe.throw('Error Fetching Field Weightages')

    match = re.search(pattern_for_wtg, self.mapping)
    if match:
        val4 = float(match.group(1).strip())
    else:
        frappe.throw('Error Fetching Field Weightages')

    return round(val1*val2*val3*val4*75)