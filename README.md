# PyLedger

Python script that reads a ledger and gets the account balance for a given user and for a specific date.

### Requirements

- Docker (https://www.docker.com)

### Installation
1. `$ docker-compose build`
2. `$ docker-compose up -d`
3. `$ docker exec -ti pyledger-app sh`

### Usage

Run the python REPL and use the following example:

```
from src.ledger import Ledger

ledger = Ledger('data/ledger.csv')
# get account balance for an account id to current date
ledger.get_account_balance('john')
# get account balance for an account id for a certain day
ledger.get_account_balance('mary', '2015-01-24')
```

### Run tests

From the docker shell (`docker exec -ti pyledger-app sh`) run the following command:

`py.test`
