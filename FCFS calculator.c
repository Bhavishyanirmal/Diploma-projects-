#include <stdio.h> // Libaray
#include <string.h>
#include <conio.h>

#define max 5 // Define Value

char p[max][10]; // 2D array for process names
int bur[max];
int arr[max];
int ct[max];
int tat[max];
int wt[max];


int n, gc, j, z;
float avgtat = 0; // Change to float for better precision
float avgwt = 0;  // for average WT

void sorting(int bur[], int arr[]); // function declaration
void input();
void calculation(int bur[], int arr[]);

// main function
int main()
{
    printf("\t\033[94mFirst Come First Serve (FCFS) Process Scheduling Calculator\n\n");
    printf("\033[0m");
    printf("\033[0;36mMax process limit: %d\n", max);
    input();
    return 0;
}

// function "input" Inputing the Elements
void input()
{
    int i;
    printf("\nEnter number of processes: ");
    scanf("%d", &n);
    printf("\033[0m");

    if (n > max)
    {
        printf("\nError: The limit is exceeded!\n");
        return;
    }

    for (i = 0; i < n; i++)
    {
        printf("\n\033[0;33mEnter process name:");
        scanf("%s", p[i]);
    }
    printf("\033[0m");

    printf("\n-------------------------------");

    for (i = 0; i < n; i++)
    {
        printf("\n\033[0;31mEnter Burst Time for %s: ", p[i]);
        scanf("%d", &bur[i]);
        if (bur[i] == 0)
        {
            printf("\nError: Burst Time should not be 0\n");
            return;
        }
    }
    printf("\033[0m");
    printf("\n-----------------------------");

    for (i = 0; i < n; i++)
    {
        printf("\n\033[0;31mEnter Arrival Time for %s: ", p[i]);
        scanf("%d", &arr[i]);
        
    }
    printf("\033[0m");
    calculation(bur, arr);
}


// function "calculation" for calculating
void calculation(int bur[], int arr[])
{

    printf("\n\033[0;35m---------------------------------------");

    printf("\nPreparing Gantt Chart...\n");
    printf("---------------------------------------\n");
    printf("\033[0m");
    sorting(bur, arr); // Sorting processes based on arrival times

    // Calculate Completion Time (CT)
    gc = 0; // Start from 0, or you can start from the arrival of the first process

    for (j = 0; j < n; j++)
    {
        if (gc < arr[j]) // If CPU is idle
        {
            printf("\n\n\t\033[0;32mCPU is idle from %d to %d\n\n", gc, arr[j]);
            gc = arr[j]; // Update gc to the arrival time of the next process
        }
        printf("\033[0m");
        gc += bur[j]; // Add the burst time to global clock
        ct[j] = gc;   // Completion time
        printf("\n\033[0;32mCompletion Time for %s: %d", p[j], ct[j]);
    }
    printf("\033[0m");
    // Calculate Turnaround Time (TAT) and Waiting Time (WT)
    printf("\n\n\t\033[0;36m--->Turn around Time (TAT)\n");
    for (z = 0; z < n; z++)
    {
        tat[z] = ct[z] - arr[z]; // TAT = Completion Time - Arrival Time
        printf("\n->TAT for %s: %d", p[z], tat[z]);
        avgtat += tat[z];
    }
    printf("\033[0m");
    avgtat /= n; // Average TAT
    printf("\n\n\n\033[0;35m------>  Average Turn around Time: %.2f", avgtat);
    printf("\033[0m");

    printf("\n\n\t\033[0;33m--->Waiting Time (WT)\n");
    for (z = 0; z < n; z++)
    {
        wt[z] = tat[z] - bur[z]; // WT = TAT - Burst Time
        printf("\n->Waiting Time for %s: %d", p[z], wt[z]);
        avgwt += wt[z];
    }
    printf("\033[0m");
    avgwt /= n;
    printf("\n\n\n\033[0;35m------>  Average waiting Time:%.2f", avgwt);
    printf("\033[0m");
}


// function "sorting" for gnatt chart
void sorting(int bur[], int arr[])
{
    int i, j, temp;
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (arr[i] > arr[j])
            {
                // Swap arrival times
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

                // Swap burst times to keep the order correct
                temp = bur[i];
                bur[i] = bur[j];
                bur[j] = temp;

                // Swap process names as well to maintain the order
                char pname[10];
                strcpy(pname, p[i]);
                strcpy(p[i], p[j]);
                strcpy(p[j], pname);
            }
        }
    }
}