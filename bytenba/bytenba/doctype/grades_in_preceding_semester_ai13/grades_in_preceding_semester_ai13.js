frappe.ui.form.on("Grades in preceding semester AI13", {
  refresh: function (frm) {
    var currentUser = frappe.session.user;
    frm.set_value("professor", currentUser);
  },
});