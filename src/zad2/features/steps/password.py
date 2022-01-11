from behave import *


def testPasswd(context, passwd):
    try:
        context.result = context.password.isValid(passwd)
    except Exception as exception:
        context.exception = exception


@when('we check password P1$')
def step_impl(context):
    testPasswd(context, "P1$")


@when('we check password Password1$')
def step_impl(context):
    testPasswd(context, "Password1$")


@when('we check password Password$')
def step_impl(context):
    testPasswd(context, "Password$")


@when('we check password pasword1$')
def step_impl(context):
    testPasswd(context, "pasword1$")


@when('we check password Password1')
def step_impl(context):
    testPasswd(context, "Password1")


@when('we check password 12345')
def step_impl(context):
    testPasswd(context, 12345)


@when('we check password None')
def step_impl(context):
    testPasswd(context, None)


@when('we check empty string')
def step_impl(context):
    testPasswd(context, "")


@then('result is False')
def step_impl(context):
    assert not context.result


@then('result is True')
def step_impl(context):
    assert context.result


@then('function raises ValueError')
def step_impl(context):
    assert isinstance(context.exception, ValueError)

@then('function raises Exception')
def step_impl(context):
    assert isinstance(context.exception, Exception)
