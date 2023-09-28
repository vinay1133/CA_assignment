# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LabworkCasestudy(Document):
    def before_save(self):
        # mms_str = self.for_mms
        # mms_mapping = {"Uploading videos of published case studies":1.5, "Case study published including last 6 months":1}
        # mms_param = mms_mapping.get(mms_str,0)
        
        # engg_str = self.for_engg
        # engg_mapping = {"Uploading videos of new experiments/PBL prepared during the PA evaluation period":1.5, "Use of new tools/simulators/virtual lab":1.25, "Quality of PB statements":1, "Continuous assessment":1}
        # engg_param = mms_mapping.get(engg_str,0)
        
        mapping_str = self.mapping_opts
        mapping_mapping = {"Strongly to CO":1, "Moderately to CO":0.8, "Not mapped to CO":0}
        mapping_param = mapping_mapping.get(mapping_str,0)
        
    def validate(self):
            """validation for MMS"""
            mms_a="Uploading videos of published case studies"
            mms_b="Case study published including last 6 months"
            mms_a_val = self.mms_a
            if mms_a_val!=1.5:
                 frappe.throw(f"Value for {mms_a} should be: 1.5")
            mms_b_val = self.mms_b
            if mms_b_val!=1:
                 frappe.throw(f"Value for {mms_b} should be: 1")
            
            """validation for Engineering"""
            engg_a="Uploading videos of new experiments/PBL prepared during the PA evaluation period"
            engg_b="Use of new tools/simulators/virtual lab"
            engg_c="Quality of PB statements"
            engg_d="Continuous assessment"
            engg_a_val = self.engg_a
            if engg_a_val<0 or engg_a_val>1.5:
                 frappe.throw(f"Value for {engg_a} should be between: 0 to 1.5")
            engg_b_val = self.engg_b
            if engg_b_val<0 or engg_b_val>1.25:
                 frappe.throw(f"Value for {engg_b} should be between: 0 to 1.25")
            engg_c_val = self.engg_c
            if engg_c_val<0 or engg_c_val>1:
                 frappe.throw(f"Value for {engg_c} should be between: 0 to 1")
            engg_d_val = self.engg_d
            if engg_d_val<0 or engg_d_val>1:
                 frappe.throw(f"Value for {engg_d} should be between: 0 to 1")
            