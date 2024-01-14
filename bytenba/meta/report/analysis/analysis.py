import frappe
import pandas as pd
from frappe.utils import today

def execute(filters=None):
	
	academic_year = filters.get('academic_year', today()[0:4])
	semester = filters.get('semester', 'Odd')
	department = filters.get('department', '')
	faculty_designation = filters.get('designation', '')
	# bucket = filters.get('bucket', '')

	sql = """SELECT p.full_name as Faculty, p.user_id as 'Employee Code', p.department as Department, p.faculty_designation as Designation, COALESCE(c.reviewer_score, "Pending") as "AI 1", COALESCE(co.reviewer_score, "Pending") as "AI 2"
  FROM `tabProfessors` as p
  JOIN `tabCertification for courses allotted` as c
  ON p.name = c.owner
	JOIN `tabCourses taught` as co
	ON p.name = co.owner
	WHERE p.department like '{department}'
  AND p.faculty_designation like '{faculty_designation}'
	AND c.academic_year = '{academic_year}'
	AND c.semester = '{semester}'
	AND co.academic_year = '{academic_year}'
	AND co.semester = '{semester}'
  """.format(department = department + "%", faculty_designation = faculty_designation + "%", academic_year = academic_year, semester = semester)

	data = frappe.db.sql(sql, as_dict=True)

  # Convert data to Pandas DataFrame
	result = [dict(row) for row in data]
	df = pd.DataFrame(result)
	column_names = df.columns.tolist()
	

	"""SEND DATA as a report	"""
	columns = []
	for name in column_names:
		columns.append({"fieldname": name,"label": name})
	data_dict = df.to_dict('records')	

	return columns, data_dict