#include <stdio.h>

int factorial_tail(int n, int acc) {
    if (n == 0 || n == 1) {
        return acc;
    } else {
        return factorial_tail(n - 1, n * acc);
    }
}

int factorial(int n) {
    // original recursion
    // if (n == 0 || n == 1) {
    //     return 1;
    // } else {
    //     return n * factorial(n - 1);
    // }
    return factorial_tail(n, 1);
}

int main() {
    printf("%d\n", factorial(5));
    return 0;
}
