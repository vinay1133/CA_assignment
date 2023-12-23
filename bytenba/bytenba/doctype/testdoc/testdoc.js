
const DocType = "testDoc"

frappe.ui.form.on(DocType, {
    refresh: function(frm) {
      
      $('#customButton').on('click', function() {
        let d = new frappe.ui.Dialog({
          title: 'Attach Evidence',
          fields: [
              {
                  label: 'Link',
                  fieldname: 'link_evidence',
                  fieldtype: 'Data'
              },
              {
                  label: 'Attach File',
                  fieldname: 'attach_evidence',
                  fieldtype: 'Attach'
              }
          ],
          size: 'small', 
          primary_action_label: 'Submit',
          primary_action(values) {
              console.log(values);
              d.hide();
          }
        });
        d.show()
      });  

    }
});