frappe.listview_settings['ME Projects'] = {
  hide_name_column: true,
  refresh: function(listview) {
    $(".comment-count").hide();
    $(".frappe-timestamp").hide();
    $(".avatar-small").hide();
  }
}

