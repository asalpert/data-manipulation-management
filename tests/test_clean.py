import pytest
import pandas as pd
from mec import clean


def test_expand_zip():
    zips = pd.Series(["63130-0000", "63130", ""])
    actual = clean.expand_zip(zips)
    assert actual == pd.DataFrame(
        {"Zip": ["63130", "63130", ""], "+4": ["0000", "", ""]}
    )


@pytest.mark.parametrize(
    "element,expected", [("A.", "A"), ("?-b", "B"), ("C", "C"), ("!!", "")]
)
def test_standardize_element(element, expected):
    actual = clean.standardize_element(element)
    assert actual == expected


def test_standardize_frame():
    df = pd.DataFrame(
        {
            "Address 1": ["123 main street."],
            "Address 2": [""],
            "City": ["saint louis"],
            "State": ["MO"],
            "Zip": ["63130"],
        }
    )
    actual = clean.standardize_frame(df)
    pd.testing.assert_frame_equal(
        actual,
        pd.DataFrame(
            {
                "Address 1": ["123 MAIN ST"],
                "Address 2": [""],
                "City": ["ST LOUIS"],
                "State": ["MO"],
                "Zip": ["63130"],
            }
        ),
    )


@pytest.mark.parametrize(
    "element,expected", [("SAINT LOUIS", "ST LOUIS"), ("SAINT CHARLES", "ST CHARLES")]
)
def test_street_suffixes(element, expected):
    actual = clean.street_suffixes(element)
    assert actual == expected


def test_filter_states():
    states = pd.DataFrame({"State": ["MO", "12", ""]})
    actual = clean.filter_states(states)
    assert actual == pd.DataFrame({"State": ["MO"]})


def test_filter_zips():
    zips = pd.DataFrame({"Zip": ["63130", "ABCDE", "06463"]})
    actual = clean.filter_zips(zips)
    assert actual == pd.DataFrame({"Zip": ["63130"]})


def test_clean_addresses():
    addresses = pd.DataFrame(
        {
            "Address 1": ["123 main street.", "", ""],
            "Address 2": ["", "", ""],
            "City": ["saint louis", "", ""],
            "State": ["MO", "12", "MO"],
            "Zip": ["63130-4862", "63130", "06463"],
        }
    )
    cleaned = clean.clean_addresses(addresses)
    pd.testing.assert_frame_equal(
        cleaned,
        pd.DataFrame(
            {
                "Address 1": ["123 MAIN ST"],
                "Address 2": [""],
                "City": ["ST LOUIS"],
                "State": ["MO"],
                "Zip": ["63130"],
                "+4": ["4862"],
            }
        ),
    )
