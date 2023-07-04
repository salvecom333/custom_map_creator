# custom_map_creator
A custom map creator written in python where it takes excel data and converts it to a interactive map in html.

Instructions:
1.) download code
2.) First you need to make a list in excel of the places you want to put on the map, i will give a example list, go to my website to see a example list. https://www.pointperks.net/customized-map-for-realestate/ If you want to customize the code with different icons or colors for the markers modify code to your liking. 
3.) Run the python script and it will generate the map. 
4.)Then all that you have to do, is put it on your website. Keep in mind you can customize this map for anything, not just realestate.

I have used openstreetmap api because this way you don’t need to use a google api key. The only problem is that openstreetmap doesn’t have a satelite layer meaning that there is no satelite view on their maps, but there is a workaround! You can overlay a satellite layer from a different source and change the opacity so you can see the street names and the satellite view. There are free sources out in the net that provide free satellite tiles you can use. I used the arcgis tile. This took me almost an entire day to get the settings just right, alot of trial and error. If you want me to create a custom map for you, email me at pointperks@gmail.com. If you do use my code for your own personal or commercial use, just provide attributions please, this stuff takes alot of hard work. This code is under Attribution 4.0 International (CC BY 4.0) https://creativecommons.org/licenses/by/4.0/ . If you feel like donating for my efforts i will leave these links below. This code is written in python. Also i added a function so you can drive directly to where your markers are. Enjoy!

Donate a taco, the more tacos i get the more i can create free scripts:

https://ko-fi.com/salvadorcarrillo_c

https://www.buymeacoffee.com/pointperksH

                                  .--===-:.                                           
                               .+*########**+:                                        
                              =*#############*=                                       
                             +################*.                                      
                            .*################*=                                      
                             .+*++++****######*+.                                     
                              .===-==++****##**+:                                     
                               -===+********#**+.                                     
                               .+*=*+++=++******:                                     
                                :--+++==+********+.                                   
                                 -=+**++****##*###*=-:.                               
                                  :=+****##########*****+=-.                          
                                    =++*#####**####*********+-.                       
                                 .=+***#******#####************=-                     
                               :+####*###+++*####**#*************+.                   
                            .-+*######*##*=*####**#******###******+.                  
                           -*#**##**#***##*###***#***##*###********=                  
                         .-**#####******####****#****#####*#*******+.                 
                      -+**########****#*##**=**##***######***#*****+.                 
                    -+**##########***####***:+**#*#######***##*****+.                 
                   =****##########***###*******#########***##******+.                 
                 :=**#########%###***###********########**##*******+.                 
                :=++*####%%%%%%###***###*******########***##**##***=                  
                -++*###%#%%%%%%##*######*******########**######*#**-                  
                -++*######+=----*#########****#########****#####***.                  
                -++*##*=:       -####*#*******##################***.                  
                :=+**:          :*###*********##########******##***.                  
              .-=++*=           .*#####*#****###########*+***###***:                  
             :-==+**-            +#####****############+==+**###***:                  
            .--=++**.            :*###################+==+***###*#*:                  
            .--==+#+              +##################+=++****####**-                  
             :=-+*+.              -#################+=++**#*#####**-                  
              .-::.               .*###############+++***########**+                  
                -.                 +#############*++***##########**+.                 
                :.                 =############++***##########*#***:                 
  ......::-:....----::.:--::...    +##########*=++**##########*###**-                 
 .::.:-:::::----===+******++++=+-:=++*+***##*+++***###############**=                 
  .. ::....:....:-=+**=-+*++++==+++=**-=**===++***################**+                 
 :=+=-::.:........--+**==**=++++++*=+**++====***##################**+                 
 -==++*+=--.:.: :.:-=+*+=+*==+++==*==+*+=++=+*+*#*###############***=                 
   .:-=+++++==-:-::=-+*==+*==+*==+*==+++*#=+*=+****##############***-                 
       .:-==+++++++***#*###*########*****+=*+=*+**-. .-=+*#####***=.                  
          ...::::::::::::.........          .....         .:-=+***.                   
                                                                ..                    
