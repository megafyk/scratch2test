#include <iostream>
#include <fcntl.h>
#include <net/if.h>
#include <linux/if_tun.h>
#include <cstring>
#include <sys/ioctl.h>
#include <unistd.h>
#include <linux/if_ether.h>

int call_tun(char *dev)
{

    int fd;
    if ((fd = open("/dev/net/tun", O_RDWR)) < 0)
    {
        std::cout << "can not open tun/tap devices" << std::endl;
        return 0;
    }

    struct ifreq ifr;
    if (*dev)
    {
        strncpy(ifr.ifr_name, dev, IFNAMSIZ);
    }
    std::cout << sizeof(ifr) << std::endl;
    memset(&ifr, 0, sizeof(ifr));
    ifr.ifr_flags = IFF_TUN | IFF_NO_PI;
    int err;
    if ((err = ioctl(fd, TUNSETIFF, (void *)&ifr)) < 0)
    {
        std::cout << "ERR: Could not ioctl tun: " << strerror(errno) << std::endl;
        close(fd);
        return err;
    }
    strcpy(dev, ifr.ifr_name);
    return fd;
}

int main()
{
    char dev[] = "wlan0";
    int fd = call_tun(dev);
    std::cout << fd << "\n" << dev << std::endl;
    return 0;
}