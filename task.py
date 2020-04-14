import json
import statistics

def create_student(first_name, last_name, grades, attendance):
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'grades': grades,
        'attendance': attendance
    }
    return student


def get_all_students_grades(diary, first_name, last_name):
     for student in diary:
        if student['first_name'] == first_name and student['last_name'] == last_name:
            for course in student['grades']:
                yield 'For {} {} in {} grades are {}.'.format(first_name, last_name, course, student['grades'][course])


def get_all_students_attendance(diary, first_name, last_name):
     for student in diary:
        if student['first_name'] == first_name and student['last_name'] == last_name:
            for course in student['attendance']:
                yield 'For {} {} in {} attendance is {}.'.format(first_name, last_name, course, student['attendance'][course])

def get_students_average_grade_in_course(diary, first_name, last_name, course):
    for student in diary:
        if student['first_name'] == first_name and student['last_name'] == last_name:
            for grade in student['grades']:
                if grade == course:
                    return 'For {} {} average in {} is {}.'.format(first_name, last_name, course, statistics.mean(student['grades'][course]))


def get_average_grade_in_course(diary, course):
    for student in diary:
        for grade in student['grades']:
            if grade == course:
                yield 'In {} for {} average is {}' \
                    .format(course, student['first_name'] + ' ' + student['last_name'], statistics.mean(student['grades'][course]))


def get_average_grade_from_course__in_school(diary, course):
    grades = []
    for student in diary:
        for grade in student['grades']:
            if grade == course:
                grades.extend(student['grades'][course])
    return 'In {} average {} for entire school '.format(course, statistics.mean(grades)) 

if __name__ == "__main__":
    diary = []
    grades = {
        'PITE':[5,4,3,5],
        'ENG':[4,4,2]
    }
    attendance = {
        'PITE':{
            '06.04.2020': True,
            '08.04.2020': False
        },
        'ENG':{
            '06.04.2020': True,
            '08.04.2020': True
        }
    }
    diary.append(create_student('Jan','Kowalski',grades, attendance))
    diary.append(create_student('Jan','Nowak',grades, attendance))
    #print(diary)
    with open('data.json', 'w') as diary_file:
        json.dump(diary, diary_file,indent=4)

    for course in get_all_students_grades(diary,'Jan','Kowalski'):
        print(course)

    for course in get_all_students_attendance(diary,'Jan','Kowalski'):
        print(course)

    print(get_students_average_grade_in_course(diary,'Jan','Kowalski','PITE'))
    print(get_students_average_grade_in_course(diary,'Jan','Kowalski','ENG'))
    for average in get_average_grade_in_course(diary, 'PITE'):
        print(average)

    print(get_average_grade_from_course__in_school(diary,'ENG'))
    
    print('\n### Get data from file ###\n')
    with open('data2.json', 'r') as diary_file:
        diary = json.load(diary_file)

    for course in get_all_students_grades(diary,'Donald','Trump'):
        print(course)

    for course in get_all_students_attendance(diary,'Jan','Pasek'):
        print(course)

    print(get_students_average_grade_in_course(diary,'Donald','Trump','PITE'))
    print(get_students_average_grade_in_course(diary,'Jan','Pasek','ENG'))
    for average in get_average_grade_in_course(diary, 'PITE'):
        print(average)

    print(get_average_grade_from_course__in_school(diary,'ENG'))