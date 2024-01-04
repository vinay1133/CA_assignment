import frappe

@frappe.whitelist()
def approve(**kwargs):

  #get user and their roles
  user = kwargs['session_user']
  owner = kwargs['owner']
  roles = frappe.get_roles(user)

  is_reviewer = True if 'reviewer' in roles else False
  is_admin = True if 'Administrator' in roles else False

  doctype = kwargs['doctype']
  doc_name = kwargs['name']
  rsc = kwargs['rsc']

  doc = frappe.get_doc(doctype, doc_name)
  #check if doc is already approve
  if doc.approved == 1:
    frappe.throw('Revoke approval before putting new reviewer score')


  if is_admin:
    pass
  else:
    if not is_reviewer:
      frappe.throw("""Form cannot be validated by faculty""")

    #check if user is not approving his own form
    if user == owner:
      frappe.throw("""Form cannot be validated by user who is the form creator""")

    #check reviewer belongs to same department
    form_owner_dept = frappe.db.get_value("Professors", owner, "department")
    form_user_dept = frappe.db.get_value('Professors', user, "department")
    if form_owner_dept != form_user_dept:
      frappe.throw("""From can only be approved by reviewer belonging to same department as form owner""")
  
  doc.reviewer_score = rsc
  doc.approved = 1
  doc.save(ignore_permissions=True,)
  frappe.db.commit()

  return 'ok'


@frappe.whitelist()
def revoke(**kwargs):

  #get user and their roles
  user = kwargs['session_user']
  owner = kwargs['owner']

  roles = frappe.get_roles(user)
  is_reviewer = True if 'reviewer' in roles else False
  is_admin = True if 'Administrator' in roles else False
  doctype = kwargs['doctype']
  doc_name = kwargs['name']

  doc = frappe.get_doc(doctype, doc_name)
  #check if doc is already not approve
  if doc.approved == 0:
    frappe.throw('Cannot revoke unapproved form')


  if is_admin:
    pass
  else:

    if not is_reviewer:
      frappe.throw("""From cannot be revoked by faculty""")

    #check if user is not approving his own form 
    if user == owner:
      frappe.throw("""Form cannot be revoked by faculty who is the form creator""")

    #check reviewer belongs to same department        
    form_owner_dept = frappe.db.get_value("Professors", owner, "department")
    form_user_dept = frappe.db.get_value('Professors', user, "department")
    if form_owner_dept != form_user_dept:
      frappe.throw("""From can only be approved by reviewer belonging to same department as form owner""")
  
  doc.approved = 0
  doc.reviewer_score = None
  doc.save(ignore_permissions=True,)
  frappe.db.commit()

  return 'ok'

