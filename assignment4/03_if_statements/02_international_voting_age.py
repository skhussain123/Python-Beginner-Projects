# Voting age for different countries
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def check_voting_eligibility(user_age, voting_age, country_name):
    """Checks if the user can vote based on their age and the voting age of the country."""
    if user_age >= voting_age:
        print(f"You can vote in {country_name} where the voting age is {voting_age}.")
    else:
        print(f"You cannot vote in {country_name} where the voting age is {voting_age}.")

def main():
    user_age = int(input("How old are you? "))
    check_voting_eligibility(user_age, PETURKSBOUIPO_AGE, "Peturksbouipo")
    check_voting_eligibility(user_age, STANLAU_AGE, "Stanlau")
    check_voting_eligibility(user_age, MAYENGUA_AGE, "Mayengua")

if __name__ == "__main__":
    main()
