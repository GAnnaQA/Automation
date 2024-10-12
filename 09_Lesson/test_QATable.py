from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from QATable import Users


db_connection_string = "postgresql://postgres:3:[:O3t8c^'a8@localhost:5432/QA"


def test_add_user():
    new_user_id = 446
    new_user_email = 'user1@mail.ru'
    user_subject_id = 1
    db = create_engine(db_connection_string)
    Session = sessionmaker(bind=db)
    sess = Session()
    new_user = Users(user_id=new_user_id,
                     user_email=new_user_email,
                     subject_id=user_subject_id)
    sess.add(new_user)
    sess.commit()
    result = sess.query(Users).filter(Users.user_id == new_user_id).first()
    if result is not None:
        saved_user_id = result.user_id
        saved_user_email = result.user_email
        saved_subject_id = result.subject_id
    else:
        print("Пользователь не найден.")

    assert saved_user_id == new_user_id
    assert saved_user_email == new_user_email
    assert saved_subject_id == user_subject_id

    sess.query(Users).filter(Users.user_id == new_user_id).delete()
    sess.commit()
    sess.close()


def test_update_user():
    new_user_id = 855
    new_user_email = 'user2@mail.ru'
    user_subject_id = 3
    db = create_engine(db_connection_string)
    Session = sessionmaker(bind=db)
    sess = Session()
    new_user = Users(
        user_id=new_user_id,
        user_email=new_user_email,
        subject_id=user_subject_id
        )
    sess.add(new_user)
    sess.commit()
    update_email = 'Update@mail.ru'
    sess.query(Users).filter(Users.user_id == new_user_id).update({
        Users.user_email: update_email
        })
    sess.commit()
    result = sess.query(Users).filter(Users.user_id == new_user_id).first()
    if result is not None:
        saved_user_id = result.user_id
        saved_user_email = result.user_email
        saved_subject_id = result.subject_id
    else:
        print("Пользователь не найден.")

    assert saved_user_id == new_user_id
    assert saved_user_email == update_email
    assert saved_subject_id == user_subject_id

    sess.query(Users).filter(Users.user_id == new_user_id).delete()
    sess.commit()
    sess.close()


def test_delete_user():
    new_user_id = 855
    new_user_email = 'user3@mail.ru'
    user_subject_id = 2
    db = create_engine(db_connection_string)
    Session = sessionmaker(bind=db)
    sess = Session()
    new_user = Users(
        user_id=new_user_id,
        user_email=new_user_email,
        subject_id=user_subject_id)
    sess.add(new_user)
    sess.commit()
    sess.query(Users).filter(Users.user_id == new_user_id).delete()
    sess.commit()
    result = sess.query(Users).filter(Users.user_id == new_user_id).all()

    assert len(result) == 0
