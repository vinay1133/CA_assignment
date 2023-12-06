import frappe
import re
import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def validateAY(academic_yr_str):
	pattern_for_ay = re.compile(r'^\d{4}-\d{4}$')
	if re.match(pattern_for_ay, academic_yr_str):
		years = academic_yr_str.split("-")
		if int(years[1]) != int(years[0]) + 1:
				frappe.throw("Academic year entered incorrectly")
	else:
		frappe.throw("Academic year must be of the form like 2022-2023")

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
		
