frappe.provide('frappe.dashboards.chart_sources');

frappe.dashboards.chart_sources["AI1 CS 1"] = {
	method: "bytenba.bytenba.dashboard_chart_source.ai1_cs_1.ai1_cs_1.get",
	filters: [
		{
			// fieldname: "company",
			// label: __("Company"),
			// fieldtype: "Link",
			// options: "Company",
			// default: frappe.defaults.get_user_default("Company")
		}
	]
};