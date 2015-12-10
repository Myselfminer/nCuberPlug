import urllib2,zipfile
import nID
import os
import download as get
import sys
def get_fields_from_repo(repository_nid, field):
    list_of_all=[]
    a=nID.parse(repository_nid,"all_url")
    text=download(a)
    try:
        split=text.split("\n")#split the downloaded data
    except:
        print("Could not parse downloaded data!")
        sys.exit()#exit if the downloaded data could not be parsed(may happen if the download module couldn't finish the download)
    b=open("nidlist.tmp","w")#presave the downloaded data(the GUI uses this file in on_load)
    for i in split:
        b.write(i+"\n")
        parsed=nID.parse(i,field)
        list_of_all.append(parsed)#pick the fields from the nids
    print("[GetFieldsFromRepo] nidlist saved!")# notify console for filesaving
    b.close()
    return list_of_all
def get_installed_version_by_name(name):
    try:
        a=open("prop/"+name+".prop","r")#uses prop files
        b=a.readlines()
        return b[0]
    except:
        return False
def download(url):
    return get.download(url)#redirect to new download function(will be removed soon)
def install(nid):
    parsed=nID.parse(nid,"url")#get url from nid argument
    version=nID.parse(nid,"version")
    a=download(parsed)# download url parsed above
    zipped=open("temp/download.zip","w")# write downloaded data to a file
    zipped.write(a)
    zipped.close()
    unzip=zipfile.ZipFile("temp/download.zip","r")# start unzip data usin zipfile
    path=nID.parse(nid,"name")
    unzip.extractall("Plugins/"+path)# end
    a=open("prop/"+path+".prop","w")#write prop
    a.write(version)
    return true
def listall(repository_nid):
    data=get_fields_from_repo(repository_nid, "name")# download list of names from the repo
    return data
def get_updates(repository_nid):
    updates=[]
    data=get_fields_from_repo(repository_nid, "version")
    datan=get_fields_from_repo(repository_nid, "name")
    for i in datan:
        lokal=get_installed_version_by_name(i)
        if lokal!=False:
            updates.append(i)#todo: compare the versions!
    return updates
def uninstall(nid):
    name=nID.parse(nid,"name")
    os.remove("prop/"+name+".prop")#delete prop
    os.removedirs("Plugins/"+name)# and plugin folder
def get_nid_by_name(nids_list, name):
    #WARNING! This function may be removed in a future release
    for i in nids_list:
        a=nID.parse(i, "name")
        if a == name:
            return i
def get_local_nids():
    nids=[]
    a=os.listdir("/prop")#read the props
    for i in a:
        a=open("i","r")
        b=a.readlines()
        nids.append(b[0])
    return nids
    
