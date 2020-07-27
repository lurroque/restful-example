from src.app import app, save_to_db, User, db
import pytest


def test_save_to_db_with_success():
    name = "shuri"
    save_to_db(name)
    assert User.query.filter_by(name=name).count() == 1
    User.query.delete()
    db.session.commit()

