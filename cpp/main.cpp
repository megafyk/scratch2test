#include <iostream>
#include <thread>

int main()
{
    std::thread t1([]() {
        std::cout << "Hello from thread 1!" << std::endl;
    });
    std::thread t2([]() {
        std::cout << "Hello from thread 2!" << std::endl;
    });
    return 0;
}