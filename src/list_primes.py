def get_all_primes(limit: int) -> list:
    if not isinstance(limit, int) or limit <= 1:
        raise ValueError("Given limit should be an integer larger than one. ")
    primes = []
    for i in range(1, limit + 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            primes.append(i)
    return primes


def get_all_primes_between(lower_limit: int, upper_limit: int) -> list:
    primes = []
    try:
        if not isinstance(lower_limit, int) or lower_limit <= 0:
            raise ValueError("Given lower_limit should be an integer larger than zero. ")
        if not isinstance(upper_limit, int) or upper_limit <= 1:
            raise ValueError("Given upper_limit should be an integer larger than one. ")
        if upper_limit <= lower_limit:
            raise ValueError("Given upper_limit should be larger than lower_limit. ")
        
        for i in range(lower_limit, upper_limit + 1):
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
    except Exception as e:
        print("Error...")
        print(e)
    return primes


def main():
    print("Hello. This programm calculates all primes in a given range... ")
    low_lim = input("lower_limit: ")
    upp_lim = input("upper_limit: ")

    print(f"The prime numbers between given limits ({low_lim}, {upp_lim}) are: \n")
    print(get_all_primes_between(int(low_lim), int(upp_lim)))

    input("program finished. press close to exit")


if __name__ == "__main__":
    main()
