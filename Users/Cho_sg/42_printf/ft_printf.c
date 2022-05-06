#include "ft_printf.h"

void    print(char c, va_list lst, int *i)
{
    if (c == '%')
        (*i) += ft_putchar('%');
    else if (c == 'd' || c == 'i')
        (*i) += ft_putnbr(va_arg(lst, int));
    else if (c == 'c')
        (*i) += ft_putchar(va_arg(lst, int));
    else if (c == 's')
        (*i) += ft_putstr(va_arg(lst, char *));
    else if (c == 'x')
        (*i) += ft_hexa(va_arg(lst, unsigned int), 1);
    else if (c == 'X')
        (*i) += ft_hexa(va_arg(lst, unsigned int), 0);
    else if (c == 'p')
    {
        ft_putstr("0x");
        (*i) += 2;
        (*i) += ft_hexa(va_arg(lst, unsigned long), 1);
    }
    else if (c == 'u')
        (*i) += ft_unsigned(va_arg(lst, unsigned int));
    else
        (*i) += ft_putchar(c);
}
int ft_printf(const char *arg, ...)
{
    int result;
    va_list lst;
    
    result = 0;
    va_start(lst, arg);
    while (*arg)
    {
        if (*arg == '%')
        {
            arg++;
            if (*arg == '\0')
                return (result);
            print(*arg, lst, &i);
        }
        else
        {
            ft_putchar(*arg);
            result++;
        }
        arg++;
    }
    va_end(lst);
    return (result);
}