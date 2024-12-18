#include<iostream>
using namespace std;

 class A
 { 
   public:
   int a, b, c, d;
   A()
   {
    cout << "enter the rupes:" ;
    cin>>a;
   cout << endl<< endl;
    cout << "enter the gram:";
    cin>>b;
   cout << endl<< endl;
   }
   void get()
    {
    cout << "enter the rupes:"  ;
    cin>>c;
    
   cout << endl<< endl;
    
    }
    void sum()
    {
      d= b * c / a;
      cout << "the ans is:" <<d <<"gram"<< endl;
    }
    
 };
 
 int main()
 {
  A obj;
  obj.get();
  obj.sum();
 }
 
 
 
 
 
 