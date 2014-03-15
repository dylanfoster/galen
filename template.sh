#!/bin/bash
read -p "Name your project: " project
mkdir $project
cd $project
read -p "Name your test suite: " test
read -p "Name your spec file: " spec
echo "@@ set

   #creds       username:password@
   branch      www.
   domain      \${branch}apple.com
   pro         http://\${creds}
   base_url    \${pro}\${domain}/
   size        1024x900
   grid        selenium grid http://127.0.0.1:5555/wd/hub
   
@@ table browsers
 | browser   | version  |
 | chrome    |   33     |
 | firefox   |   27     |
 | safari    |    7     |

@@ parameterized using browsers
<give this an appropriate test title> \${browser} \${version} \${size} |
     \${grid} --page \${base_url} --browser \${browser} --version \${version} --platform \"MAC\"

repeat above as needed" > $test.test

echo "
###############################################
## test suite name                           ##
## Author: 			                         ##
## Date: 			                         ## 
###############################################


#desc
#
#
#

===============================================
object definitions
===============================================

spec definitions" > $spec.spec

echo "#!/bin/bash
galen test <testfile>.test --htmlreport \"reports\"
cd reports
shopt -s extglob
now=\$(date +'%m%d%y_%H:%M')
zip report_\$now.zip *.* -x *.zip
rm !(*.zip)" > $test.sh
