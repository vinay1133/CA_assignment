const DocType = "Internal revenue generation"

frappe.ui.form.on(DocType, {

	approved: function(frm){
		if(frm.doc.approved == 1){
			frm.set_df_property("reviewer_score", "read_only", 1)
		}
		if(frm.doc.approved == 0){
			frm.set_df_property("reviewer_score", "read_only", 0)
		}
	},

	// view_evidence: function(frm){
	// 	var evi_link = frm.doc.link_for_evidence
	// 	if (evi_link){
	// 		url = "http://localhost:8000" + evi_link
	// 		window.open(url, "_blank");
	// 	}
	// 	else{
	// 		frappe.msgprint('No evidence provided')
	// 	}
	// },
	uploadbutton: function(frm){		
		const fileInput = document.getElementById('fileInput').files[0]; // Fetch the file input element

		const formData = new FormData();
		formData.append('file', fileInput);
		
		// Read file as data URL 
		const reader = new FileReader();
		reader.onload = function(event) {
				const dataURL = event.target.result;
		
				frappe.call({
						method: 'bytenba.custom_utilities.evidenceUpload',
						args: {
								fileData: dataURL.split(',')[1], // Send only the base64 encoded data
						},
						callback: function(r) {
								if (r.message === 'file gotten') {
										frappe.msgprint('Success');
								} else {
										frappe.msgprint('Error');
								}
						}
				});
		};
		
		reader.readAsDataURL(fileInput);
		
	},
	
  refresh: function(frm) {

    if (frm.doc.__islocal) {
      var currentUser = frappe.session.user;
      frm.set_value('professor', currentUser);
    }
				
		frm.add_custom_button(__("New Form"), () => {			
			frappe.confirm('Create new form?',
			() => {
				frappe.new_doc(DocType, {})
			}, () => {
				frm.refresh()
			})
		}).css({'color':'white','font-weight': 'normal', background: '#2490ef'});

		frappe.call({
			method: 'bytenba.get_reviewer.get_reviewer',
			args: {
					'session_user': frappe.session.user
			},
			callback: function(response) {
					if (response) {
							frm.set_value('reviewer', response.message)
					}
			}
	});
	frm.set_value('academic_year', getAY());
  },

	onload: function(frm){
		if(frm.doc.self_appraisal_score && frm.doc.approved == 0){
			frm.set_value('reviewer_score', frm.doc.self_appraisal_score)
		}
		if (frm.doc.owner != frappe.session.user && frappe.user.has_role('reviewer') == 1){
			$.each(frm.fields_dict, function(fieldname, field) {
				if(fieldname === 'approved'){
	        frm.set_df_property(fieldname, "read_only", 0)
	      }
	      else{
	      frm.set_df_property(fieldname, "read_only", 1)	
	      }
	    });
			frm.set_df_property("reviewer_score", "read_only", 0)
		}
	},

});

function getAY(){
	var currentYear = frappe.datetime.get_today().split("-")[0];
	var nextYear = String(parseInt(currentYear) + 1);
	academic_year =  currentYear + "-" + nextYear;
	return academic_year
}

let d = new frappe.ui.Dialog({
	title: 'Enter details',
	fields: [
			{
					label: 'First Name',
					fieldname: 'first_name',
					fieldtype: 'Data'
			},
			{
					label: 'Last Name',
					fieldname: 'last_name',
					fieldtype: 'Data'
			},
			{
					label: 'Age',
					fieldname: 'age',
					fieldtype: 'Int'
			}
	],
	size: 'small', // small, large, extra-large 
	primary_action_label: 'Submit',
	primary_action(values) {
			console.log(values);
			d.hide();
	}
});