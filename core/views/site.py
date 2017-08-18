#!/usr/bin/env python
from flask import Blueprint, render_template

__all__ = ['bp']

bp = Blueprint('site', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    pass