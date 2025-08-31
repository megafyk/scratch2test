#include <iostream>
#include <fcntl.h>
int main()
{
    std::cout << "Hello world!" << std::endl;
    int  fd = open("/dev/net/tun", O_RDWR);
    std::cout << fd << std::endl;     
    return 0;
}