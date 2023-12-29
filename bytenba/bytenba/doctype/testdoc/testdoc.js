
const DocType = "testDoc"

frappe.ui.form.on(DocType, {
    refresh: function(frm) {

      if (frm.doc.__islocal) {
        var currentUser = frappe.session.user;
        frm.set_value('autocomplete_hfeq', currentUser);
      }

    }
});