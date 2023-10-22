import frappe
from frappe import _
from frappe.utils.dashboard import cache_source


@frappe.whitelist()
@cache_source
def get(
	chart_name=None,
	chart=None,
	no_cache=None,
	filters=None,
	from_date=None,
	to_date=None,
	timespan=None,
	time_interval=None,
	heatmap_year=None,
):
	return {
		"labels": ["12am-3am", "3am-6am", "6am-9am", "9am-12pm",
    "12pm-3pm", "3pm-6pm", "6pm-9pm", "9pm-12am"],
		
		"datasets": [
		{
			"name": "Some Data",
			"values": [25, 40, 30, 35, 8, 52, 17, -4]
		},
		{
			"name": "Another Set",
			"values": [25, 50, -10, 15, 18, 32, 27, 14]
		},
		{
			"name": "Yet Another",
			"values": [15, 20, -3, -15, 58, 12, -17, 37]
		}
	],
	
		"type": "bar",
	}