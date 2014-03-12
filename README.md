Automated Layout Testing with Galen Framework

In an effort to reduce time on repeated testing, we are experimenting with automation on some of the elements that do not (or rarely) change.
This includes Global Nav, Global Footer and Product Nav. We'll also be including basic checks for promos and other additions that are easy to judge
in regard to layout.

In order to use the galen framework there is some setup involved.

Things you need: 

1. Selenium (full stack for grid testing) https://code.google.com/p/selenium/
2. GalenFramework http://galenframework.com/
3. Your favorite IDE (I use eclipse)

In addition to the list above, if you wish to run on Chrome you'll need to get the chrome driver and install this in your system PATH

You can get chromedriver from https://code.google.com/p/chromedriver/ 

1. Download and unzip the chromedriver somewhere easy to remember (like your home directory)
2. Once unzipped open terminal and cd to where you unzipped the chromedriver and run this command:
	sudo mv chromdriver /usr/bin
    enter your password for your machine when prompted

To install galen framework:

1. Download and unzip the galenframework from above to an easy to remember place (like inside your /workspace for eclipse)
2. You'll need to add the galen binary to your PATH. To do this is the same as above.
	a. Open terminal and cd to where you unzipped galen.
	b run this command: mv galen /usr/bin and enter your password when prompted.
	
	
To run a specific suite (.spec)
1. Open terminal and cd to where your project is (for me it's /Users/<username>/Documents/workspace/<name of project>    
2. Run this command: 
	galen check <name of specfile> \
	--url http://apple.com \
	--size 1024x900 \
	--htmlreport "reports"
	
	and hit return/enter
	
		a. <name of specfile> is the name of the file you are running, for example globalNav.spec
		b. url is the url to run against
		c. htmlreport is userdefined meaning you can set it to whatever and it will create that folder, 
		   leave it blank and it will generate reports in your main project folder.
		   
To run a test suite
1. Open terminal and cd to where your project is (for me it's /Users/<username>/Documents/workspace/<name of project>    
2. Run this command: 
	galen test <name of testfile> --htmlreport "reports"
	
	and hit return/enter
	
		a. <name of testfile> is the name of your test suite, for exmaple globalNav.test
		b. htmlreport is userdefined meaning you can set it to whatever and it will create that folder, 
		   leave it blank and it will generate reports in your main project folder.