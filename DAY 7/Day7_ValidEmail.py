email = input("Enter email: ")
if "@" in email:
    if email.count("@") == 1:
        if "." in email:
            if " " not in email:
                if email == email.lower():
                    if email.endswith("@gmail.com"):

                        username = email.split("@")[0]
                        domain = email.split("@")[1]

                        username_check = username.replace(".", "")
                        domain_check = domain.replace(".", "")

                        if username_check.isalpha():
                            if domain_check.isalpha():
                                print("Email is valid")

                                print("Email length:", len(email))
                                print("Reversed email:", email[::-1])
                                print("Email in uppercase:", email.upper())
                            else:
                                print(" Domain contains numbers or special characters")
                        else:
                            print(" Username contains numbers or special characters")
                    else:
                        print(" Only @gmail.com emails are allowed")
                else:
                    print(" Uppercase letters are not allowed")
            else:
                print(" Spaces are not allowed in email")
        else:
            print(" '.' is missing in email")
    else:
        print(" Email must contain exactly one '@'")
else:
    print(" '@' is missing in email")