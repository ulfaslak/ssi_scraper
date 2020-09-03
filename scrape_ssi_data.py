import os, re, shutil
import requests as rq
import zipfile, urllib


# GLOBALS
# -------
IN_DIR = 'data/'
OUT_DIR = 'data/'
URL = "https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning/arkiv-med-overvaagningsdata-for-covid19"


# Existing files names
# --------------------
existing_files = [f for f in os.listdir(IN_DIR) if f[:4] == "Data"]


# Scrape new files
# ----------------

# Get urls
data_urls = re.findall(
    r"https://files.ssi.dk/Data-\w+-\w+-\d{8}-\w{4}",
    rq.get(URL).text
)

# Remove urls for files already downloaded
data_urls = [
    url for url in data_urls
    if url[21:] not in existing_files
]

# Download data
bad_urls = []
for url in data_urls:

    # Folder path and create folder
    out_dir = OUT_DIR + url[21:]
    os.mkdir(out_dir)
    
    # Download
    try:
        filehandle, _ = urllib.request.urlretrieve(url)
    except urllib.error.HTTPError:
        bad_urls.append(url)
        continue

    # Unzip
    zip_file_object = zipfile.ZipFile(filehandle, 'r')

    # Get content filenames into a list
    content_filenames = zip_file_object.namelist()

    # Extract each file
    for filename in content_filenames:
        content = zip_file_object.open(filename).read()
        with open(out_dir + "/" + filename, 'wb') as fp:
            fp.write(content)


# Conclusive message
# ------------------
n_new_files = len(data_urls) - len(bad_urls)
if n_new_files == 0:
    print("No new files")
if n_new_files > 0:
    print(f"Successfully extracted {n_new_files} new file(s):")
    for url in data_urls:
        print(f"    {url}")

if len(bad_urls) > 0:
    print(f"Could not extract {len(bad_urls)} file(s):")
    for url in bad_urls:
        print(f"    {url}")