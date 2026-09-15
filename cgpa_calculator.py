#include <stdio.h>

int main() {
    int n, i;
    float grade, credit;
    float totalCredits = 0, totalGradePoints = 0;
    float GPA, CGPA;

    printf("Enter the number of courses: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        printf("\nCourse %d\n", i);

        printf("Enter grade point: ");
        scanf("%f", &grade);

        printf("Enter credit hours: ");
        scanf("%f", &credit);

        totalCredits += credit;
        totalGradePoints += grade * credit;
    }

    GPA = totalGradePoints / totalCredits;

    // For one semester, GPA and CGPA are the same
    CGPA = GPA;

    printf("\n-----------------------------\n");
    printf("Total Credits = %.2f\n", totalCredits);
    printf("Total Grade Points = %.2f\n", totalGradePoints);
    printf("Semester GPA = %.2f\n", GPA);
    printf("Overall CGPA = %.2f\n", CGPA);
    printf("-----------------------------\n");

    return 0;
}