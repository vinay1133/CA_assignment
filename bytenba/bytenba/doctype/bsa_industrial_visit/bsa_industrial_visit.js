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
  }
});
