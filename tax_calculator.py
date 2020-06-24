#!python
'''
Tax Calculator** - Asks the user to enter a cost and either a country or state tax.
It then returns the tax plus the total cost with tax.
'''

def tax_calculator(income, central_tax = 5.3, state_tax = 3.3):
    '''
    calculate central tax and state tax saparately and return
    taxted income after
    '''
    Ctax_income = (central_tax * income) / 100 #3975
    Stax_income = (state_tax * income) / 100 #2475
    final_income = income - (Ctax_income + Stax_income)#75,000 - 6450 = 68,550
    return final_income


def test_tax_calculator():
    '''
    test case to check
    '''
    assert tax_calculator(75000) == 68550

if __name__ == "__main__":
    test_tax_calculator()
