# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

pattern = re.compile(r'^\d{4}-\d{4}$')

class InnovationinTLP(Document):
	def before_save(self):
		

		"""get mark1"""
		participants_int = self.no_of_participants
		enrolled_int = self.no_of_enrollments
		mark1 = participants_int / enrolled_int
		
		"""get mark2 cluster"""
		no1 = self.quality_of_assignments
		no2 = self.quality_of_tests
		no3 = self.quality_of_experiment
		no4 = self.activities_done_outside_the_classroom
		no5 = self.activities_for_slow_learners
		no6 = self.activities_for_advance_learners
		sum1 = no1+no2+no3+no4+no5
		mark2 = sum1 / 6
		

		"""get mark3 mapping"""
		map_out = self.mappinng
		mapdict = {'Strongly to PO(1.5)': 1.5, 'Moderately to PO(1)': 1, 'Moderately to CO(0.8)': 0.8, 'Neither mapping to PO nor CO (0)': 0}
		mark3 = mapdict.get(map_out, 0)
		
		"""get mark4 assessment"""
		act_int = self.no_of_activities
		mark4 = act_int * 0.25
		

		product_of_wtg = mark1*mark2*mark3*mark4
		marks = product_of_wtg*150
		frappe.msgprint(f'marks {marks}')

		self.obtained_marks = marks

	def autoname(self):
		self.name = f'AI6_{self.academic_year}_{self.professor}'

	def validate(self):

		# no of participants
		enrolled = self.no_of_enrollments
		participants=self.no_of_participants
		if participants > enrolled:
			frappe.throw('Number of participants should be less than number of students enrolled')
		
		# clusters
		no1 = self.quality_of_assignments
		no2 = self.quality_of_tests
		no3 = self.quality_of_experiment
		no4 = self.activities_done_outside_the_classroom
		no5 = self.activities_for_slow_learners
		no6 = self.activities_for_advance_learners
		list1={no1,no2,no3,no4,no5,no6}
		for x in list1:
			if int(x)<0 or int(x)>1:
				frappe.throw('All fields under the cluster should be between 0 to 1.')

		# assessment(term work)
		activities = self.no_of_activities
		if activities < 4:
			frappe.throw('Minimum nunmber of activities considered for term work should be 4')

		#academic yr
		academic_yr_str = self.academic_year
		if not re.match(pattern, academic_yr_str):
			frappe.throw('Academic year must be of the form like 2022-2023')


