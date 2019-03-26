# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def create_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="sdfdsf", lastname="sdfsdfsdfsd", address="fdfsfdsfsfsd", mobile="9797987987"))
    app.session.logout()