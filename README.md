<strong><p style="font-size:24px;">Automated Layout Testing with Galen Framework</p></strong>

In an effort to reduce time on repeated testing, we are experimenting with automation on some of the elements that do not (or rarely) change.
This includes Global Nav, Global Footer and Product Nav. We'll also be including basic checks for promos and other additions that are easy to judge
in regard to layout.

<strong>Linux/Unix based install</strong>

Open terminal create a /test folder in your home drive and cd there
	mkdir test
	cd test

You should be in /Users/[username]/test

Run command:

    git init
    git clone https://interactive-git.apple.com/interactive-qa-fe/AppleLayoutTesting
    cd AppleLayoutTesting
    git tag (this will show you the latest version)
    git checkout -b (whatever the latest tag is)
    	*note: if you already have a clone, run git fetch --tags to get the latest tags
    
You should now have the latest version of AppleLayoutTesting
 
To install galen and chromedriver open terminal and cd to AppleLayoutTesting

run command:

	sudo ./install.sh
	
This will add the files to their correct location for you.

To start and register the selenium grid run start.sh and register.sh in separate windows. You should be able to do this by
simply typing start.sh and register.sh respectively.

As a shortcut I've added scripts to run the test for you.
To run a particular test (iOS.test for example) 

1. Open terminal and cd to it's location (~/test/AppleLayoutTesting/iOS)
2. Run command:
		./iOS.sh

or for General Nav
		./gNav.sh
		
		
This will run the test automatically and generate the reports in the "reports" folder within that project folder (/iOS/reports")





<strong><p style=font-size: 20px;">If you would like to install the necessary files yourself the steps to follow are listed below.</p></strong>

Things you need: 

1. Selenium (full stack for grid testing) https://code.google.com/p/selenium/
2. GalenFramework http://galenframework.com/
3. Your favorite IDE (I use eclipse)

In addition to the list above, if you wish to run on Chrome you'll need to get the chrome driver and install this in your system PATH

You can get chromedriver from https://code.google.com/p/chromedriver/ 

1. Download and unzip the chromedriver somewhere easy to remember (like your home directory)
2. Once unzipped open terminal and cd to where you unzipped the chromedriver and run this command:

		sudo mv chromedriver /usr/bin
    	enter your password for your machine when prompted

To install galen framework:

1. Download and unzip the galenframework from above to an easy to remember place (like inside your /workspace for eclipse)
2. You'll need to add the galen binary to your PATH. To do this you can run the following command in terminal

		echo "export PATH=$PATH:/location of galen folder" >> ~/.profile
		
		e.g. echo "export PATH=$PATH:~/test/AppleLayoutTesting/includes/galen-bin-0.9.0/" >> ~/.profile

		
	
<strong><p style="font-size:20px;">Running Galen</p></strong>

To run a specific suite (.spec)

1. Open terminal and cd to where your project is (for me it's /Users/[username]/Documents/workspace/[name of project]    
2. Run this command: 

		galen check <name of specfile> \
		--url http://apple.com \
		--size 1024x900 \
		--htmlreport "reports"

and hit return/enter

a. [name of specfile] is the name of the file you are running, for example globalNav.spec

b. url is the url to run against

c. htmlreport is userdefined meaning you can set it to whatever and it will create that folder, 
   leave it blank and it will generate reports in your main project folder.
		   
To run a test suite

1. Open terminal and cd to where your project is (for me it's /Users/[username]/Documents/workspace/[name of project]    
2. Run this command: 

		galen test <name of testfile> --htmlreport "reports"
	
and hit return/enter

a. [name of testfile] is the name of your test suite, for example globalNav.test

b. Here htmlreport must be defined (I use "reports")
		   

Running in Selenium grid

To support more browsers and coverage, you can run Galen in Selenium Grid. If you have already downloaded and installed the full selenium stack
just open terminal and cd to where this is unzipped.

1. Start the hub by running command: 

   		java -jar selenium-server-standalone-2.40.0.jar -role hub 
2. Register the node for use by opening another terminal in the same folder and run command: 

   		java -jar selenium-server-standalone-2.40.0.jar -role node -hub http://localhost:4444/grid/register
   
Now you can use Selenium grid for testing. *Note: you may need to change the selenium-server-standalone-2.40.0.jar version (2.40.0 is current 
as of 3/11/2013)






CHANGELOG

Current Features: 

	1. Tests Global Nav, Global Footer and Product Nav on all Flagship pages
	2. iOS test for /ios page and promo call out (where applicable) including Global Nav, Footer and Product Nav
	3. Can test against any ic branch on Firefox and Chrome by passing in your credentials
	4. Can test against any size browser, protocol (http, https) and url by passing in their values in the .test file for the project
	5. Runs on Selenium Grid for cross browser support (only Chrome and Firefox currently supported for ic branches)
	6. Shell scripts for starting and registering the Selenium grid
	7. Shell scripts for starting the tests.
	8. Element approximation range, full-page screenshot set (changes can be made in config file for each project. i.e. iOS, General etc)
	
	3/13/14
	Added install.sh to install the necessary files for you (only mac/linux supported at the moment)



Upcoming:

	1. full ic branch support for Safari and IE
	2. Additional pages to test.
	3. Installer file for Windows
	4. Bug fixes
