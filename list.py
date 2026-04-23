student_info = ["Name:", "ID : ", "Course Code : ", "Section : "]
print("Original List:", student_info)
student_info.append("course code")
student_info.pop(2)
student_info.insert(2, "faculty Name :")
print("Modified List:", student_info)
