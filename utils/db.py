from django.db.models import Func


# noinspection PyAbstractClass
class Round2(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'
