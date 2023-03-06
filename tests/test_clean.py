import pandas as pd
from mec import clean


def test_strip_punctuation():
    s = pd.Series(["A.", "?B", "C", "!!"])
    pd.testing.assert_series_equal(
        clean.strip_punctuation(s), pd.Series(["A", "B", "C", ""])
    )


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
    pd.testing.assert_frame_equal(
        clean.clean_addresses(addresses),
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
