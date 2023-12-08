import frappe

import secrets
import string

from datetime import datetime

# Create a datetime object representing "2023-12-08 10:00:00"
def get_datetime():
  date_string = "2023-12-08 10:00:00"
  datetime_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

  return str(datetime_object)


def generate_random_string():
    l = []
    for i in range(0,6):
      alphabet = string.ascii_lowercase + string.digits
      random_string = ''.join(secrets.choice(alphabet) for _ in range(10))
      l.append(random_string)
    return l

def insert():
  try:
    time_str = get_datetime()
    parentval = 'Peer reviewed publications'
    nameval = generate_random_string()

    one = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 0, '{parentval}', 'reviewer', 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 , NULL, NULL, NULL, NULL);""".format(nameval = nameval[0], parentval = parentval, time_str = time_str)
    
    two = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 3, '{parentval}', 'reviewer', 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0 , NULL, NULL, NULL, NULL);""".format(nameval = nameval[1], parentval = parentval, time_str = time_str)    

    three = """INSERT INTO `tabCustom DocPerm`(name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 0, '{parentval}', 'reviewer', 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, NULL, NULL, NULL, NULL);""".format(nameval = nameval[2], parentval = parentval, time_str = time_str)

    four = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 1, '{parentval}', 'System Manager', 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL);""".format(nameval = nameval[3], parentval = parentval, time_str = time_str)

    five = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 2 , '{parentval}', 'vit_emp', 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0,NULL, NULL, NULL, NULL);""".format(nameval = nameval[4], parentval = parentval, time_str = time_str)    

    six = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 0, '{parentval}', 'vit_emp',0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL);""".format(nameval = nameval[5], parentval = parentval, time_str = time_str)

    print('reference query : \n', one, '\n')

    frappe.db.sql(one)
    frappe.db.sql(two)
    frappe.db.sql(three)
    frappe.db.sql(four)
    frappe.db.sql(five)
    frappe.db.sql(six)

    frappe.db.commit()

    print('success')

  except Exception as e:
    print(e)






