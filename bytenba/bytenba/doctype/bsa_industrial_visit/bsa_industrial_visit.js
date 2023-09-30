// Copyright (c) 2023, byte_team and contributors
// For license information, please see license.txt

// frappe.ui.form.on("BSA industrial visit", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('BSA industrial visit', {
  refresh: function(frm) {
      // Get the current user's username
      var currentUser = frappe.session.user;

      // Set the value of the "Professor" field
      frm.set_value('professor', currentUser);

      // Make the "Professor" field read-only (optional)
      // frm.set_df_property('professor', 'read_only', 1);
  },
  onload: function(frm) {
    if (frm.doc.internships_status == "Equal to or more than 1 (1.2)") {
      frm.toggle_display('number_of_internships', true);
    }
    else{
      frm.toggle_display('number_of_internships', false);
    }
    if (frm.doc.projects_status == "Equal to or more than 1 (1.1)") {
      frm.toggle_display('number_of_projects', true);
    }
    else{
      frm.toggle_display('number_of_projects', false);
    }
  },
  internships_status: function(frm) {
    if (frm.doc.internships_status == "None (1)") {
        frm.toggle_display('number_of_internships', false);
    } else {
        frm.toggle_display('number_of_internships', true);
    }
  frm.refresh_field('number_of_internships');
  },
  projects_status: function(frm) {
    if (frm.doc.projects_status == "None (1)") {
        frm.toggle_display('number_of_projects', false);
    } else {
        frm.toggle_display('number_of_projects', true);
    }
  frm.refresh_field('number_of_projects');
  }
});