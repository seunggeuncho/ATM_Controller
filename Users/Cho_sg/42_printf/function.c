#include "ft_printf.h"

int ft_putchar(char c)
{
    write(1, &c, 1);
    return (1);
}

int ft_putstr(char *s)
{
    int i;

    i = 0;
    if (!s)
    {
        write(1, "(null)", 6);
        return (6);
    }
    while (s[i])
    {
        write(1, &s[i], 1);
        i++;
    }
    return (i);
}

int ft_putnbr(int n)
{
    int i;
    
    i = 0;
    if (n == -2147483648)
    {
        i += (ft_putstr("-2147483648"));
        n = 8;
    }
    if (n < 0)
    {
        i += (ft_putchar('-'));
        n = -n;
    }
    if (n > 9)
    {
        i += (ft_putnbr(n / 10));
        i += (ft_putnbr(n % 10));
    }
    else
        i += (ft_putchar(n + 48));
    return (i);
}

int ft_unsigned(unsigned int n)
{
    int i;

    i = 0;
    if (n > 9)
    {
        i += (ft_unsigned(n / 10));
        i += (ft_unsigned(n % 10));
    }
    else
        i += (ft_putchar(n + 48));
    return (i);
}

int ft_hexa(unsigned long ul, int n)
{
    int i;

    i = 0;
    if (ul % 16 >= 16)
    {
        i += ft_hexa(ul / 16, n);
    }
    if (ul % 16 / 10)
    {
        i += ft_putchar((ul % 16) + 48);
    }
    else
    {
        if (n == 1)
            i += ft_putchar((ul % 16) + 87);
        else
            i += ft_putchar((ul % 16) + 55);
    }
    return (i);
}