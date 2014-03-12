==================================
lNav             id  productheader
pHeader          css #productheader h2
overview         css  #pn-overview a
designtab        css  #pn-design a
features         css  #pn-features a
whatis           css  #pn-what-is a
==================================

@ Local Nav Main | all

lNav
     width: 980px
     contains: overview, designtab, features, whatis
     
@ Local Nav Header | all

pHeader
     height: 31px
     inside: lNav 14px top, 7px left
     
@ Local Nav Links | all
     
overview
     color scheme: >0% #999999
     text is: Overview
     
designtab
     color scheme: >0% #333333
     text is: Design
     
features
     color scheme: >0% #333333
     text is: Features
     
whatis
     color scheme: >0% #333333
     text is: What is iOS