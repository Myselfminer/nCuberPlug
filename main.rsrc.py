{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'nCuberPlug',
          'size':(733, 301),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'load', 
    'position':(281, 204), 
    'label':'load', 
    },

{'type':'Button', 
    'name':'Update', 
    'position':(630, 200), 
    'label':'Update', 
    'visible':False, 
    },

{'type':'Button', 
    'name':'Install', 
    'position':(630, 200), 
    'label':'Install', 
    'visible':False, 
    },

{'type':'Button', 
    'name':'Uninstall', 
    'position':(630, 200), 
    'label':'Uninstall', 
    },

{'type':'StaticText', 
    'name':'DescriptionF', 
    'position':(350, 70), 
    'size':(356, 123), 
    'text':'Nothing Selected!', 
    },

{'type':'StaticText', 
    'name':'Description', 
    'position':(280, 70), 
    'text':'Description:', 
    },

{'type':'StaticText', 
    'name':'OwnerF', 
    'position':(350, 50), 
    'text':'Nothing Selected!', 
    },

{'type':'StaticText', 
    'name':'Owner', 
    'position':(280, 50), 
    'text':'Owner:', 
    },

{'type':'StaticText', 
    'name':'VersionF', 
    'position':(350, 30), 
    'text':'Nothing Selected!', 
    },

{'type':'StaticText', 
    'name':'Version', 
    'position':(280, 30), 
    'text':'Version:', 
    },

{'type':'StaticText', 
    'name':'NameF', 
    'position':(350, 10), 
    'text':'Nothing Selected!', 
    },

{'type':'StaticText', 
    'name':'Name', 
    'position':(280, 10), 
    'text':'Name:', 
    },

{'type':'StaticText', 
    'name':'nCuberPlug', 
    'position':(16, 30), 
    'text':'nCuberPlug', 
    },

{'type':'List', 
    'name':'List1', 
    'position':(100, 10), 
    'size':(172, 221), 
    'items':[], 
    },

{'type':'Button', 
    'name':'Settings', 
    'position':(10, 150), 
    'label':'Settings', 
    },

{'type':'Button', 
    'name':'Updates', 
    'position':(9, 118), 
    'label':'Updates', 
    },

{'type':'Button', 
    'name':'Installed', 
    'position':(9, 58), 
    'backgroundColor':(0, 255, 0, 255), 
    'label':'Installed', 
    },

{'type':'Button', 
    'name':'allPlugins', 
    'position':(9, 88), 
    'label':'All Plugins', 
    },

] # end components
} # end background
] # end backgrounds
} }
