// Copyright (c) 2023, byte_team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lab work-Case study', {
    onload: function(frm) {
        // Hide the 'quality_score' field when the form loads
        frm.toggle_display('quality_score', false);
    },
    for_engineering: function(frm) {
        const opt1 = "Uploading videos of new experiments/PBL prepared during the PA evaluation period";
        if (frm.doc.for_engineering != opt1) {
            // Show the 'quality_score' field if the selected option is not 'opt1'
            frm.toggle_display('quality_score', true);
        } else {
            // Hide the 'quality_score' field if the selected option is 'opt1'
            frm.toggle_display('quality_score', false);
        }
		frm.refresh_field('quality_score');
    },
    refresh(frm) {
    var currentUser = frappe.session.user;
    frm.set_value('professor', currentUser);
	},
    // validate: function(frm) {
    //     const opt1 = "Uploading videos of published case studies";
    //     const opt2 = "Case study published including last 6 months";
    //     if (frm.doc.mms_a < 0 || frm.doc.mms_a > 1.5) {
    //         frappe.msgprint(__('The float value for '+opt1+ ' should be between 0 and 1.5'));
    //         frappe.validated = false; // This will prevent the form from being saved
    //     }
    //     if (frm.doc.mms_b < 0 || frm.doc.mms_b > 1) {
    //         frappe.msgprint(__('The float value for '+opt2+ ' should be between 0 and 1'));
    //         frappe.validated = false; // This will prevent the form from being saved
    //     }
    // }
});

