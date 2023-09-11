frappe.ui.form.on("Certification for courses allotted", {
	refresh(frm) {
		frm.set_query('reviewer', function() {
			return {
				query: "bytenba.get_professors.get_professor_names"
			};
		});
		frm.refresh_field("reviewer");
	}
});
frappe.ui.form.on("Courses taught", {
	refresh(frm) {
		frm.set_query('reviewer', function() {
			return {
				query: "bytenba.get_professors.get_professor_names"
			};
		});
		frm.refresh_field("reviewer");
	}
});
frappe.ui.form.on("Course_Lab outcome attainment", {
	refresh(frm) {
		frm.set_query('reviewer', function() {
			return {
				query: "bytenba.get_professors.get_professor_names"
			};
		});
		frm.refresh_field("reviewer");
	}
});