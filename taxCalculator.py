def compute_tax(status, income):
    tax = 0

    if status == 0:  # Single
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 835 + (income - 8350) * 0.15
        elif income <= 82250:
            tax = 4675 + (income - 33950) * 0.25
        elif income <= 171550:
            tax = 16750 + (income - 82250) * 0.28
        elif income <= 372950:
            tax = 41754 + (income - 171550) * 0.33
        else:
            tax = 108216 + (income - 372950) * 0.35

    elif status == 1:  # Married Filing Jointly
        if income <= 16700:
            tax = income * 0.10
        elif income <= 67900:
            tax = 1670 + (income - 16700) * 0.15
        elif income <= 137050:
            tax = 9350 + (income - 67900) * 0.25
        elif income <= 208850:
            tax = 26637 + (income - 137050) * 0.28
        elif income <= 372950:
            tax = 46741 + (income - 208850) * 0.33
        else:
            tax = 90562 + (income - 372950) * 0.35

    elif status == 2:  # Married Filing Separately
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 835 + (income - 8350) * 0.15
        elif income <= 68525:
            tax = 4675 + (income - 33950) * 0.25
        elif income <= 104425:
            tax = 13351 + (income - 68525) * 0.28
        elif income <= 186475:
            tax = 26346 + (income - 104425) * 0.33
        else:
            tax = 48747 + (income - 186475) * 0.35

    elif status == 3:  # Head of Household
        if income <= 11950:
            tax = income * 0.10
        elif income <= 45500:
            tax = 1195 + (income - 11950) * 0.15
        elif income <= 117450:
            tax = 6227 + (income - 45500) * 0.25
        elif income <= 190200:
            tax = 24035 + (income - 117450) * 0.28
        elif income <= 372950:
            tax = 44783 + (income - 190200) * 0.33
        else:
            tax = 103121 + (income - 372950) * 0.35

    return tax


def main():
    print("Tax Filing Status:")
    print("0 = Single")
    print("1 = Married Filing Jointly")
    print("2 = Married Filing Separately")
    print("3 = Head of Household")

    status = int(input("Enter filing status: "))
    income = float(input("Enter taxable income: "))

    tax = compute_tax(status, income)

    print(f"\nYour tax amount is: Le {tax:.2f}")


main()
