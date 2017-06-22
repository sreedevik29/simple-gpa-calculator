# Creating a gpa calculator
# need variables for each subject
# need to calculate average
# if and elif statements 
# --> i.e. if variable is between 85-100, then gpa is 4.0
# then return overall average

def subject_grades(subject1, subject2, subject3, subject4, subject5):
	
	average_subject = (subject1 + subject2 + subject3 + subject4 + subject5)/5
	print(average_subject)

	if average_subject > 85:
		print("Your GPA is 4.0")
	elif average_subject > 80:
		print("Your GPA is 3.7")
	elif average_subject > 75:
		print("Your GPA is 3.3")
	elif average_subject > 69:
		print("Your GPA is 3.0")
	elif average_subject > 59:
		print("Your GPA is 2.3")
	elif average_subject > 55:
		print("Your GPA is 1.7")
	elif average_subject > 50:
		print("Your GPA is 1.0")
	else:
		print("I'm sorry, you have failed the semester. Your GPA is 0")

def main():
	subject_grades(67, 70, 89, 50, 76)

if __name__ == '__main__':
	main()
