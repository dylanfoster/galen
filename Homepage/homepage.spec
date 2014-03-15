###############################################
## Homepage (apple.com/)tiles 1024 spec file ##
## Author: Dylan Foster                      ##
## Date: 3/14/14                             ## 
###############################################

#min width of promo tile wrapper is 1024 so we'll start there
#promo tiles should be 25% of this no matter what size
#promo wrapper is 2px down from hero (might change?)
#possible breakpoints
# 1024, 1152, 1280, 1600 each in individual spec files.

====================================
hero             css .hero
tileWrap         css .promos>ul
tiles-item-*     css .promos>ul li
====================================



@ Homepage Hero & Tiles 1024x768 | @desktop small

hero
     width: 1440px
     
tileWrap
     below: hero 2px
     width: 1024px
     height: 200px
     
tiles-item-*
     width: ~25% of tileWrap/width
