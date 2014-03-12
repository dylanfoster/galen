================================
body            xpath /html
footer          id    globalfooter
breadbag        id    breadory
breadcrumbs     id    breadcrumbs
apple           css   .home
bread-slice-*   css   #breadcrumbs li
links-*         css   #breadcrumbs li a
dNav            id    directorynav
================================


@ Global Footer Main | all

footer
     width: 980px
     centered horizontally inside: screen

@ Global Footer Container | all

breadbag
     width: 980px
     centered horizontally inside: footer
 
@ Breadcrumbs | all
    
breadcrumbs
     width: 978px
     height: 33px
     
apple
     width: 44px
     height: 33px
     
bread-slice-*
     height: 33px
     aligned horizontally all: apple
     
[ 1 - ${count("bread-slice-*") - 1} ]
bread-slice-@
     near: bread-slice-@{+1} 0px left
     
#bread-slice-2
    #text is: iOS
     

@ Directory Nav | all

dNav
     width: 978px
     below: breadcrumbs 0px
     