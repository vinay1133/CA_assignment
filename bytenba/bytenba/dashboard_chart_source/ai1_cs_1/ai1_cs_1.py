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
		"labels": ["AI-1", "AI-2", "AI-3", "AI-3.1", "AI-3.2", "AI-3.3", "AI-3.4", "AI-4", "AI-5", "AI-6", "AI-7",  "AI-8",  "AI-9.1", "AI-9.2", "AI-10.1", "AI-10.2", "AI-11", "AI-12", "AI-13", "AI-14"],
		
		"datasets": [
		{
			"name": "Completed",
			"values": [1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2]
		},
		{
			"name": "Required",
			"values": [2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1]
		}
	],
	"type": "bar",
	"axisOptions": {
    "xAxisMode": 'tick' 
},
	}

	# return {
	# 	"labels": ["SD-1", "SD-2", "SD-3", "SD-4", "SD-5"],
		
	# 	"datasets": [
	# 	{
	# 		"name": "Completed",
	# 		"values": [1,2,1,2,2]
	# 	},
	# 	{
	# 		"name": "Required",
	# 		"values": [1,1,2,2,1]
	# 	}
	# ],
	# "type": "bar",
	# }

