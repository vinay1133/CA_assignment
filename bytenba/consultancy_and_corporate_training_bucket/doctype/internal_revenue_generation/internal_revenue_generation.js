const DocType = "Internal revenue generation"

frappe.ui.form.on(DocType, {

  refresh: function(frm) {
		
		if (frappe.session.user == "Administrator"){
			frm.set_value('professor', "Administrator");
			frm.set_value('reviewer', "Administrator");
		}
		else
		{		
			frappe.call({
					method: 'bytenba.get_reviewer.get_reviewer',
					args: {
							'session_user': frappe.session.user
					},
					callback: function(response) {
							if (response) {
									frm.set_value('reviewer', response.message[0])
									if (frm.doc.owner == frappe.session.user){
										// frm.set_value('professor', response.message[1]);
										if (frm.doc.__islocal) {
											frm.set_value('professor', response.message[1]);
										}
									}
							}
					}
			});
		}
		
		if (frappe.user.has_role('Administrator') || frappe.user.has_role('reviewer'))
		{
		frm.add_custom_button(__(frm.doc.approved == 1 ? "Revoke" : "Approve"), () => {
				if (frm.doc.approved == 0){
				let d = new frappe.ui.Dialog({
					title: 'Approve self appraisal score',
					fields: [
							{
									label: 'Self Appraisal Score',
									fieldname: 'sapc',
									fieldtype: 'Read Only',
									default: frm.doc.self_appraisal_score

							},
							{
									label: 'Reviewer Score',
									fieldname: 'rsc',
									fieldtype: 'Int',
									default: frm.doc.self_appraisal_score
							},
					],
					size: 'small', // small, large, extra-large 
					primary_action_label: 'Approve',
					primary_action(values) {
						frappe.call({
							method: 'bytenba.approveScore.approve',
							args: {
									
									'session_user': frappe.session.user,
									'owner': frm.doc.owner,
									'doctype': frm.doc.doctype,
									'name': frm.doc.name,
									'rsc': values.rsc

							},
							callback: function(response) {
									if (response) {
											if (response.message == 'ok'){
												frm.refresh()
												}
										}
								}
						});
							d.hide();
					}
			});
			d.show();
			}
			
			if (frm.doc.approved == 1){
				frappe.confirm(
					'Are you sure you want to revoke approval on this form?',
					function(){
						frappe.call({
							method: 'bytenba.approveScore.revoke',
							args: {
									'session_user': frappe.session.user,
									'owner': frm.doc.owner,
									'doctype': frm.doc.doctype,
									'name': frm.doc.name,
							},
							callback: function(response) {
									if (response) {
											if (response.message == 'ok'){
												frm.refresh()
												}
										}
								}
						});
					},
					function(){
							frappe.msgprint('Approval NOT revoked')
					}
				)
			}
		}).css({'color':'white','font-weight': 'normal', background: frm.doc.approved == 1 ? "#000000" : "#2490ef"});
		}
		//if form approved and user is not reviewer or administrator 
		if(frm.doc.approved == 1 && (frappe.user.has_role('reviewer') != 1 || frappe.user.has_role('Administrator') != 1)){
			$.each(frm.fields_dict, function(fieldname, field) {
	      frm.set_df_property(fieldname, "read_only", 1)	
	    });
		}
		frm.set_value('academic_year', getAY());
		frm.dashboard.hide()
  }
});

function getAY(){
	var currentYear = frappe.datetime.get_today().split("-")[0];
	var nextYear = String(parseInt(currentYear) + 1);
	academic_year =  currentYear + "-" + nextYear;
	return academic_year
}

