#include <iostream>
#include <limits>
#include <math.h>
using std::cin;
using std::cout;
using std::endl;
using std::sqrt;

void displayMenu()
{
    cout << "Number Processors Tools" << endl;
    cout << "1. Prime number checker" << endl;
    cout << "2. Number base converter (binary, decimal, hex)" << endl;
    cout << "3. Statistical calculator (mean, median, mode)" << endl;
    cout << "4. Fibonacci sequence generator" << endl;
    cout << "5. Exit" << endl;
    cout << "Please choose options from 1-5: " << endl;
}
void clear_buffer()
{
    cin.clear();
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
int input()
{
    int op;
    if (!(cin >> op))
    {
        clear_buffer();
        cout << "Invalid option" << endl;
        return -1;
    }
    if (op < 1 || op > 5)
    {
        cout << "Invalid option" << endl;
        return -1;
    }
    return op;
}

void check_prime()
{
    cout << "check_prime, please enter num: " << endl;
    long long num;
    cin >> num;
    if (num < 1)
    {
        cout << num << " is not prime" << endl;
        return;
    }
    if (num == 2 || num == 3)
    {
        cout << num << " is prime" << endl;
        return;
    }
    if (num % 2 == 0)
    {
        cout << num << " is not prime" << endl;
        return;
    }
    for (int i = 3; i < sqrt(num) + 1; i++) {
        if (num % i == 0) {
            cout << num << " is not prime" << endl;
            return;
        }
    }
    cout << num << " is prime" << endl;
}
void base_convert()
{
    cout << "base_convert" << endl;
}
void stat_calc()
{
    cout << "stat_calc" << endl;
}
void fib()
{
    cout << "fib" << endl;
}
int main()
{
    while (true)
    {
        displayMenu();
        int op = input();
        bool skip = false;
        switch (op)
        {
        case 1:
            check_prime();
            break;
        case 2:
            base_convert();
            break;
        case 3:
            stat_calc();
            break;
        case 4:
            fib();
            break;
        case 5:
            skip = true;
            break;
        default:
            break;
        }

        if (skip)
        {
            break;
        }
    }
    return 0;
}