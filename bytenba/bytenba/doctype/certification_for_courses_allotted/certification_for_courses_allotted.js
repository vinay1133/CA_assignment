// Copyright (c) 2023, byte_team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Certification for courses allotted', {
  refresh: function(frm) {
    if (frm.doc.__islocal) {
      var currentUser = frappe.session.user;
      frm.set_value('professor', currentUser);
    }
    if (!frm.doc.owner) {
      var currentUser = frappe.session.user;
      frm.set_value('professor', currentUser);
    }
  }
});
