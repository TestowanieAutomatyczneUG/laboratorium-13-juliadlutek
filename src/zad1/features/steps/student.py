from behave import *
from Student import StudentList, Student


@given('we have empty list')
def step_impl(context):
    context.list = StudentList()


@given('we have list with one student')
def step_impl(context):
    context.student = Student("Jan", "Nowak", 1)
    context.list = StudentList([context.student])


@given('we have list with two students')
def step_impl(context):
    context.student1 = Student("Jan", "Nowak", 1)
    context.student2 = Student("Maria", "Kowalska", 2)
    context.list = StudentList([context.student1, context.student2])


@when('we add student to list')
def step_impl(context):
    context.list.addStudent("Jan", "Nowak")


@when('we delete student from list')
def step_impl(context):
    context.list.deleteStudentById(1)


@then('there is one student on list')
def step_impl(context):
    assert len(context.list.getAllStudents()) == 1


@then('there are two students on list')
def step_impl(context):
    assert len(context.list.getAllStudents()) == 2


@then('student list is empty')
def step_impl(context):
    assert len(context.list.getAllStudents()) == 0


@then('student with id 1 exists')
def step_impl(context):
    context.list.getStudentById(1)
    assert context.failed is False

