// Copyright (c) 2023, byte_team and contributors
// For license information, please see license.txt

// frappe.ui.form.on("MMS FY Projects", {
// 	refresh(frm) {

// 	},
// });
// Copyright (c) 2023, byte_team and contributors
// For license information, please see license.txt

frappe.ui.form.on("MMS FY Projects", {
  refresh: function(frm) {
    //owner and local criteria
    if (frm.doc.__islocal && !frm.doc.owne) {
      var currentUser = frappe.session.user;
      frm.set_value('professor', currentUser);
    }
    //get reviewer
    frappe.call({
      method: 'bytenba.get_reviewer.get_reviewer',
      args: {
          'session_user': frappe.session.user
      },
      callback: function(response) {
          if (response) {
              frm.set_value('reviewer', response.message)
          }
      }
  });
  //set academic year by default
  frm.set_value('academic_year', getAY())
  frm.doc.professor.click()
  }
});
function getAY(){
  var currentYear = frappe.datetime.get_today().split("-")[0];
  var nextYear = String(parseInt(currentYear) + 1);
  academic_year =  currentYear + "-" + nextYear;
  return academic_year
}
