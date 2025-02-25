#!/usr/bin/env python
import sqlite3
from pytest import fixture

@fixture
def common_fixture():  # user-defined fixture
    return ['alpha', 'beta', 'gamma']

@fixture
def presidents():
    conn = sqlite3.connect('presidents.db')
    return conn.cursor.execute('select * from presidents')

# predefined hook (all hooks start with 'pytest_')
def pytest_runtest_setup(item):
    if "test_config" in str(item):
        print(f"Hello from setup, {item}", end=" ")
