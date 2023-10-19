frappe.pages['control'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Admin',
		single_column: true
	});
}