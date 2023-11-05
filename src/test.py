

socket_message = {
    'user': 'Token <token>',
    'task': '<uuid4>',
    # 'type': 'change_status',
    'details': {
        'status': 'new'
    },
    'timestamp': 2412525235,
}

match socket_message:
    case {"user": str(token), "type": str(type_)}:
        print(f'{token=} | {type_=}')
    case _:
        print('error!')