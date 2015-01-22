#include<stdio.h>
void reverse1(char* str)
{
    int length;
    int i;
    char upper;
    char lower;
    length = strlen(str);
    if (length == 0)
    {
        printf("The string is null\n");
        return;
    }
    for(i = 0; i < length; i++)
    {
        if(str[i] >='a' && str[i] <= 'z')
        {
            upper = ('A' + str[i] - 'a');
            str[i] = upper;
        }
        else
        {
            lower = ('a' + str[i] - 'A');
            str[i] = lower;
        }
    }
}
void reverse2(char* str)
{
    char* end = str;
    char tmp;
    if(str)
    {
        while(*end)
        {
            ++end;
        }
        --end;
        while(str < end)
        {
            tmp = *str;
            *str++ = *end;
            *end-- = tmp;
        }
    }
}
int main()
{
    char str[50];
    printf("Enter a string :");
    gets(str);
    reverse1(str);
    printf("The reverse1 string is %s\n", str);
    reverse2(str);
    printf("The reverse2 string is %s\n", str);
    return 0;
}
