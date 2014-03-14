#!/bin/bash
galen test iOS.test --htmlreport "reports"
cd reports
now=$(date +'%m%d%y_%H:%M')
zip report_$now.zip *.*
