#include <stdio.h>

int main()
{
    double A,B;
    scanf("%lf %lf", &A, &B);
    printf("MEDIA = %.5lf\n", (A*3.5+B*7.5)/(3.5+7.5));
    return 0;
}
