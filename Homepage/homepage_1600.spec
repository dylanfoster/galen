###############################################
## Homepage (apple.com/)tiles 1152 spec file ##
## Author: Dylan Foster                      ##
## Date: 3/17/14                             ## 
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



@ Homepage Hero & Tiles 1600x1200 | @desktop x-large

hero
     width: 1440px
     
tileWrap
     below: hero 2px
     width: 1440px
     height: 200px
     
tiles-item-*
     width: ~25% of tileWrap/width
     height: 100% of tileWrap/height