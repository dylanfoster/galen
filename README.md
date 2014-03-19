<strong style="font-size: 24px;" >Galen Install and Template files</strong>

<p>Building off of the galen framework, these will help with the current install process by adding the necessary files to your PATH. </p>

<p>In addition, template.sh will help you get started quickly by creating a project folder, a .test file, a .spec file and shell script to run the test.
The template.sh will also zip up all of the report files (report.html, screenshots, css and js) with a timestamp so that you can keep track of 
testing history. This is an interactive shell script, once you run it you can name your project, test and spec files as you wish.</p>

<p>This repo is completely self contained and includes Galen, Chromedriver, Selenium (including standalone server for Grid). You can clone this
and run ./install.sh to get you started. After that template.sh will create the template for you, start.sh will start the grid and register.sh will
register the node for you.
</p>

<p>Many thanks to <strong>Ivan Shubin</strong> for his hard work on Galen Framework. 