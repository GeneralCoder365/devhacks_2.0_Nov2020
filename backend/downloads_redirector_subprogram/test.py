from bs4 import BeautifulSoup as bsoup
import requests
import wget 
import os

rel_path = 'backend/downloads_redirector_subprogram/redirector_data.dat'
url = 'https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/'
urls = []
names = []
d_file_list = []

def get_path(url):
    with open(rel_path, "r+") as dat_file:
        dat_list = dat_file.readlines()
        i = 0
        while i < len(dat_list):
            var = dat_list[i].split(",")
            if var[0] in url:
                path = var[1]
                break
            else:
                i += 1
                       
        return path
        

def get_files(url):
    path = get_path(url)
    print("path: " + path)
    print("URL: " + url)
    names = []
    urls = []
    # get request for the url so that it can be turned into a "soup"
    req = requests.get(url)
    # the html gotten from before is parsed
    soup = bsoup(req.text, "html.parser")

    # finds tags that start with
    for i, link in enumerate(soup.findAll('a')):
        # forms a full link
        want_url = url + link.get('href')
        urls.append(want_url)
        # gives wanted download link
        names.append(soup.select('a')[i].attrs['href'])

    # zips both lists together so going through each becomes easy
    n_url = zip(names, urls)

    for name, link in n_url:
        # need try and except because will throw error if try and download
        # a non downloadable link
        try:
            # uses wget to download a link
            wget.download(name, path)
            print("downloading: " + name + " to: " + path)
        except:
            pass

get_files(url)