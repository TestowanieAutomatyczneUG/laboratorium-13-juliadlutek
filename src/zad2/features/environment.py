from Password import Password


def before_scenario(context, scenario):
    context.password = Password()


def after_scenario(context, scenario):
    context.password = None
