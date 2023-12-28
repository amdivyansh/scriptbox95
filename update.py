#!/usr/bin/env python3
import requests
import zipfile
import io
import re
import os
import shutil
import time
def download_latest_release_repository():
    url = f"https://api.github.com/repos/amdivyansh/scriptbox95_source_data/releases/latest"
    #headers = {"Authorization": f"token {access_token}"}
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        release_info = response.json()
        download_url = release_info['zipball_url']
        
        print(f"Downloading from: {download_url}")
        
        response = requests.get(download_url)
        if os.path.exists('main'):
                        shutil.rmtree('main')
        content_disposition = response.headers.get('Content-type')
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall()
        # Get the extracted folder name
        extracted_folder_name = z.namelist()[0]
        print(extracted_folder_name)
        # Rename the extracted folder to the new name
        os.rename(extracted_folder_name, 'main')
    else:
        print(f"Failed to download repository. Status code: {response.status_code}")
