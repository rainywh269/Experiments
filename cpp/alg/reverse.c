#include<stdio.h>
#include <string.h>

char *strrtok(char *s)
{
    char *end = s + (strlen(s) - 1);
    for(; end > s ; --end, ++s)
    {
        (*s) ^= (*end);
        (*end) ^= (*s);
        (*s) ^= (*end);
    }
}

int main()
{
    char s[] = "My name is Jack";
    char d[] = " ";
    char t[100];
    int i = 0, j = 0, k = 0;
    strrtok(s);
    printf("%s",s );
    //for(i = strlen(s) - 1 ; i >= 0 ;i--)
    //{
    //    if(s[i] == ' ' || i == 0)
    //    {
    //        j = i == 0 ?  i : i + 1;
    //        for(j = j; s[j] != '\0'; j++) t[k++] = s[j];
    //        t[k++] = ' ';
    //        s[i] = '\0';
    //    }
    //}
    //t[k] = '\0';
    return 0;
}
