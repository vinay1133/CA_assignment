frappe.listview_settings['Certification for courses allotted'] = {
  hide_name_column: true,
  refresh: function(listview) {
    $(".comment-count").hide();
    $(".frappe-timestamp").hide();
    $(".avatar-small").hide();
  }
}

