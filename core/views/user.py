#!/usr/bin/env python

from flask import Blueprint, render_template

__all__ = ['bp']

bp = Blueprint('user', __name__)

@bp.route('/profile')
def profile():
    return render_template('index.html')