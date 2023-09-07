frappe.ui.form.on("Certification for courses allotted", {
	refresh(frm) {
		frm.set_query('reviewer', function() {
			return {
				query: "bytenba.bytenba.doctype.certification_for_courses_allotted.certification_for_courses_allotted.get_professor_names"
			};
		});
		frm.refresh_field("reviewer");
	}
});