from django.http import HttpResponse

from faker import Faker

from .models import Student

faker = Faker()


def generate(request):
    student = Student.objects.create(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=faker.random_int(min=16, max=22)
    )
    return HttpResponse(f"Our student is: {student}")


def generate_set_students(request):
    count = int(request.GET.get('count', 1))
    if count > 100 or count < 1:
        return HttpResponse("Number of students must be between 1 and 100")
    students = []
    for i in range(count):
        student = Student.objects.create(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            age=faker.random_int(min=16, max=22)
        )
        students.append(student)
    names = ", ".join([f"{student.first_name} {student.last_name}, age {student.age}" for student in students])
    return HttpResponse(f"Our students: {names}")
