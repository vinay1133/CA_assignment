frappe.listview_settings['BSA guest lecture'] = {
  hide_name_column: true,
  refresh: function(listview) {
    $(".comment-count").hide();
    $(".frappe-timestamp").hide();
    $(".avatar-small").hide();
  }
}

