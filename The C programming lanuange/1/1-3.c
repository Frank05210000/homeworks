#include <stdio.h>

int main()
{
    printf("標題叫我做一個標題\n");
    float fahr, celsius;
    int LOWER = 0,
        UPPER = 300,
        STEP = 20;

    while (fahr < UPPER)
    {
        fahr += STEP;
        celsius = (5.0 / 9.0) * (fahr - 32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
    }
}