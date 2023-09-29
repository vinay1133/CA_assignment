# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Course_Laboutcomeattainment(Document):
	def before_save(self):
		total = 0
		count = 0
		for item in self.enter_courselab_name:
			total += item.attainment
			count+=1
		self.average_attainment = (total)/count
		if self.average_attainment>2 and self.average_attainment<=3:
			self.self_appraisal_score=200
		elif self.average_attainment>1 and self.average_attainment<=2:
			self.self_appraisal_score=150
		elif self.average_attainment>0 and self.average_attainment<=1:
			self.self_appraisal_score=100
		else:
			self.self_appraisal_score=0
