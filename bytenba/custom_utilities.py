import datetime
from io import BytesIO
import frappe
import re
import os, uuid
import boto3, requests
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


# def validateAY(academic_yr_str):
# 	pattern_for_ay = re.compile(r'^\d{4}-\d{4}$')
# 	if re.match(pattern_for_ay, academic_yr_str):
# 		years = academic_yr_str.split("-")
# 		if int(years[1]) != int(years[0]) + 1:
# 				frappe.throw("Academic year entered incorrectly")
# 	else:
# 		frappe.throw("Academic year must be of the form like 2022-2023")

def standard_validation(self):

	existing_record = frappe.db.exists(self.doctype, {'name': self.name})
	if existing_record and existing_record != self.name:
		frappe.throw('There already exists such a record in the database')
	
	#validate academic year string
	# pattern_for_ay = re.compile(r'^\d{4}-\d{4}$')
	# if re.match(pattern_for_ay, self.academic_year):
	# 	years = self.academic_year.split("-")
	# 	if int(years[1]) != int(years[0]) + 1:
	# 			frappe.throw("Academic year entered incorrectly")
	# else:
	# 	frappe.throw("Academic year must be of the form like 2022-2023")
	pattern_for_ay = r'^20(2[4-9]|[3-9][0-9])$'
	if not re.match(pattern_for_ay, self.academic_year):
			frappe.throw("Academic year must be of the form like 2024")

	#get faculty information
	info = frappe.db.get_list('Professors', fields = ["select_reviewer", "full_name", "department", "faculty_designation"], filters={'name': ['=', self.owner]}, as_list=True, ignore_permissions = True)
	#validate Faculty
	if not self.reviewer == info[0][0]:
		frappe.throw('Error at reviewer')
	if not self.professor == info[0][1]:
		frappe.throw('Error at full name')
	if not self.department == info[0][2]:
		frappe.throw('Error at department')
	if not self.designation == info[0][3]:
		frappe.throw('Error at faculty designation')		
		
	roles = frappe.get_roles(self.modified_by)
	is_reviewer = True if 'reviewer' in roles else False
	is_admin = True if 'Administrator' in roles else False

	if self.approved == 1 and not is_reviewer and not is_admin:
		frappe.throw("Cannot modify document post approval")

# def validate_delete(doc, method):
# 	if doc.approved == 1 and not doc.modified_by == "Administrator":
# 		frappe.throw('Cannot delete document post approval')

@frappe.whitelist()
def evidenceUpload(fileData):
	AWS_ACCESS_KEY = 'AKIA2BMG37DHUNDSWJWC'
	AWS_SECRET_KEY = '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'
	AWS_S3_BUCKET_NAME = 'appraiseprofilestorage'
	AWS_REGION = 'us-west-2'
	LOCAL_FILE = fileData
	OBJECT_KEY = 'fromAppNEW.pdf'
	CONTENT_TYPE = 'application/pdf'

	# Assuming 'file' is the key containing the uploaded file in FormData
	fileData = {'file': '...'}

	# Get the file from the FormData
	file_content = fileData.get('file')  # Adjust accordingly if different key name

	if file_content:
			# Convert base64 data to bytes
			file_content = file_content.encode()

			# Create an in-memory stream with BytesIO
			file_stream = BytesIO(file_content)

			s3_client = boto3.client(
					service_name='s3',
					region_name=AWS_REGION,
					aws_access_key_id=AWS_ACCESS_KEY,
					aws_secret_access_key=AWS_SECRET_KEY
			)

			try:
					response = s3_client.upload_fileobj(
							file_stream,
							AWS_S3_BUCKET_NAME,
							OBJECT_KEY,
							ExtraArgs={'ContentType': CONTENT_TYPE}
					)
					print("File uploaded successfully to AWS S3")
			except Exception as e:
					print("Error uploading file to AWS S3:", e)
	else:
			print("File content not found in FormData")


@frappe.whitelist()
def uploadToBlob(file, filename):
		
		try:

			connect_str = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=appraiseteststorage;AccountKey=sxAY187MXRIf5voMhZcIGH4R48KZukd58HrEmKyp+4coax/i4CaIp4qr2ULgtWU6qwdGXzPU9Fau+ASttKoLSA==;BlobEndpoint=https://appraiseteststorage.blob.core.windows.net/;FileEndpoint=https://appraiseteststorage.file.core.windows.net/;QueueEndpoint=https://appraiseteststorage.queue.core.windows.net/;TableEndpoint=https://appraiseteststorage.table.core.windows.net/"
			# Create BlobServiceClient
			blob_service_client = BlobServiceClient.from_connection_string(connect_str)

			name = filename.strip().lower()

			# Replace invalid characters with a hyphen (-)
			name = re.sub(r'[^a-zA-Z0-9\-]', '-', name)

			# Remove consecutive hyphens
			name = re.sub(r'\-+', '-', name)

			# Remove leading/trailing hyphens
			name = name.strip('-')

			# Limit the length of the name (Azure Blob name limit is 1024 characters)
			formatted_blob_name = name = name[:1024]

			# Blob client with formatted name
			blob_client = blob_service_client.get_blob_client(container="firsttestcontainer", blob=formatted_blob_name)

			blob_client.upload_blob(file)

			return "success"

		except Exception as e:
			return str(e)
		

import frappe

@frappe.whitelist()
def get_user_info(session_user):
		if session_user == "Administrator":
			return ["Not Applicable", "Administrator", "Not Applicable", "Not Applicable"]
		
		data = frappe.db.get_list('Professors', fields = ["select_reviewer", "full_name", "department", "faculty_designation"], filters={'name': ['=', session_user]}, as_list=True, ignore_permissions = True)
		
		return data[0]


@frappe.whitelist()
def get_reviewer_names(doctype, txt, searchfield, start, page_len, filters):
		data = frappe.db.get_list('Has Role', start=start, page_length= page_len, fields=["parent"], filters = {'role': ['=', 'reviewer']}, as_list=True)
		return data

@frappe.whitelist()
def get_roles(session_user):
		roles = frappe.get_roles(session_user)
		return roles