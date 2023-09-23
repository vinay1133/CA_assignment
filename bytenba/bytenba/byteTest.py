import random
import string
import frappe

def executeNOW():
    
    frappe.db.begin()
    frappe.db.savepoint('savepoint')
    try:

      prof = [
          {"first_name":"Mirabella","last_name":"Landall","emailid":"mlandall0@edublogs.org"},
          {"first_name":"Dexter","last_name":"Clarridge","emailid":"dclarridge1@fc2.com"},
          {"first_name":"Chelsy","last_name":"Vescovo","emailid":"cvescovo2@xinhuanet.com"},
          {"first_name":"Vinni","last_name":"Librey","emailid":"vlibrey3@liveinternet.ru"},
          {"first_name":"Rosemarie","last_name":"Handling","emailid":"rhandling4@usa.gov"},
          {"first_name":"Mort","last_name":"Phethean","emailid":"mphethean5@storify.com"},
          {"first_name":"Myrilla","last_name":"Petrillo","emailid":"mpetrillo6@seattletimes.com"},
          {"first_name":"Bax","last_name":"Crosen","emailid":"bcrosen7@stanford.edu"},
          {"first_name":"Leora","last_name":"Sommerland","emailid":"lsommerland8@multiply.com"},
          {"first_name":"Oriana","last_name":"Durnian","emailid":"odurnian9@artisteer.com"},
          {"first_name":"Georgeanne","last_name":"Scoines","emailid":"gscoinesa@jiathis.com"},
          {"first_name":"Nickolas","last_name":"Hazeldene","emailid":"nhazeldeneb@histats.com"},
          {"first_name":"Alane","last_name":"Westcarr","emailid":"awestcarrc@vistaprint.com"},
          {"first_name":"Carin","last_name":"Cleatherow","emailid":"ccleatherowd@yandex.ru"},
          {"first_name":"Samuel","last_name":"Plaide","emailid":"splaidee@imageshack.us"},
          {"first_name":"Jarrad","last_name":"Sharland","emailid":"jsharlandf@cornell.edu"},
          {"first_name":"Anna-diana","last_name":"Kohnemann","emailid":"akohnemanng@wordpress.org"},
          {"first_name":"Oralia","last_name":"Mecco","emailid":"omeccoh@i2i.jp"},
          {"first_name":"Sibel","last_name":"Crowdace","emailid":"scrowdacei@whitehouse.gov"},
          {"first_name":"Marietta","last_name":"Callear","emailid":"mcallearj@surveymonkey.com"},
      ]
      
      for emp in prof:
        
       # name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        
        sql = sql = """insert into `tabProfessors` (name, creation, modified, modified_by, owner, docstatus, idx, first_name, last_name, department, email, access_level)
         values ('{name}', '2023-09-02 11:00:25.707751', '2023-09-02 11:00:25.707751', 'Administrator', 'Administrator', 0, 0, '{fname}', '{lname}', 'Computers', '{emailid}', 1)""".format(name = emp['emailid'], fname=emp['first_name'], lname=emp['last_name'], emailid=emp['emailid'])

        # print(sql)
        frappe.db.sql(sql)
            
      k = input('Shall we commit?y/n')
      if k == 'y':
          frappe.db.commit()
          print('commited')
      if k == 'n':
            frappe.db.rollback()
        

    except Exception as e:

        print(e)
        frappe.db.rollback()

# def executeNOW():
    
#     frappe.db.begin()
#     frappe.db.savepoint('savepoint')
#     try:
        
#       sql = """SELECT CONCAT(first_name, ' ', last_name) AS full_name, name, department FROM tabProfessors"""
#       data = frappe.db.sql(sql, as_list = 1)
#       data_list = []
#       for i in data:
#         sublist = [i[0], i[1], i[2]]
#         data_list.append(sublist)
      
#       return data_list

#     except Exception as e:

#         print(e)
#         frappe.db.rollback()