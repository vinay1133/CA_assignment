frappe.ui.form.on("Exam related work", {
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
	frm.set_value('academic_year', getAY());
  }
});