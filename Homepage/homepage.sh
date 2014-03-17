#!/bin/bash
galen test homepage.test --htmlreport "reports"
cd reports
shopt -s extglob
now=$(date +'%m%d%y_%H:%M')
zip report_$now.zip *.* -x *.zip
rm !(*.zip)
