all_teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
               'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(dict_of_teachers):
  count = 0
  target_teacher = None
  for teacher in dict_of_teachers:
    if len(dict_of_teachers[teacher]) > count:
        count = len(dict_of_teachers[teacher])
        target_teacher = teacher
  return target_teacher

def stats(dict_of_teachers):
  output_list = []
  for teacher in dict_of_teachers:
    output_list.append([teacher, len(dict_of_teachers[teacher])])
  return output_list

def courses(dict_of_teachers):
	all_courses = []
	for teacher_courses in dict_of_teachers.values():
			all_courses.extend(teacher_courses)
	return all_courses
