#include <stdio.h>

// Function to check if a number is a palindrome
int isPalindrome(int num, int originalNum, int reversedNum) {
    if (num == 0) {
        if (originalNum == reversedNum) {
            return 1; // It's a palindrome
        } else {
            return 0; // It's not a palindrome
        }
    } else {
        int lastDigit = num % 10;
        reversedNum = reversedNum * 10 + lastDigit;
        return isPalindrome(num / 10, originalNum, reversedNum);
    }
}

int main() {
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);

    int result = isPalindrome(n, n, 0);

    if (result == 1) {
        printf("It is a palindrome.\n");
    } else {
        printf("It is not a palindrome.\n");
    }

    return 0;
}
