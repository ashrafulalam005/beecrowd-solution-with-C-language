#include <stdio.h>

int main()
{
    double x1, x2, y1, y2, distance;
    scanf("%lf %lf", &x1, &y1);
    scanf("%lf %lf", &x2, &y2);

    distance = sqrt(pow(x2-x1,2)+pow(y2-y1,2));

    printf("%.4lf\n", distance);
    return 0;
}


