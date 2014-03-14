#!/bin/bash
galen test GlobalNav.test --htmlreport "reports"
cd reports
now=$(date +'%m%d%y_%H:%M')
zip report_$now.zip *.*
