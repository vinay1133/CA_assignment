import frappe
import random
import secrets
import string

from datetime import datetime

# Create a datetime object representing "2023-12-08 10:00:00"
def get_datetime():
  current_date_time = datetime.now()
  formatted_string = current_date_time.strftime('%Y-%m-%d %H:%M:%S')
  return formatted_string

@frappe.whitelist()
def apiCheck(param =None):
  return frappe.db.sql(f"select full_name from `tabProfessors` where name = 'disha.singh@email.com'", as_dict= True)

def generate_random_string():
    l = []
    for i in range(0,6):
      alphabet = string.ascii_lowercase + string.digits
      random_string = ''.join(secrets.choice(alphabet) for _ in range(10))
      l.append(random_string)
    return l

def insert(doctype):

  try:
    time_str = get_datetime()
    parentval = doctype
    nameval = generate_random_string()

    namList = []
    namedata  = frappe.db.sql("""select name from `tabCustom DocPerm` where parent = "{parent}" order by role;""".format(parent = parentval), as_list = 1)
    for i in namedata:
      namList.append(i[0])

    if namList:
      for i in namList:
        frappe.sb.sql(f"delete from `tabCustom DocPerm` where name = '{i}'")
    
    frappe.db.commit()

    one = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 0, '{parentval}', 'reviewer', 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 , NULL, NULL, NULL, NULL);""".format(nameval = nameval[0], parentval = parentval, time_str = time_str)
    
    two = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 3, '{parentval}', 'reviewer', 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0 , NULL, NULL, NULL, NULL);""".format(nameval = nameval[1], parentval = parentval, time_str = time_str)    

    three = """INSERT INTO `tabCustom DocPerm`(name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 0, '{parentval}', 'reviewer', 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, NULL, NULL, NULL, NULL);""".format(nameval = nameval[2], parentval = parentval, time_str = time_str)

    four = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 1, '{parentval}', 'System Manager', 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL);""".format(nameval = nameval[3], parentval = parentval, time_str = time_str)

    five = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 2 , '{parentval}', 'vit_emp', 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0,NULL, NULL, NULL, NULL);""".format(nameval = nameval[4], parentval = parentval, time_str = time_str)    

    six = """INSERT INTO `tabCustom DocPerm` (name, creation, modified, modified_by, owner, docstatus, idx, parent, role, if_owner, permlevel, `select`, `read`, `write`, `create`, `delete`, submit, cancel, amend, report, export, import, share, print, email, _user_tags, _comments, _assign, _liked_by) VALUES ('{nameval}', '{time_str}', '{time_str}', 'Administrator', 'Administrator', 0, 0, '{parentval}', 'vit_emp',0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL);""".format(nameval = nameval[5], parentval = parentval, time_str = time_str)

    # print('reference query : \n', one, '\n')

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

