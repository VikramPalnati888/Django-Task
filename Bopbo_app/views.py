from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from urllib.request import urlopen
from django.core.files.storage import FileSystemStorage



def sheet(request):
	if request.method == "POST":
		# use creds to create a client to interact with the Google Drive API
		scope = ['https://spreadsheets.google.com/feeds',
				 'https://www.googleapis.com/auth/drive',
				 'https://www.googleapis.com/auth/drive.file',
				 'https://www.googleapis.com/auth/drive.appdata',
				 'https://www.googleapis.com/auth/drive.apps.readonly']
		creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
		client = gspread.authorize(creds)

		service = build('drive', 'v3', credentials=creds)
		# Find a workbook by name and open the first sheet
		# Make sure you use the right name here.
		sheet = client.open("task-drive@task-292517.iam.gserviceaccount.com").sheet1


		Name = request.POST['name']
		Email = request.POST['email']
		Mobile_No = request.POST['mobileno']
		Messages = request.POST['message']
		Attachment_File = request.FILES['filename']

		# fs = FileSystemStorage(location='static\\media\\files\\')
		# print(fs,'Pppppp')
		# filename = fs.save(Attachment_File.name, Attachment_File)
		# file_url = fs.path(filename)
		# print(type(file_url),"lllllll")

		# file_name = file_url.split('\\')
		# print(file_name,"filename")

		#here form data storing like name, email, mobile_no, message
		row = [Name, Email, Mobile_No,	Messages]
		index = 2
		sheet.insert_row(row, index)

		# folder_id = '1YHJvfup29RIQ5lbttGu8BjBwQBOoVCew'
		# mime_type = ['image/jpeg','image/png','application/vnd.ms-excel','application/pdf','application/msword']

		file_metadata = {
				'name':file_url,
				'parents':[folder_id],
		}

		# media =  MediaFileUpload(file_url,mimetype=mime_type)
		# file = service.files().create(body=file_metadata,
		# 						media_body=media,
		# 						fields='id').execute()


	return render(request, 'contactus.html', messages.success(request, 'Thank you for submission form'))