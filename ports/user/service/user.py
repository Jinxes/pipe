# -*- coding:utf8 -*-
from boot.kernel import app
from common.singleton import singleton
from boot import db
from ports.user.model.user import User


@singleton
class UserService:

    _curent_user = None

    def email_exist(self, email):
        '''
        确认电子邮件是否有重复
        :param email: string
        :return: bool
        '''
        num = User.query.filter_by(email=email).count()
        return True if num > 0 else False

    def findById(self, id):
        '''
        根据 id 定位单个用户
        :param id: User.id
        :return: User
        '''
        user = User.query.filter_by(id=id).first()
        return user

    def set_curent_user(self, user):
        '''
        设置当前用户
        :param user: User
        :return: None
        '''
        self._curent_user = user

    def get_curent_user(self):
        '''
        根据当前 token 中的用户标识定位单个用户
        使用前必须调用闭包 authorization.dependent
        或调用 self.set_curent_user 方法指定当前用户
        :return: User
        '''
        return self._curent_user