def createUsers():

  json_file = [
  {
    "name_email": "madelonWashBrasher@vit.edu.in",
    "f_name": "Madelon",
    "m_name": "Wash",
    "l_name": "Brasher",
    "u_name": "madelonWashBrasher",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "lorenaEddyTimmens@vit.edu.in",
    "f_name": "Lorena",
    "m_name": "Eddy",
    "l_name": "Timmens",
    "u_name": "lorenaEddyTimmens",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Associate Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "rickNyeBrosini@vit.edu.in",
    "f_name": "Rick",
    "m_name": "Nye",
    "l_name": "Brosini",
    "u_name": "rickNyeBrosini",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "gillyAylmerPestricke@vit.edu.in",
    "f_name": "Gilly",
    "m_name": "Aylmer",
    "l_name": "Pestricke",
    "u_name": "gillyAylmerPestricke",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Associate Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "ashlieOnidaDemko@vit.edu.in",
    "f_name": "Ashlie",
    "m_name": "Onida",
    "l_name": "Demko",
    "u_name": "ashlieOnidaDemko",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "somersetNettyWillcox@vit.edu.in",
    "f_name": "Somerset",
    "m_name": "Netty",
    "l_name": "Willcox",
    "u_name": "somersetNettyWillcox",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Assistant Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "shanonSonniMattacks@vit.edu.in",
    "f_name": "Shanon",
    "m_name": "Sonni",
    "l_name": "Mattacks",
    "u_name": "shanonSonniMattacks",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Assistant Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "natalineTomlinZellner@vit.edu.in",
    "f_name": "Nataline",
    "m_name": "Tomlin",
    "l_name": "Zellner",
    "u_name": "natalineTomlinZellner",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Associate Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "graemeMorganaMcElroy@vit.edu.in",
    "f_name": "Graeme",
    "m_name": "Morgana",
    "l_name": "McElroy",
    "u_name": "graemeMorganaMcElroy",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Assistant Professor",
    "role": "vit_emp"
  },
  {
    "name_email": "dionysusParkerGriffey@vit.edu.in",
    "f_name": "Dionysus",
    "m_name": "Parker",
    "l_name": "Griffey",
    "u_name": "dionysusParkerGriffey",
    "department": "EXTC",
    "is_hod": 1,
    "faculty_designation": "Assistant Professor",
    "role": "reviewer"
  },
  {
    "name_email": "ariellaSadyeSterzaker@vit.edu.in",
    "f_name": "Ariella",
    "m_name": "Sadye",
    "l_name": "Sterzaker",
    "u_name": "ariellaSadyeSterzaker",
    "department": "EXTC",
    "is_hod": 0,
    "faculty_designation": "Not Applicable",
    "role": "department_executive"
  }
]




  frappe.db.begin()
  frappe.db.savepoint('savepoint')

  try:
    for obj in json_file:

      name_email = obj['name_email']
      f_name = obj['f_name']
      m_name = obj['m_name']
      l_name = obj['l_name']
      u_name = obj['u_name']
      full_name = f_name +" "+ m_name +" "+ l_name
      department = obj['department']
      is_hod = obj['is_hod']
      faculty_designation = obj['faculty_designation']
      role = obj['role']
    
      user_query = f"INSERT INTO `tabUser` (name, modified_by, owner, docstatus, idx, enabled, email, first_name, middle_name, last_name, username, send_welcome_email, unsubscribed, mute_sounds, logout_all_sessions, document_follow_notify, document_follow_frequency, follow_created_documents, follow_commented_documents, follow_liked_documents, follow_assigned_documents, follow_shared_documents, thread_notify, send_me_a_copy, allowed_in_mentions, simultaneous_sessions, login_after, login_before, bypass_restrict_ip_check_if_2fa_enabled, full_name) values ('{name_email}', 'Administrator', 'Administrator', 0, 0, 1, '{name_email}', '{f_name}', '{m_name}', '{l_name}', '{u_name}', 0, 0, 0, 1, 0, 'Daily', 0, 0 , 0, 0 , 0, 1, 0, 1, 1, 0, 0, 0, '{full_name}')"

      professor_query = f"INSERT INTO `tabProfessors` (name, user ,modified_by, owner, docstatus, idx, first_name, last_name, full_name, department, access_level, is_hod, email_id, faculty_designation) values ('{name_email}','{name_email}', 'Administrator', 'Administrator', 0, 0, '{f_name}', '{l_name}', '{full_name}', '{department}', 0, {is_hod}, '{name_email}', '{faculty_designation}')"

      alphabet = string.ascii_lowercase + string.digits
      name_random_string = ''.join(secrets.choice(alphabet) for _ in range(10))

      has_roles_query = f"INSERT INTO `tabHas Role` (name, modified_by, owner, docstatus, idx, role, parent, parentfield, parenttype) values ('{name_random_string}', 'Administrator','Administrator',0, 1, '{role}' , '{name_email}', 'roles', 'User')"

      frappe.db.sql(user_query)
      frappe.db.sql(professor_query)
      frappe.db.sql(has_roles_query)

      for i in ['Contacts','Workflow', 'Desk', 'Integrations', 'Custom', 'Automation','Core', 'Email', 'Social', 'Geo', 'Printing', 'Website']:
        alphabet = string.ascii_lowercase + string.digits
        name_random_string2 = ''.join(secrets.choice(alphabet) for _ in range(10))
        allow_modules_query = f"INSERT INTO `tabBlock Module` (name, modified_by, owner, docstatus, module, parent, parentfield, parenttype) values ('{name_random_string2}', 'Administrator', 'Administrator', 0, '{i}', '{name_email}', 'block_modules', 'User')"
        frappe.db.sql(allow_modules_query)
      
      k = input('Shall we commit?y/n')
      if k == 'y':
        frappe.db.commit()
        print('commited')
      if k == 'n':
        frappe.db.rollback()
  
  except Exception as e:
    print(e)
    frappe.db.rollback()


