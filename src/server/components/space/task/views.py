from abc import ABC

from django.shortcuts import render
from django.views.generic import View

socket_message = {
    'user': 'Token <token>',
    'task': '<uuid4>',
    'type': 'change_status',
    'details': {
        'status': 'new'
    },
    'timestamp': 2412525235,
}


class TaskMessageDetail:

    def __init__(self, details: dict) -> None:
        self.__status = details.get('status')

    def status(self):
        return self.__status


class TaskNotificationMessage:

    def __init__(self, message: dict) -> None:
        self.__task = message.get('task')
        self.__type = message.get('type')
        self.__token = message.get('token')
        self.__details = TaskMessageDetail(message.get('details'))

    @property
    def task(self):
        return self.__task

    @property
    def token(self):
        return self.__token

    @property
    def type_(self):
        return self.__type

    @property
    def details(self):
        return self.__details


class ParserCore(ABC):

    def __init__(self): ...


class ParserCron:

    def run(self): ...


class Company(View):

    def get(self, request):
        return render(request, template_name='page/company/index.html')