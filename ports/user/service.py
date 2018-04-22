#-*- coding:utf8 -*-
from boot.kernel import app
from opt.singleton import singleton
from werkzeug.security import generate_password_hash, check_password_hash
from boot import db
from ports.user.model.user import User

@singleton
class Service:

    _curent_user = None

    def add(self, email, password, nickname, gender):
        '''
        添加一个用户
        :param email: string
        :param password: string
        :param nickname: string
        :param gender: integer
        :return: bool 成功 True 失败 False
        '''
        try:
            password_hash = self.make_password_hash(password)
            user = User(
                email=email, password=password_hash, nickname=nickname, gender=gender
            )
            db.session.add(user)
            db.session.commit()
            return True
        except Exception:
            return False

    def email_exist(self, email):
        '''
        确认电子邮件是否有重复
        :param email: string
        :return: bool
        '''
        num = User.query.filter_by(email=email).count()
        return True if num > 0 else False

    def make_password_hash(self, password):
        '''
        make password to hash string
        :param password: string
        '''
        return password

    def check_password(self, password, password_hash):
        '''
        检测密码
        :param password: string
        :param password_hash: string
        :return: bool
        '''
        return password_hash == password

    def auth_check_by_email(self, email, password):
        '''
        通过email检测用户是否有权限登录
        :param email: string
        :param password: string
        :return: User|False
        '''
        user = User.query.filter_by(email=email).first()
        if user:
            if self.check_password(password, user.password):
                return user
        return False

    def auth_check_by_id(self, id, password):
        '''
        通过用户 id 检测用户是否有权限登录
        :param email: string
        :param password: string
        :return: User|False
        '''
        user = User.query.get(id)
        if user:
            if self.check_password(password, user.password):
                return user
        return False

    def findById(self, id):
        user = User.query.filter_by(id=id).first()
        return user

    def set_curent_user(self, user):
        self._curent_user = user

    def get_curent_user(self):
        return self._curent_user
