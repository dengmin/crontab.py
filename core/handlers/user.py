#!/usr/bin/env python
from flask import session, g, flash
from core.model import User
from flask_peewee.utils import check_password

class UserHandler(object):

    def authenticate(self, username, password):
        active = User.select().where(User.active == True)
        try:
            user = active.where(User.username == username).get()
        except User.DoesNotExist:
            return False
        else:
            if not check_password(password, user.password):
                return False
            return user

    def login_user(self, user):
        session['logged_in'] = True
        session['user_pk'] = user.get_id()
        session.permanent = True
        g.user = user
        flash('You are logged in as %s' % user, 'success')

    def logout_user(self):
        session.clear()
        g.user = None
        flash('You are now logged out', 'success')

    def get_logged_in_user(self):
        if session.get('logged_in'):
            if getattr(g, 'user', None):
                return g.user

            try:
                return User.select().where(
                    User.active == True,
                    User.id == session.get('user_pk')
                ).get()
            except User.DoesNotExist:
                pass