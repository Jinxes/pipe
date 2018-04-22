#-*- coding:utf8 -*-
from flask import request
import re

class Validator:

    def __init__(self):
        self.errors = dict()
        self.valid = True

    def invalid(self):
        return not self.valid

    def isvalid(self):
        return self.valid

    def get_errors(self):
        return self.errors

    def set_error(self, base, dic):
        self.valid = False
        if base not in self.errors.keys():
            self.errors[base] = {}
        self.errors[base].update(dic)

    def __call__(self, field):
        self.field = field
        self.value = str(request.args.get(field))
        return self

    def email(self, message = '电子邮件格式错误'):
        str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if not re.match(str, self.value):
            self._push_error_message('email', message)
        return self

    def required(self, message = '不能为空'):
        if (self.value is None) or (self.value == ''):
            self._push_error_message('required', message)
        return self

    def max_length(self, max_length, message = '超出长度'):
        if self.value is None:
            return self
        if (len(self.value) > max_length):
            self._push_error_message('max_length', message)
        return self

    def numeric(self, message = '参数必须为数字'):
        if not self.value.isdigit():
            self._push_error_message('numeric', message)
        return self

    def contain(self, con_list, message = '参数不正确'):
        con_list = [str(i) for i in con_list]
        if self.value not in con_list:
            self._push_error_message('contain', message)
        return self

    def has(self, field):
        if request.args.get(field, None) is None:
            return False
        return True

    def _push_error_message(self, type, message):
        swap = {type: message}
        self.set_error(self.field, swap)
