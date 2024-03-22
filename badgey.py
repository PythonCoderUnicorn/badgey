#!/bin/bash


from termcolor import colored
import random

print(colored("--"*30, "yellow") )

logo="""

              @
            &&&#$       .-----------------.
           &&&&&@@      | Hi !            |
         /@@@@@@@@##    | Can I teach you |
        @@( .)@(. )@#  -| a lesson ?      |
       #@@@@@@@@@@@@##  |_________________|
      @@@@@@[    ]@@@@#     Badgey v 0.0.1
     #@@@@@@@@@@@@@@@@#
    %@@@@@@@@@@@@@@@@@@#
    %@@@@@@@@@@@@@@@@@@@|
    %@@@@@@/#######\@#@@|
    %@@@@@/         \@@@|
    @@@@/            \$/
    @@/ 
"""

# print(logo)
print(colored( logo, "yellow") )

# ------------------------- "Can I teach you a lesson?"
# 
# https://www.geeksforgeeks.org/play-sound-in-python/
# pip3 install playsound
import playsound

filename = "./startrek-badgey.wav"  # play WAV file
playsound.playsound(filename)




print(colored("--"*30, "yellow") )

def lessons():
  print(colored( "- -"*20, "green") )

  plasma ="""
           When working on the warp core unit, be sure
           to remove the deprecated horizontal cores in the
           secondary hull. Horizontal cores have various
           technology inefficiencies.

           def warp_core( unit_type ):
               if unit_type == "horizontal":
                  print(" [*] WARNING [*] ")
                  print(" Using horizontal cores is not advised ")
                  print(" Horizontal cores have been deprecated. ")
                  print(" It is advised you reach the nearest Starbase for repairs. ")
                  print(" -- Starfleet Engineering --")
           """

  conduits="""
            When cleaning the plasma conduit (power conduit) 
            which is part of the warp drive and power grids, 
            be sure to have any clutter removed from the area. 

            Plasma conduit uses copper (Cu+) tubing, which Bolaris IX 
            has a steady supply and often gives Starfleet a discount. 

            When installing copper tubing, be sure to reinforce 
            it with nanopolymer adhesive.

            Clean tubing surface first then apply adhesive evenly.
           """

  impulse="""
          Impulse reactors use a deflector pulse which is fed into
          a deflector array, which has the potential output to
          disrupt a subspace links. 

          Caution when linking the deflector pulse to the array, 
          as EPS conduits on the station or ship can rapture.

          Follow the Starfleet Engineering standards and 
          procedures manual Section 67.2.1. 
          """

  inducers="""
          [*] ------------ CAUTION -------------- [*] 
          Phase inducers 

          Working on phase inducers is dangerous work.
          Serious injuries may result from improper 
          installation or repairs, such as radiation
          poisoning. 

          Before working on phase inducers it is advised
          you unlink the transporters, communications and
          warp drive systems. This allows for safe repairs.

          """

  facts = [ 
          # plasma,
          # conduits,
          #  impulse,
          inducers

          ]
  x=random.randint( 0, len(facts)-1)
  print(f" Today's lesson: \n{facts[x]}")
  print(colored( "- -"*20, "green") )



lesson = str(input("Learn a lesson? (y/n): "))

if lesson.lower() =="y":
  # call the lessons function
  lessons()
else:
  print(":::: okay \U0001f603 :::::\n")

# lessons()

print(colored("\n-- Program Exited --\n", "cyan") )
