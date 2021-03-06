# This file is part of the account_bank_statement_csv module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class AccountBankStatementCsvTestCase(ModuleTestCase):
    'Test Account Bank Statement Csv module'
    module = 'account_bank_statement_csv'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountBankStatementCsvTestCase))
    return suite