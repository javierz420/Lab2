print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Enter numbers separated by commas: ")
    numlist = [int(x.strip()) for x in user_input.split(',')]
    return numlist

def calc_average(numlist):
    total = sum(numlist)
    average = total / len(numlist)
    return float(average)

def find_min_max(numlist):
    if not numlist:
        return None, None  # Handle the case when the list is empty
    return min(numlist), max(numlist)

def sort_temperature(numlist):
    sorted_list = sorted(numlist)
    return sorted_list

def calc_median_temperature(numlist):
    sorted_list = sort_temperature(numlist)
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    return median

if __name__ == "__main__":
    display_main_menu()
    numbers = get_user_input()

    average = calc_average(numbers)
    min_num, max_num = find_min_max(numbers)
    sorted_numbers = sort_temperature(numbers)
    median = calc_median_temperature(numbers)

    print("Average:", average)
    print("Minimum:", min_num)
    print("Maximum:", max_num)
    print("Sorted List:", sorted_numbers)
    print("Median:", median)