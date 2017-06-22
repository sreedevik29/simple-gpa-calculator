# Creating a gpa calculator
# need variables for each subject
# if and elif statements 
# --> if variable is between 85-100, then gpa is 4.0
# then return overall average

def main():
	subject1 = 94
	subject2 = 88
	subject3 = 89
	subject4 = 89
	subject5 = 85

	average_subject = (subject1 + subject2 + subject3 + subject4 + subject5)/5
	print(average_subject)

	if average_subject > 85:
		print("Your GPA is 4.0")
	elif average_subject > 80:
		print("Your GPA is 3.7")
	elif average_subject > 75:
		print("Your GPA is 3.3")
	elif average_subject > 70:
		print("Your GPA is 3.0")
	elif average_subject > 60:
		print("Your GPA is 2.3")
	elif average_subject > 55:
		print("Your GPA is 1.7")
	elif average_subject > 50:
		print("Your GPA is 1.0")
	else:
		print("I'm sorry, you have failed the semester. Your GPA is 0")

if __name__ == '__main__':
	main()
