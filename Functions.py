#1
def convert_to_seconds(hours, minutes, seconds):
	hours_to_minutes = hours * 60 * 60
	minutes_to_seconds = minutes * 60
	return hours_to_minutes + minutes_to_seconds + seconds

	#OR

def hours_to_minutes(hours):
	minutes = hours * 60 	
	return minutes

def minutes_to_seconds(minutes):
	seconds = minutes * 60
	return seconds

def convert_to_seconds(hours,minutes,seconds):
	return minutes_to_seconds(hours_to_minutes(hours)) + minutes_to_seconds(minutes) + seconds


#2
def convert_to_inches(feet, inches):
	feet_to_inches = feet * 12
	return feet_to_inches + inches