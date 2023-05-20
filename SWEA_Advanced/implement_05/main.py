# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def permutation(order, k, n):
    if k == n:
        print(order)
    else:
        check = [False]*n
        for i in range(k):
            check[order[i]] = True

        for i in range(n):
            if check[i] == False:
                order[k]= i
                permutation(order, k+1, n)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = [5,5,5,5,5]
    permutation(order, 0, 4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
