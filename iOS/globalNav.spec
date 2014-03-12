================================
body           xpath /html
gHeader        id globalheader
gNav           id globalnav
home           id gn-apple
store          id gn-store
mac            id gn-mac
ipod           id gn-ipod
iphone         id gn-iphone
ipad           id gn-ipad
itunes         id gn-itunes
support        id gn-support
gNav-item-*    css #globalnav li




gSearch        id globalsearch

================================

@ Global Nav Header | all

#checking global header width/height and location
#
#

gHeader
     height: 36px
     width: 980px
     centered horizontally inside: screen
     inside: body 18px top


@ Global Nav Bar | all
#checking global nav width/height and child elements
#
#

gNav
     height: 36px
     width: 845px
     contains: home, store, mac, ipod, iphone, ipad, itunes, support
     
     
#gNav list items height/width
#
#

gNav-item-*
     height: 36px
     width: ~ 106px
  
  
  
@ Global Search | all
#global search
#
#
     
gSearch
     width: ~ 132px
     height: ~35px
     near: gNav 0px right
     
     
     


