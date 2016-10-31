based_principal_balance = 1738455.78
current_interest = 5.05
current_month = 9
current_year = 2559
pay_per_month = 29300# 29300

new_interests = [4.5, 4.5, 4.5, 6.725]
new_interests = False

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]

def interest_per_day(balance, interest):
    return (balance * (interest/100)) / 365

def is_free(balance):
    if balance < 0:
        print 'you are free'
        return True

def principal_balance(balance, year=0):
    if is_free(balance):
        return
    start_month = current_month if year == 0 else 0

    this_year_dept = 0
    print 'year: %s' % (year + current_year)
    interest = current_interest
    if new_interests:
        interest = new_interests[year] if year < 3 else new_interests[3]

    for month_index in xrange(start_month, 12):
        new_month_interest = interest_per_day(balance, interest) * days_in_months[month_index]
        this_year_dept += new_month_interest
        balance = balance - (pay_per_month - new_month_interest)
        print 'month: %s' % (month_index + 1)
        print 'interest(%s): %s' % (interest, new_month_interest)
        print 'balance: %s' % (balance)
        if is_free(balance):
            return
    print 'this year dept: %s' % (this_year_dept)
    principal_balance(balance, year + 1)

principal_balance(based_principal_balance)
