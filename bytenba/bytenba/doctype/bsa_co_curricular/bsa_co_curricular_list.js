const DocType = "BSA-Co-curricular"

frappe.listview_settings[DocType] = {
  hide_name_column: true,
  refresh: function(listview) {
    // $(".comment-count").hide();
    $(".frappe-timestamp").hide();
    $(".avatar-small").hide();
  }
}

