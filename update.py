import requests
import zipfile
import io
import os
import re
def download_latest_release_repository(owner, repo, access_token, new_folder_name):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    headers = {"Authorization": f"token {access_token}"}
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        release_info = response.json()
        download_url = release_info['zipball_url']
        
        print(f"Downloading from: {download_url}")
        
        response = requests.get(download_url, headers=headers)
        content_disposition = response.headers.get('Content-type')
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall()
        # Get the extracted folder name
        extracted_folder_name = z.namelist()[0]
        print(extracted_folder_name)
        # Rename the extracted folder to the new name
        os.rename(extracted_folder_name, new_folder_name)
        
        print(f"Repository downloaded and extracted successfully")
    else:
        print(f"Failed to download repository. Status code: {response.status_code}")

# Usage:
# Make sure to replace 'owner', 'repo', 'access_token', and 'new_folder_name' with actual values.
download_latest_release_repository('amdivyansh', 'scriptbox95', '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', 'main2')