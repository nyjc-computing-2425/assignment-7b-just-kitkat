# Built-in imports
import math

# Your code below
REF = {
    "A": 70,
    "B": 60,
    "C": 55,
    "D": 50,
    "E": 45,
    "S": 40,
    "U": 0,
}

GRADE = {}
for score in range(101):
    for grade in REF:
        if score >= REF[grade]:
            GRADE[score] = grade
            break


def read_testscores(filename):
    """
    Process student data from the specifiec filename

    Arguments:
    filename: str -- name of the file

    Return:
    List[dict] -- list of dictionaries containing student info
    """
    with open(filename, "r") as f:
        data = f.readlines()[1:] # discard header
        # calls f.close() automatically

    info = [] # list of dict -- keys: class, name, overall, grade
    for item in data:
        item = item.split(",")
        p1, p2, p3, p4 = item[2:]
        overall = (int(p1)/30 * 15) + (int(p2)/40 * 30) + (int(p3)/80 * 35) + (int(p4)/30 * 20)
        overall = math.ceil(overall)
        info.append({
            "class": item[0],
            "name": item[1],
            "overall": overall,
            "grade": GRADE[overall],
        })
        
    return info


def analyze_grades(studentdata):
    """
    Process studentdata and return the analytics of 
    how the students did (number of students who 
    attained each grade per class)

    Arguments:
    studentdata: list -- list of student data

    Return:
    dict -- analytics of students' grades
    """
    data = {}
    for item in studentdata:
        student_class, grade = item["class"], item["grade"]
        if student_class in data: # class exists
            data[student_class][grade] += 1
        else: # class doesn't exist, create class data
            data[student_class]={
                "A": 0,
                "B": 0,
                "C": 0,
                "D": 0,
                "E": 0,
                "S": 0,
                "U": 0,
            }
            data[student_class][grade] += 1

    return data

