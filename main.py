#!/usr/bin/python

"""
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/04/14 02:38:47 $"
"""

import nID
import plugin
import os

repository_nid="all_url:https://www.dropbox.com/s/tvyxx5iidodidz2/nid_sample_list.txt?dl=1@name:Sample Repo Name@owner:myselfminer"

from PythonCard import model

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass
    def on_allPlugins_mouseClick(self, event):
        allp=plugin.listall(repository_nid)# get a list of all plugins aviable in the repo
        self.components.List1.items=allp#update List1 with the list
    def on_load_mouseClick(self,event):
        a=open("nidlist.tmp","r")# open saved nids(presaved result of plugin.listall())
        b=a.readlines()
        a=plugin.get_nid_by_name(b,self.components.List1.stringSelection) # get nid by using the selection in List1
        # ---Set Component values---
        self.components.NameF.text=nID.parse(a, "name")
        self.components.VersionF.text=nID.parse(a, "version")
        self.components.OwnerF.text=nID.parse(a, "Author")
        self.components.DescriptionF.text=nID.parse(a, "Description")
    def on_Installed_mouseClick(self, event):
        nids=plugin.get_local_nids()
        final=[]
        for i in nids:#create a nidlist of installed plugins
            now=nID.parse(i, "name")
            final.append(now)
        self.components.List1.items=final
        

if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
