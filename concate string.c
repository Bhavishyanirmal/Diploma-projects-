#include<stdio.h>
#include<conio.h>
void main()
{
  char s1[40],s2[40];
  char s3[40];
  int i=0,j=0,k=0;
  printf("enrollment number:236090307080\n");
  printf("name: bhavishya \n");
  printf("---------------------------------------\n");
  printf("\nconcate string opration\n\n");
  
  printf("enter string s1 :");
  gets(s1);
  printf("enter string s2 :");
  gets(s2);
  while(s1[i]!=NULL)
  {
   s3[k]=s1[i];
   i++;
   k++;
  }
  
 while(s2[j]!=NULL)
 {
  s3[k]=s2[j];
  j++;
  k++;
 }s3[k]='\0';
 printf("string concate is:");
 puts(s3);
getch();
}