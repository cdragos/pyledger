from datetime import datetime

import numpy as np
import pandas as pd


class Ledger:

    """A service for parsing ledgers."""

    def __init__(self, filepath):
        """
        Create a new ledger service.

        :param filepath: the file path for the ledger.
        :type filepath: str
        """
        self.filepath = filepath
        self.df = pd.read_csv(
            self.filepath,
            names=['date', 'from', 'to', 'amount'],
            parse_dates=['date'],
            dtype={'amount': np.float32},
            skipinitialspace=True
        )

    def get_account_balance(self, account_id, date=None):
        """Get account balance from ledger for an account.

        :param account_id: A string that represents the account.
        :type account_id: str
        :param date: The date in the format %Y-%m-%d, defaults to None.
        :type date: str, optional
        :return: Returns the balance for the given account.
        :rtype: str
        """
        date = (
            (date and datetime.strptime(date, '%Y-%m-%d')) or datetime.utcnow())
        df_received = self.df[(self.df['to'] == account_id) & (self.df['date'] <= date)]
        df_given = self.df[(self.df['from'] == account_id) & (self.df['date'] <= date)]

        amount_received = df_received['amount'].sum()
        amount_given = df_given['amount'].sum()
        account_balance = amount_received - amount_given

        return f"§{account_balance:.2f}"
