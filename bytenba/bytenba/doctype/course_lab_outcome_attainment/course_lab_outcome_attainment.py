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
