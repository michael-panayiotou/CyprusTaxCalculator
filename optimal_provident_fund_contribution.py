from termcolor import colored
import math

infin = math.inf


def calculate_tax_bracket(amount, low, high, percentage):
    if amount < low:
        return 0
    if amount < high:
        return (amount - low) * percentage / 100

    return (high - low) * percentage / 100


def calculate_max_provident_fund_contribution(amount, social, gesy):
    return (amount * 20 / 100) - social - gesy


def print_tax_brackets(amount):
    print("20% tax bracket: " + str(calculate_tax_bracket(amount, 19501, 28000, 20)))
    print("25% tax bracket: " + str(calculate_tax_bracket(amount, 28001, 36300, 25)))
    print("30% tax bracket: " + str(calculate_tax_bracket(amount, 36301, 60000, 30)))
    print("35% tax bracket: " + str(calculate_tax_bracket(amount, 60000, infin, 30)))


def calculate_total_tax(amount):
    return calculate_tax_bracket(amount, 19501, 28000, 20) \
           + calculate_tax_bracket(amount, 28001, 36300, 25) \
           + calculate_tax_bracket(amount, 36301, 60000, 30) \
           + calculate_tax_bracket(amount, 60000, infin, 30)


if __name__ == '__main__':
    # User inputs
    monthly_salary = 0
    other_income = 0

    # total annual income calculation & deductions
    total_income = monthly_salary * 13 + other_income
    social_insurance = 8.3 * total_income / 100
    national_health_fund = 2.65 * total_income / 100

    total_taxable_income = total_income - social_insurance - national_health_fund

    print("Taxable income without provident_fund: " + "{:.2f}".format((total_taxable_income)))
    print_tax_brackets(total_taxable_income)
    total_tax_without_provident_fund = calculate_total_tax(total_taxable_income)
    print("Total taxes due (without provident_fund): " + "{:.2f}".format((total_tax_without_provident_fund)))
    print(colored("##########################################################", 'blue'))

    provident_fund_plan = calculate_max_provident_fund_contribution(total_income, social_insurance,
                                                                    national_health_fund)
    total_taxable_income -= provident_fund_plan
    print("Taxable income after provident_fund: " + "{:.2f}".format((total_taxable_income)))
    print_tax_brackets(total_taxable_income)

    total_tax_with_provident_fund = calculate_total_tax(total_taxable_income)
    tax_saving = total_tax_without_provident_fund - total_tax_with_provident_fund
    print("Amount needed for provident_fund (annual): " + "{:.2f}".format((provident_fund_plan)) + " (from pocket: " \
          + "{:.2f}".format((provident_fund_plan - tax_saving)) + " from tax: " + "{:.2f}".format(tax_saving) + ")")
    print("Total taxes due (with provident_fund): " + "{:.2f}".format(total_tax_with_provident_fund))

    print(colored("##########################################################", 'blue'))
    print(colored("Taxes saved: " + "{:.2f}".format((total_tax_without_provident_fund - total_tax_with_provident_fund)),
                  'green'))
    print("Per month contribution: " + colored("{:.2f}".format((provident_fund_plan / 12)), 'red') \
          + " (from pocket: " + colored("{:.2f}".format((provident_fund_plan - tax_saving) / 12), "yellow") \
          + " from tax: " + colored("{:.2f}".format(tax_saving / 12) + ")", 'green'))
