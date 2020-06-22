from datetime import datetime

import pytest
import pandas as pd

from src.ledger import Ledger


def test_get_account_balance(mocker):
    mock_read_csv = mocker.patch('src.ledger.pd.read_csv')
    mock_read_csv.return_value = pd.DataFrame({
        'date': pd.Series([
            datetime(2015, 1, 16),
            datetime(2015, 1, 17),
            datetime(2015, 1, 17),
            datetime(2015, 1, 17),
            datetime(2015, 1, 18),
        ]),
        'from': pd.Series([
            'john',
            'john',
            'mary',
            'dragos',
            'mary',
        ]),
        'to': pd.Series([
            'mary',
            'supermarket',
            'insurance',
            'mary',
            'supermakert',
        ]),
        'amount': pd.Series([
            135.00,
            20.00,
            100.00,
            90.00,
            10.00,
        ]),
    })

    ledger = Ledger('data.csv')
    assert ledger.get_account_balance('john') == '§-155.00'
    assert ledger.get_account_balance('mary') == '§115.00'


def test_get_account_balance_with_date(mocker):
    mock_read_csv = mocker.patch('src.ledger.pd.read_csv')
    mock_read_csv.return_value = pd.DataFrame({
        'date': pd.Series([
            datetime(2015, 1, 16),
            datetime(2015, 1, 17),
            datetime(2015, 1, 17),
            datetime(2015, 1, 17),
            datetime(2015, 1, 18),
        ]),
        'from': pd.Series([
            'john',
            'john',
            'mary',
            'dragos',
            'mary',
        ]),
        'to': pd.Series([
            'mary',
            'supermarket',
            'insurance',
            'mary',
            'supermakert',
        ]),
        'amount': pd.Series([
            135.00,
            20.00,
            100.00,
            90.00,
            10.00,
        ]),
    })

    ledger = Ledger('data.csv')
    assert ledger.get_account_balance('mary', '2015-01-17') == '§125.00'
