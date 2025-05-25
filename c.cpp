#include <iostream>
using namespace std;
	
int main()
{
	double hours, rate, pay;
	
	//Get the numbers of hours the employee worked.
	cout << " How many hours did you work? ";
	cin >> hours;
	
	//Get the hourly pay rate.
	cout << " How much are you paid for an hour? ";
	cin >> rate;
	
	//Calculate the pay.
	
	pay = hours + rate;
	
	//Display the pay.
	cout << " Your total pay in $ " << pay << endl;
	return 0;
}
