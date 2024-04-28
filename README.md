# AutomaticIconsConverter
Automatically generates icons of different sizes
There are 2 versions: ***main.py***, run once; and ***mainServer.py*** that runs continously

## Running
1. in ***config.py***, configure input and output folders, as well as final resolutions<br>If you use server version, set also wait time(in seconds)
2. Insert your logos/icons/photos into *specified* folder
3. Run the ***main.py***
4. If you running version:<br>
   -***Normal*** - it will process everything and close itself <br>
   -***Server*** - to close the server use ***Ctrl+C***
5. Your files should be ready in *specified* folder

## Config
You can configure this app by changing values in *config.py*

***pathMade*** - path to the folder with done images <br>
***pathToMake*** - path to the folder with not done images yet <br>
***sizes*** - array with dimensions of final images
