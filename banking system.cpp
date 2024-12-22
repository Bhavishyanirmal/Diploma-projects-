#include <iostream>
#include <stdio.h>
#include <conio.h>
using namespace std;
long int ab, ba, bc;
int d, e;

class Bank
{
public:
    int acno;
    string name;
    long int balance;

public:
    void OpenAccount()
    {
        cout << "Enter Account Number: ";
        cin >> acno;
        if (acno == 1)
        {
            name = "Ravi Dabhi";
            cout << endl;
            cout << "Account Name:" << name << endl;
            balance = 10000;
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        else if (acno == 2)
        {
            name = "Yash Kaveiya";
            cout << endl;
            cout << "Account Name:" << name << endl;
            balance = 10000;
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        else if (acno == 3)
        {
            name = "Nirmal Bhavishya";
            cout << endl;
            cout << "Account Name:" << name << endl;
            balance = 10000;
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        else if (acno == 4)
        {
            name = "Jadeja Pramukhrajsinh ";
            cout << endl;
            cout << "Account Name:" << name << endl;
            balance = 10000;
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        else if (acno == 5)
        {
            name = "Doshi Mrunal";
            cout << endl;
            cout << "Account Name:" << name << endl;
            balance = 10000;
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
    }
    void ShowAccount()
    {
        cout << "Account Number: " << acno << endl;
        cout << "Name: " << name << endl;
        cout << "Balance: " << balance << endl;
    }
    void Deposit()
    {
        int amt;
        cout << endl;
        cout << "Enter Amount U want to deposit? ";
        cin >> amt;
        bc = amt;
        balance = balance + amt;
        cout << "Your Balance:" << balance << endl;
    }
    void Withdrawal()
    {
        int Balance = balance;
        int amt;
        cout << endl;
        cout << "Enter Amount U want to withdraw? ";
        cin >> amt;
        ba = amt;
        if (amt <= balance)
        {
            Balance = Balance - amt;
            balance = Balance;
            cout << "Your remaining Balance:" << balance << endl;
        }
        else
            cout << "Less Balance..." << endl;
    }
    void bank_balance()
    {
        balance = (ab - ba) + bc;
        cout << "bank_balance=" << balance;
    }
    void Trans()
    {

        int a, b, c;
        cout << "Enter the Account Number(Sender):";
        cin >> a;
        if (a == 1)
        {balance=10000;
            name = "Ravi Dabhi";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==1)
            {
            balance =10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
        }
        else if (a == 2)
        {balance=10000;
            name = "Yash Kaveiya";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==2)
            {
            balance =10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            
        }
        else if (a == 3)
        {balance=10000;
            name = "Nirmal Bhavishya";
            cout << endl;
            cout << "Account Name:" << name << endl;
           if(acno==3)
            {
            balance=10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        else if (a == 4)
        {balance=10000;
            name = "JADEJA PRAMUKHRAJSINH S";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==4)
            {
            balance =10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            
            ab = balance;
        }
        else if (a == 5)
        { balance=10000;
            name = "DOSHI MRUNAL S";
            cout << endl;
            cout << "Account Name:" << name << endl;
           if(acno==1)
            {
            balance =10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            
            ab = balance;
        }
        cout << endl;

        cout << "Enter the Account Number (Receiver):";
        cin >> b;
        if (b == 1)
        {balance=10000;
            name = "Ravi Dabhi";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==1)
            {
            balance =10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            
        }
        if (b == 2)
        {
             balance=10000;
            name = "Yash Kaveiya";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==2)
            {
            balance = 10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            
        }
        else if (b == 3)
        {
            balance=10000;
            name = "Nirmal Bhavishya";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==3)
            {
            balance = 10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        else if (b == 4)
        {
             balance=10000;
            name = "JADEJA PRAMUKHRAJSINH S";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==4)
            {
            balance = 10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            
            ab = balance;
        }
        else if (b == 5)
        {
          balance=10000;
            name = "DOSHI MRUNAL S";
            cout << endl;
            cout << "Account Name:" << name << endl;
            if(acno==5)
            {
            balance = 10000+bc-ba;
            }
            cout << "Account Balance:" << balance << endl;
            ab = balance;
        }
        cout << endl;
        cout << "Amount Transfer Rs:";
        cin >> c;
        if (a == 1 && b == 2 || a == 2 && b == 1 || a == 1 && b == 3 || a == 3 && b == 1 || a == 1 && b == 4 || a == 4 && b == 1 || a == 1 && b == 5 || a == 5 && b == 1)
        {
            ::d = balance - c;
            ::e = balance + c;
            balance = ::d;
            balance = ::e;
            cout << "The Amount remaining in sender Rs:" << ::d << endl;
            cout << "The Amount balance in reciever Rs:" << ::e << endl;
        }
        else if (a == 2 && b == 3 || a == 3 && b == 2 || a == 2 && b == 4 || a == 4 && b == 2 || a == 2 && b == 5 || a == 5 && b == 2)
        {
            ::d = balance - c;
            ::e = balance + c;
            balance = ::d;
            balance = ::e;
            cout << "The Amount remaining in sender Rs:" << ::d << endl;
            cout << "The Amount balance in reciever Rs:" << ::e << endl;
        }
        else if (a == 3 && b == 4 || a == 4 && b == 3 || a == 3 && b == 5 || a == 5 && b == 3)
        {
            ::d = balance - c;
            ::e = balance + c;
            balance = ::d;
            balance = ::e;
            cout << "The Amount remaining in sender Rs:" << ::d << endl;
            cout << "The Amount balance in reciever Rs:" << ::e << endl;
        }
        else if (a == 4 && b == 5 || a == 5 && b == 4)
        {
            ::d = balance - c;
            ::e = balance + c;
            balance = ::d;
            balance = ::e;
            cout << "The Amount remaining in sender Rs:" << ::d << endl;
            cout << "The Amount balance in reciever Rs:" << ::e << endl;
        }
    }
    void new_acc()
    {
        int b;
        long int c;
        char a[20];
        cout << "Enter the Account Name:";
        cin >> a;
        cout << "Enter Your DOB:";
        cin >> b;
        cout << "Enter Mobile Number:";
        cin >> c;
        cout << "Your Account has been created successfully";
    }

    int Search(int);
};

int Bank::Search(int a)
{
    a = acno;
    if (acno == a)
    {
        ShowAccount();
        return (1);
    }
    return (0);
}

// main code
int main()
{

    Bank C[3];

    int found = 0, a, ch, i;
    for (i = 1; i <= 1; i++)
    {
        C[i].OpenAccount();
    }

    do
    {
    dis:
        // display options
        cout << "\n\n1:By Account No\n2:Deposit\n3:Withdraw\n4:check balance:\n5:Transactio(RTGS):\n6:New Account" << endl;

        // user input
        cout << endl;
        cout << "Please input your choice: ";
        cin >> ch;
        cout << endl;

        switch (ch)
        {

        case 1: // searching the record

            for (i = 1; i <= 1; i++)
            {
                found = C[i].Search(a);
                if (found)
                    break;
            }
            if (!found)
                cout << "Record Not Found" << endl;
            break;
        case 2: // deposit operation

            cout << endl;
            for (i = 1; i <= 1; i++)
            {

                found = C[i].Search(a);
                if (found)
                {

                    C[i].Deposit();
                    break;
                }
            }
            if (!found)
                cout << "Record Not Found" << endl;
            break;

        case 3: // withdraw operation

            for (i = 1; i <= 1; i++)
            {
                found = C[i].Search(a);
                if (found)
                {
                    C[i].Withdrawal();
                    break;
                }
            }
            if (!found)
                cout << "Record Not Found" << endl;
            break;

        case 4:

            C[i].bank_balance();
            break;
        case 5:
            C[i].Trans();

            goto dis;
            break;
        case 6:
            C[i].new_acc();
            break;

        default:
            cout << "Wrong Option" << endl;
        }
    } while (ch != 7);
    cout << "Please Enter the Number between (1-6)";
    return 0;
}