import frappe
import json



@frappe.whitelist()
def getData():
	# query = """SELECT i.professor, .proficiency, a.evaluation_date, c.employee_name AS reviewer ,e.department FROM `tabEmployee Skill` AS a JOIN `tabEmployee Skill Map` AS b ON a.parent = b.name JOIN `tabEmployee` AS e ON a.parent = e.name JOIN `tabEmployee` as c ON b.reviewer = c.company_email  WHERE evaluation_date >= DATE('{pb}') AND evaluation_date <= DATE('{pe}')""".format(pb = pb, pe = pe)
  pass