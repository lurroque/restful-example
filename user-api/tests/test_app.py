from src.app import app, save_to_db, get_users_from_db, User, db
import pytest


def test_save_to_db_with_success():
    name = "shuri"
    save_to_db(name)
    assert User.query.filter_by(name=name).count() == 1
    User.query.delete()
    db.session.commit()


def test_get_users_from_db_with_success():
    expected_user = "shuri"
    save_to_db(expected_user)
    user_list = get_users_from_db()
    assert expected_user in user_list
    User.query.delete()
    db.session.commit()

