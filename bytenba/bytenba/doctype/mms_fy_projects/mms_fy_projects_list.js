frappe.listview_settings['MMS FY Projects'] = {
  hide_name_column: true,
  refresh: function(listview) {
    $(".comment-count").hide();
    $(".frappe-timestamp").hide();
    $(".avatar-small").hide();
  }
}
