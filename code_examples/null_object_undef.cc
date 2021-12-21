#include <iostream>

class Foo
{
public:
    void hello()
    {
        std::cout << "Hello, World!" << '\n';
    }

    void disp_x()
    {
        std::cout << x << '\n';
    }

    int x;
};

int main(void)
{
    Foo *foo = nullptr;

    foo->hello();

    foo->disp_x();
}
