students = [{'name': 'Nuna','maths':'30', 'english': '63', 'science': '56'}, 
            {'name': 'Mosa','maths':'80', 'english': '63', 'science': '50'},
            {'name': 'Lilo','maths':'62', 'english': '93', 'science': '86'},
            {'name': 'Lebo','maths':'20', 'english': '49', 'science': '46'}]

"""for student in students:
    maths = int(student['maths'])
    english = int(student['english'])
    science = int(student['science'])
    average = (maths + english + science) / 3
    print(f"{student['name']}'s average: {average:.2f}")
"""

    


def get_grade(average):
    if average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


def get_status(average):
    return 'Pass' if average >= 50 else 'Fail'

results = []


for student in students:
    maths = int(student['maths'])
    english = int(student['english'])
    science = int(student['science'])
    average = (maths + english + science) / 3


    result = {
        'name': student['name'],
        'average': round(average,2),
        'grade': get_grade(average),
        'status': get_status(average)
    }
    results.append(result)

for r in results:
    print(r)


class_avg = sum(r['average'] for r in results) / len(results)

highest_mark = max(results, key=lambda r: r['average'])

lowest_mark = min(results, key=lambda r: r['average'])

pass_no = sum(1 for r in results if r['status'] == 'Pass')
fail_no = len(results) - pass_no

print("="*45)
print("====Results And Class Statistic=====")
print("="*45)
print(f"{'Name':<10}{'Average':<12}{'Grade':<10}{'Status':<10}")
print("="*45)

for r in results:
    print(f"{r['name']:<10}{r['average']:<12}{r['grade']:<10}{r['status']:<10}")


print("*"*40)
print("Stats")
print("*"*40)

print(f"Class Average : {class_avg:.2f}")
print(f"Highest Mark : {highest_mark['name']} ({highest_mark['average']})")
print(f"Lowest Mark : {lowest_mark['name']} ({lowest_mark['average']})")

print(f"Pass No :  {pass_no}")
print(f"Fail No :  {fail_no}")


while True:
    search_name = input("\nEnter student name: ").strip()

    if search_name.lower() == 'exit':
        print("Oooopsie!!!")
        break
    
    found = False
    for r in results:
        if r['name'].lower() == search_name.lower():
            print(f"\nName : {r['name']}")
            print(f"Average : {r['average']}")
            print(f"Grade : {r['grade']}")
            print(f"Status : {r['status']}")
            found = True
            break
    
    if not found:
        print(f"No student named '{search_name}' found. Try again")