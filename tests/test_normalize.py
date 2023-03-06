import pandas as pd
from mec import normalize


def test_split_addresses():

    contributions = pd.DataFrame.from_records(
        [
            {
                "Street Address": "1 BROOKINGS DR",
                "City": "ST LOUIS",
                "State": "MO",
                "Zip": "63118",
                "Amount": 100,
            },
            {
                "Street Address": "1 BROOKINGS DR",
                "City": "ST LOUIS",
                "State": "MO",
                "Zip": "63118",
                "Amount": 100,
            },
            {
                "Street Address": "1 BROOKINGS DR",
                "City": "KANSAS CITY",
                "State": "MO",
                "Zip": "64030",
                "Amount": 100,
            },
            {
                "Street Address": "1 BROOKINGS DR",
                "City": "CLAYTON",
                "State": "MO",
                "Zip": "63118",
                "Amount": 100,
            },
        ]
    )
    index = pd.MultiIndex.from_frame(
        pd.DataFrame(
            {
                "Street Address": ["1 BROOKINGS DR", "1 BROOKINGS DR"],
                "Zip": ["63118", "64030"],
            }
        )
    )
    pd.testing.assert_frame_equal(
        normalize.split_addresses(contributions),
        pd.DataFrame(
            {
                "City": ["ST LOUIS", "KANSAS CITY"],
                "State": ["MO", "MO"],
            },
            index=index,
        ),
    )


def test_split_recipients():

    contributions = pd.DataFrame.from_records(
        [
            {
                "MECID": "C12345",
                "Committee Name": "Committee A",
                "Amount": 100,
            },
            {
                "MECID": "C12345",
                "Committee Name": "Committee A",
                "Amount": 200,
            },
        ]
    )
    pd.testing.assert_frame_equal(
        normalize.split_recipients(contributions),
        pd.DataFrame(
            {
                "Committee Name": ["Committee A"],
            },
            index=pd.Index(["C12345"], name="MECID"),
        ),
    )


def test_split_contributors():

    contributions = pd.DataFrame.from_records(
        {
            "First Name": ["John", "John", None, None],
            "Last Name": ["Doe", "Doe", None, None],
            "Committee": [None, None, "Committee A", None],
            "Company": [None, None, None, "Company Z"],
            "Street Address": [
                "123 MAIN ST",
                "123 MAIN ST",
                "456 MAIN ST",
                "789 MAIN ST",
            ],
            "Zip": ["63118", "63118", "63118", "63118"],
            "Occupation": ["Student", "Student", None, None],
            "Employer": ["WUSTL", "WUSTL", None, None],
        },
        index=pd.Index(["C12345", "C12345", "C67890", "C90210"], name="MECID"),
    )
    contributions = normalize.split_contributors(contributions)
    assert contributions == {
        "Individual": pd.DataFrame(
            {
                "Street Address": ["123 MAIN ST"],
                "Zip": ["63118"],
                "Occupation": ["Student"],
                "Employer": ["WUSTL"],
            },
            index=pd.Index(["John Doe"], name="Contributor Name"),
        ),
        "Committee": pd.DataFrame(
            {
                "Street Address": ["456 MAIN ST"],
                "Zip": ["63118"],
            },
            index=pd.Index(["Committee A"], name="Contributor Name"),
        ),
        "Company": pd.DataFrame(
            {
                "Street Address": ["789 MAIN ST"],
                "Zip": ["63118"],
            },
            index=pd.Index(["Company Z"], name="Contributor Name"),
        ),
    }
