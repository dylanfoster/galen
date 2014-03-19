#!/bin/bash
echo "Adding Galen and Chromedriver to your PATH
..
..
..
.."

echo "export PATH=$PATH:~/test/galen/includes/selenium-2.40.0/:~/test/galen/includes/galen-bin-0.9.0/:~/test/galen" >> ~/.profile
mv ~/test/galen/includes/chromedriver /usr/bin/
. ~/.profile

echo "...Done"
echo "Your PATH is now"  echo "$PATH"
echo "
Reload your profile by typing:  source ~/.profile
...
...
...Then you are ready to start your grid. Just run start.sh then open another termianl and run register.sh"
