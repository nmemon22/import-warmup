import sys
# from portfolio.data import create_portfolio
# import portfolio.data
# import portfolio.report
import portfolio
my_portfolio = portfolio.data.create_portfolio("Retirement")
portfolio.report.print_report(my_portfolio)