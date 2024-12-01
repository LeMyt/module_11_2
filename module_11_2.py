import inspect
from pprint import pprint


def introspection_info(obj):
    type_ = type(obj)

    class_name = type_.__name__

    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    module = getattr(type_, '__module__', None)

    special_methods = [
        method for method in attributes
        if method.startswith('__') and method.endswith('__')
    ]

    additional_info = {}
    if isinstance(obj, dict):
        additional_info['keys'] = list(obj.keys())
    elif isinstance(obj, list):
        additional_info['length'] = len(obj)
    elif hasattr(obj, '__doc__'):
        additional_info['documentation'] = obj.__doc__

    return {
        'type': class_name,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'special_methods': special_methods,
        'additional_info': additional_info
    }

number_info = introspection_info(42)
pprint(number_info)