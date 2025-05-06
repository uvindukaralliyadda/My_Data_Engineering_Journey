
has_high_income=False
has_good_cre=False

if has_good_cre and has_high_income:
    print("Eligible for Loan")

elif has_good_cre:
    print("Should have good Income")

elif has_high_income:
    print("Should have good credit")

else:
    print("Must have both")
