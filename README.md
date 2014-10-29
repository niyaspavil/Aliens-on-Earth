Aliens-on-Earth
===============
This is a console based python application, in which Aliens from any different planet can register their details and also can print it in either text or pdf format.

Design
---------
This application has three levels,

     1.Ui
     2.Admin
     3.Plugins

The Ui level provide a console based user interface. which collect the Alien Details

Admin level create an alien object with details. It collects all the available fomats(plugins) and creates user desired output format.

Plugin level contains all the available plugins. Developers can load and remove plugin files.


Installation 
------------  

python setup.py install

Type "register" to run the program.