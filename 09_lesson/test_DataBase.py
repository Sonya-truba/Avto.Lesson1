from sqlalchemy import create_engine, text

user_name = "ВВОДЯТСЯ ДАННЫЕ УКАЗАННЫЕ В ПИСЬМЕ"
password = "ВВОДЯТСЯ ДАННЫЕ УКАЗАННЫЕ В ПИСЬМЕ"


def test_insert():
    db_connection_string = f"postgresql://{user_name}:{password}@localhost:5432/SkyPro"
    engine = create_engine(db_connection_string)
    with engine.connect() as conn:
        max_id = conn.execute(text("select MAX(subject_id) from subject")).fetchone()[0]
        subject_id = max_id + 1
        subject_title = 'My subject'
        values = {"id": subject_id, "title": subject_title}
        conn.execute(text("insert into subject (subject_id,subject_title) VALUES (:id,:title)"), values)
        conn.commit()
        result_select = conn.execute(text("SELECT * FROM subject where subject_id= :id"), values).fetchall()
        assert result_select[0][0] == subject_id
        return subject_id


def test_update():
    db_connection_string = f"postgresql://{user_name}:{password}@localhost:5432/SkyPro"
    engine = create_engine(db_connection_string)
    with engine.connect() as conn:
        subject_id = test_insert()
        subject_title = 'My subject new'
        values = {"id": subject_id, "title": subject_title}
        conn.execute(text("update subject set subject_title = :title where subject_id= :id "), values)
        conn.commit()
        result_select = conn.execute(text("SELECT subject_title FROM subject where subject_id= :id"), values).scalar()
        assert result_select == subject_title


def test_delete_by_ID():
    db_connection_string = f"postgresql://{user_name}:{password}@localhost:5432/SkyPro"
    engine = create_engine(db_connection_string)
    with engine.connect() as conn:
        max_id = conn.execute(text("select MAX(subject_id) from subject")).scalar()
        values = {"id": max_id}
        conn.execute(text("delete from subject where subject_id = :id "), values)
        conn.commit()
        max_id_new = conn.execute(text("select MAX(subject_id) from subject")).scalar()
        assert max_id_new == max_id - 1
