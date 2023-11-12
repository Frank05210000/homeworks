#include <stdio.h>
// 不太了解 還在研究中
#define YES 1
#define NO 0

int main()
{
    // CTRL+Z will Signal to EOF-End of File
    int c, nl, nw, nc, inword; // nl -new line
                               // nw -new word
                               // nc -new chatacter
                               // inword -program in word or not

    inword = NO;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF)
    {
        ++nc;
        if (c == '\n')
            ++nl;
        if (c == ' ' || c == '\t' || c == '\n')
            inword = NO;
        else if (inword == NO)
        {
            inword = YES;
            ++nw;
        }
    }
    printf("%d %d %d\n", nl, nw, nc);

    getchar();
}