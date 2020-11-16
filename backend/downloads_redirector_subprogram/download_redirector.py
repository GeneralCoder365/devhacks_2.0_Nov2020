from bs4 import BeautifulSoup as bsoup
import requests
import wget 
import urllib
import os

url = 'https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/'
root_path = ''
setpath = '' 
rel_path = 'backend/downloads_redirector_subprogram/redirector_data.dat'
stored = True
new_names = []
file_list = []
d_file_list = []
new_name = " "      

def get_path(url):
    with open(rel_path, "r+") as dat_file:
        dat_list = dat_file.readlines()
        i = 0
        while i < len(dat_list):
            var = dat_list[i].split(",")
            if var[0] in url:
                setpath = var[1]
                break
            else:
                i += 1
        dat_file.close()               
    return setpath   

def get_files(url, setpath):
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
            wget.download(name, setpath)
            print("downloading: " + name + " to: " + setpath)
            d_file_list.append(name)
        except:
            pass
    list_compare(d_file_list)

def add_root(root_link, root_path):
    with open(rel_path, "a") as dat_file:
        # adds a formatted root link and path
        dat_file.write(root_link + "," + root_path + "\n")  
    dat_file.close()

def del_root(root_link):
    # opens for read and write
    with open(rel_path, "r+") as dat_file:
        # stores each line as a string in a dat_list
        dat_list = dat_file.readlines()
        for i in range(len(dat_list) -1):
            var = dat_list[i]
            # splits by comma so index 0 is the link and index 1
            # is the path
            comp = var.split(",")
            # deletes an index if the same as a provided link
            if comp[0] in root_link or comp[0] == root_link:
                del dat_list[i]
    dat_file.close()
        
    with open(rel_path, "w+") as dat_file:
        # case work in case user only had one root and deletes it
        if len(dat_list) < 1:
            dat_file.write(" ")
        else:
            # rewrites the .dat file
            for i in range(len(dat_list) -1):
                dat_file.write(dat_list[i]) 
    dat_file.close()   

def list_compare(d_file_list):
    for root, directories, files in os.walk(setpath, True):
        for x in files:
            # gives list of files in path
            file_list.append(x)

    for y in range(len(d_file_list)-1):
        # edits links so that file name corresponds with downloadable link
        temp = d_file_list[y].split("/")
        temp2 = temp[len(temp)-1]
        d_file_list[y] = temp2

    for z in range(len(file_list)-1):
        # deletes file if it has the same name as the one just downloaded
        if file_list[z] in d_file_list:
            # puts path and file together so it can be removed
            d_file = os.path.join(setpath, file_list[z])
            os.remove(d_file)
        else:
            print("skip")


get_files(url, setpath)
