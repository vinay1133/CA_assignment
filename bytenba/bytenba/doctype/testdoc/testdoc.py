# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
# from frappe.model.document import Document


# class testDoc(Document):
# 	pass
@frappe.whitelist()
def api_check():
  return {'ishaan': "hello"}