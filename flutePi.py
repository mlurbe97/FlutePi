#!/usr/bin/python3
# -*- coding: utf-8 -*-

#	Learning to play the Piano with a Python Bot  Copyright (C) 2020  Manel Lurbe Sempere
#	This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#	This is free software, and you are welcome to redistribute it
#	under certain conditions; type `show c' for details.

########################################
#			Imports					   #
########################################
import time
import sys
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
#end Imports.

########################################
#		Initialize I2C bus             #
########################################

# Create the servo connection.
kit = ServoKit(channels=16)
#end Initialize I2C bus.

########################################
#		Global variables               #
########################################

# Servo angles.
on = 90
off = 0

# Flute variables
board_pin = 4
on = True
off = False
GPIO.setmode(GPIO.BCM)
GPIO.setup(board_pin, GPIO.OUT)

# Song to be played.
song = []
#end Global variables.

########################################
#		Music notes available          #
########################################

# Channel of each servo motor.
mt0 = kit.servo[0]
mt1 = kit.servo[1]
mt2 = kit.servo[2]
mt3 = kit.servo[3]
mt4 = kit.servo[4]
mt5 = kit.servo[5]
mt6 = kit.servo[6]
mt7 = kit.servo[7]
mt8 = kit.servo[8]
mt9 = kit.servo[9]
mt10 = kit.servo[10]
mt11 = kit.servo[11]
mt12 = kit.servo[12]
mt13 = kit.servo[13]
mt14 = kit.servo[14]
mt15 = kit.servo[15]

# Servo motors available.
motor_list = [mt0,mt1,mt2,mt3,mt4,mt5,mt6,mt7,mt8,mt9,mt10,mt11,mt12,mt13,mt14,mt15]

# Each note with each channel.
flute_map = {
	"f1": mt0,
	"f2": mt1,
	"f3": mt2,
	"f4": mt3,
	"f5": mt4,
	"f6": mt5,
	"f7": mt6,
	"f8": mt7,
	"f9": mt8
}

# Each note with each channel.
music_notes = {# list of flute holes for each note.
	"do": {"f1","f2","f3","f4","f5","f6","f7","f8","f9"},
	"do#": "",
	"reb": "",
	"re": {"f2","f3","f4","f5","f6","f7","f8","f9"},
	"re#": "",
	"mib": "",
	"mi": {"f3","f4","f5","f6","f7","f8","f9"},
	"fa": {"f4","f5","f6","f7","f8","f9"},
	"fa#": "",
	"solb": "",
	"sol": {"f5","f6","f7","f8","f9"},
	"sol#": "",
	"lab": "",
	"la": {"f6","f7","f8","f9"},
	"la#": "",
	"sib": "",
	"si": {"f7","f8","f9"},
	"do2": {"f8","f9"},
	"do2#": "",
	"re2b": "",
	"re2": ""
}
#end Music notes available.

########################################
#		Note tempo defines             #
########################################

# Values of each type of note.
dobleredonda = 3.2
redonda = 1.6
blancaplus = 1.2
blancasemi = 1
blanca = 0.8
negraplus = 0.6
negrasemi = 0.5
negra = 0.4
corchea = 0.2
semicorchea = 0.1
ssemicorchea = 0.05
sssemicorchea = 0.025

# Each tempo with each value.
tempo_notes = {
	"dr":dobleredonda,
	"r":redonda,
	"b+":blancaplus,
	"b-":blancasemi,
	"b":blanca,
	"n+":negraplus,
	"n-":negrasemi,
	"n":negra,
	"c":corchea,
	"sc":semicorchea,
	"ssc":ssemicorchea,
	"sssc":sssemicorchea
}
#end Note tempo defines.

########################################
#			usage function             #
########################################
def usage(program_name):
	print("Usage:\n\tpython3 "+program_name+" music_sheets/music_sheet.txt\nor:\n\t./"+program_name+" music_sheets/music_sheet.txt")
#end usage function.

########################################
#		play_note function             #
########################################
def play_note(the_notes):
	for note in the_notes:
		for position in note[0]:
			flute_map[position].angle = on
		time.sleep(0.01) # Wait for servo motor change.
	GPIO.output(board_pin, on)
	time.sleep((the_notes[0])[1])
	GPIO.output(board_pin, off)
	for note in the_notes:
		for position in note[0]:
			flute_map[position].angle = on
		time.sleep(0.01) # Wait for servo motor change.
#end play_note function.

########################################
#			reset function             #
########################################
def reset():
	for motor in motor_list:
		motor.angle = off
#end reset function.

########################################
#		get_music_sheets function      #
########################################
def get_music_sheet(music_sheet):
	try:
		song_file = open(music_sheet,"r")
	except:
		print("No music_sheet called music_sheets/"+str(music_sheet)+" found.")
		sys.exit(1)
	song_content = song_file.read().split("\n")
	for notes in song_content:
		try:
			tuple_notes = notes.split("\t")
			list_notes = []
			for note in tuple_notes:
				values = note.split(",")
				tupla = (music_notes[values[0]],tempo_notes[values[1]])
				list_notes.append(tupla)
			song.append(list_notes)
		except:
			continue
#end get_music_sheets function.

########################################
#	   	mover_mt_angle  function       #
########################################
def mover_mt_angle(motor,angle):
	mt = motor_list[motor]
	mt.angle = angle
	time.sleep(0.2)
#end mover_mt_angle function.

#########################################
#    Read arguments and get music_sheets  #
#########################################

# Get program name.
program_name = sys.argv[0].replace("./","")

# Get number of arguments.
num_args = len(sys.argv)

# Exit program if no music_sheet are selected.
if num_args <= 1:
	print("No music_sheet selected")
	usage(program_name)
	sys.exit(1)
 
# Get music_sheet name.
music_sheet = sys.argv[1]

# If music_sheet name is reset, reset motors and end program.
if music_sheet == "reset":
	reset()
	print("Reset notes")
	sys.exit(1)

# If music_sheet name is test, test motors and end program.
if music_sheet == "test":
	try:
		mover_mt_angle(int(sys.argv[2]),int(sys.argv[3]))
		print("movido")
	except:
		print("Incorrect values for test, motor_index and angle.")
	sys.exit(1)

# Get the music_sheet.
get_music_sheet(music_sheet)

#########################################
#		Play Song non-Threaded			#
#########################################

print('Playing piano, press Ctrl-C to quit...')
try:
	while True:
		reset()
		for note in song:
			time.sleep(0.06) # Modify to your servo motor delay in position changing.
			play_note(note)
		print("The song has ended, playing again...")
except KeyboardInterrupt:
	reset()
	print("Turning off the piano.")
	sys.exit(1)
#end Play Song non-Threaded.

#end Program.