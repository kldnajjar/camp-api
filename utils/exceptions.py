from rest_framework.views import exception_handler


def camp_exception_handler(exc, context):
    response = exception_handler(exc, context)
    errors = response.data
    detail_error = errors.pop('detail', None)
    response.data = {}
    if detail_error:
        response.data['msg'] = detail_error
    if errors:
        response.data['details'] = {}
        for k, v in errors.items():
            response.data['details'][k] = v
    return response
