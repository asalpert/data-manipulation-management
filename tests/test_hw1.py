import os
from pathlib import Path
from importlib.util import find_spec
import datetime


def test_module_exists():
    assert Path("fake_records.py").exists()


def test_faker_installed():
    assert find_spec("faker")


def test_generate():
    import fake_records

    df = fake_records.generate()
    assert len(df) == 1000
    assert {
        "First Name",
        "Last Name",
        "Birthday",
        "Email",
        "Phone Number",
    } == set(df.columns)


def test_data_folder_ignored():
    from git import Repo

    r = Repo(".")
    assert r.ignored("data")


def test_save():

    import pandas as pd
    import fake_records

    df = pd.DataFrame({"a": [1]})
    fake_records.save(df)
    assert os.path.exists("data/fake_records.csv")
    os.remove("data/fake_records.csv")
    os.rmdir("data")


def test_load(tmp_path):
    import fake_records
    import pandas as pd

    df = pd.DataFrame(
        {
            "First Name": ["A"],
            "Last Name": ["B"],
            "Birthday": [pd.Timestamp(datetime.date(2000, 1, 1))],
            "Phone Number": ["555-555-5555"],
        },
        index=pd.Index(["example@example.com"], name="Email"),
    )
    df.to_csv(tmp_path / "test.csv")
    pd.testing.assert_frame_equal(fake_records.load(tmp_path / "test.csv"), df)


def test_assign_salaries():
    import fake_records
    import pandas as pd

    df = pd.DataFrame({"a": [1 for _ in 1000]})
    df = fake_records.assign_salaries(df)
    df["Salary"].min() >= 20000
    df["Salary"].max() <= 100000
    assert len(df.columns) == 2
