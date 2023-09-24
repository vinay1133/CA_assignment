# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

doctype = 'BSA-Mini Prj'

class BSAMiniPrj(Document):
    def before_save(self):
        type_of_guide_str = self.type_of_guide
        guide_mapping = {"Industry expert as Co-guide":1.5, "Faculty guided only":1}
        guide_param = guide_mapping.get(type_of_guide_str,0)
        
        type_of_organistion_of_industry_coguide_str = self.type_of_organistion_of_industry_coguide
        org_coguide_mapping = {"MNC":1.5, "National":1.3, "SMEs":1.1, "None":1}
        org_coguide_param = org_coguide_mapping.get(type_of_organistion_of_industry_coguide_str,0)
        
        type_of_project_str=self.type_of_project
        project_mapping={"Functional Project":1,"Non-functional Project":0.5}
        project_param=project_mapping.get(type_of_project_str,0)
        
        mapping_str = self.mapping
        map_mapping = {"Strongly to PO":1.5, "Strongly to CO":1, "Moderately to PO":1, "Moderately to CO":0.8, "Neither PO nor CO":0}
        mapping_param = map_mapping.get(mapping_str,0)
        
        weightage = mapping_param*project_param*org_coguide_param*guide_param*75
        self.marks_obtained = weightage