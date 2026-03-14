#include <string>
#include <iostream>

class Printer
{
public:
    virtual void print(const std::string &document);
};
class Scanner
{
public:
    virtual void scan(std::string &document);
};

int main()
{
    try
    {
        /* code */
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    
    return 0;
}