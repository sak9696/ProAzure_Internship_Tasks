def prime_or_not():
    while True:
        num = input("Enter a number or 'stop' to exit: ")

        if num == "stop":
            break

        num = int(num)

        if num <= 1:
            print("Not prime")
            continue

        flag = 0
        for i in range(2, num):
            if num % i == 0:
                flag = 1
                break

        if flag == 0:
            print("Prime number")
        else:
            print("Not prime")

prime_or_not()