def addToCB1():
  
  frappe.db.begin()
  frappe.db.savepoint('savepoint')

  try:
    k = frappe.db.get_list('Professors', pluck='name',filters={'department': 'CMPN'},)
    k.remove('Administrator')
    k.remove('patrik.jane@vit.edu.in')
    
    col1Opts = ['Above 1 lakh (1.5)', 'Up to 1 lakh (1.25)', 'Up to 50 K (1)', 'Up to 25 K (0.8)', '5K to 25 K (0.5)']
    col2Opts = ['Individual Consultancy (1.5)', 'Convenor/PI(1)', 'Co-Convenor /Co-PI(0.8)', 'Organizing Secretary (0.6)', 'Member (0.3)']
    
    for prof in k:

      doc = frappe.new_doc("Internal revenue generation")
        
      doc.col1 = random.choice(col1Opts)
      doc.col2 = random.choice(col2Opts)
      doc.academic_year =  "2023-2024"
      doc.semester = "Even"
      doc.professor = prof
      doc.modified_by = prof
      # doc.CurrOwner = prof
      doc.reviewer = "Virat Ajay Kashyap"
      
      
      doc.insert(ignore_permissions=True)

      k = input('Shall we commit?y/n')
      if k == 'y':
        frappe.db.commit()
        print('commited')
      if k == 'n':
        frappe.db.rollback()

  except Exception as e:
    print(e)
    frappe.db.rollback()

import json 

def insertUser():
      
  frappe.db.begin()
  frappe.db.savepoint('savepoint')
  try:
    with open(f'/workspace/development/frappe-bench/apps/credence_hr/credence_hr/credence_hr/report/attrition_report/s12.json', 'r') as f:
      json_list = json.load(f)
    
    for doc in json_list:
        
        if doc["status"] == "Left":
          
          join_date = doc['date_of_joining']
          # random_date_str = random_date(join_date)
          start_date = datetime.strptime(join_date, '%Y-%m-%d').date()
          end_date = datetime.strptime('2022-12-31', '%Y-%m-%d').date()
          delta = end_date - start_date
          random_days = random.randrange(delta.days + 1)
          random_date = start_date + timedelta(days=random_days)
          doc["relieving_date"] = random_date.strftime('%Y-%m-%d')
      
          query = """
          INSERT INTO `tabEmployee` (name, employee, modified_by,owner, gender, date_of_joining, first_name, date_of_birth, middle_name, last_name, status, company, department, reports_to ,company_email, user_id, relieving_date) VALUES ('{name}', '{name}','Administrator','Administrator','{gender}', '{date_of_joining}', '{first_name}', '{date_of_birth}', '{middle_name}', '{last_name}', '{status}', '{company}', '{department}', '{reports_to}' ,'{company_email}', '{user_id}', '{relieving_date}')
          """.format(name = doc['name'], gender = doc['gender'], date_of_joining= doc['date_of_joining'], first_name= doc['first_name'], date_of_birth = doc['date_of_birth'], middle_name = doc['middle_name'], last_name = doc['last_name'], status=doc['status'], company ='personal', department = doc['department'], reports_to = 'HR-EMP-00001' ,company_email = doc['company_email'], user_id = doc['user_id'], relieving_date = doc['relieving_date'])
          
          frappe.db.sql(query)
          

        else:
            
            query = """
            INSERT INTO `tabEmployee` (name, employee, modified_by,owner, gender, date_of_joining, first_name, date_of_birth, middle_name, last_name, status, company, department, reports_to ,company_email, user_id) VALUES ('{name}', '{name}','Administrator','Administrator','{gender}', '{date_of_joining}', '{first_name}', '{date_of_birth}', '{middle_name}', '{last_name}', '{status}', '{company}', '{department}', '{reports_to}' ,'{company_email}', '{user_id}')
            """.format(name = doc['name'], gender = doc['gender'], date_of_joining= doc['date_of_joining'], first_name= doc['first_name'], date_of_birth = doc['date_of_birth'], middle_name = doc['middle_name'], last_name = doc['last_name'], status=doc['status'], company ='personal', department = doc['department'], reports_to = 'HR-EMP-00001' ,company_email = doc['company_email'], user_id = doc['user_id'])
            frappe.db.sql(query)
            
    
    k = input('Shall we commit?y/n')
    if k == 'y':
      frappe.db.commit()
      print('commited')

  except Exception as e:
    print(e)
    frappe.db.rollback()
    




