#1
def draw_square(num):
	for i in range(num):
		print ("* " * num)

draw_square(4)

	#OR

def draw_square(num):
	row = "* " * num + "\n"
	row_squared = row * num
	return row_squared

print draw_square(4)

#2

def draw_checkerboard():
	for y in range(4):	
		num = 0
		for x in range(8):
			if num % 2 != 0:
				print "o   ",
			if num % 2 == 0:
				print "x   ",
			num = num + 1
		print "\n"
		num = 1
		for x in range(8):
			if num % 2 != 0:
				print "o   ",
			if num % 2 == 0:
				print "x   ",
			num = num + 1
		print "\n"

draw_checkerboard()

	#AKA

def draw_checkerboard():
	num = 0
	for y in range(8):	
		num = num + 1
		for x in range(8):
			if num % 2 != 0:
				print "o   ",
			if num % 2 == 0:
				print "x   ",
			num = num + 1
		print "\n"

draw_checkerboard()

# grid = ["*" for i in range(4)]
# print grid

# grid = [range(4)]
# print grid

# print range(4)

# num1 = 4
# num2 = num1 ** num1

# # for i in range(16):
# # 	if i % 4 == 0:
# # 		print "\n"
# # 	else: print "*",

# for i in range(4):
# 	while i < 16:
# 		for i in range(4):
# 			print "*",

#2
# def draw_checkerboard():
# 	for x in range(61):
# 		if x % 2 == 1:
# 			print "o"
# 		if x % 2 == 0:
# 			print "x"

# print draw_checkerboard()
