==================================
body              xpath /html
hero              id    hero
promo             css   .update
design            css   .row.design
==================================

@all

@@ if
promo
     visible
@@ do
promo
     centered horizontally inside: screen
     near: hero -12px bottom
     near: design ~ 71px top
     
@@ otherwise
hero
     above: design 0 to 10px
@@ end