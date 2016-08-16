#include <iostream>
#include <string>
#include <stdlib.h>  
using namespace std;



bool gameStart() {
	string choice;
	cout << "Welcome to the Lovely Mother's Day Magic 8 Ball of Favors and Gratitude" << endl;
	cout << "Has anyone told you, you look beautiful today?" << endl;
	cout << "Will you play this game? (Yes/No)" << endl;
	cout << "> ";
	cin >> choice;

	if (choice=="yes"){
		cout << "Oh yippee! " << endl;
		return true;
	}
	else if (choice=="no") {
		cout << "WHOOPS SORRY FOR TRYING TO BOTHER YOU WITH MY KINDNESS!!! get bent." << endl;
		return false;
	}
	else
	{
		cout << "ERR It has to be lower case. Try Again Babe!" << endl;
		return false;
	}
}

void game()
{
	cout << "********************************************************" << endl;
	cout << "*     Let's see what the Magic 8 Ball of Love Says     *" << endl;
	cout << "********************************************************" << endl;
	cout << "Thinking..."                                              << endl;

	string choice;
	cout << "The Mysterious Magic 8 Ball has Returned with an Answer!" << endl;
	cout << "After you've learned everything you need to know... Type QUIT" << endl;
	do
	{
		cout << "Do you wish to recieve a Mother's Day Blessing? (Yes/QUIT)" << endl;
		cout << "> ";
		cin >> choice;
		cout << "\n";
		if (choice == "yes")
		{
			int coupon = rand() % 5 + 1;
			if(coupon == 5)
			{
				cout << "Revan and I love you very much! Take a day off and let Daddy do some work!" << endl;
				cout << "In order to redeem this the Magic 8 Ball of Love must pick this on the day you wish to use it\n" << endl;
			}
			else if (coupon == 4)
			{
				cout << "A Spa day! Take a day off and go to that hair place you like! One free voucher to a spa in IF\n" << endl;
			}
			else if (coupon == 3)
			{
				cout << "Tough Luck Sista, you married a jerk! YOU GET NOTHING!\n" << endl;
			}
			else if (coupon == 2)
			{
				cout << "Time for the real Mother's Day Gift ;) ;) winky\n" << endl;
			}
			else if (coupon == 1)
			{
				cout << "I love you so much Julia, you make my life so blessed and I'm so proud everyday to be able" << endl;
				cout << "to call you my wife. I can't wait until Katherine is born. We have such a beautiful family and" << endl;
				cout << "you make me want to be a better man. I LOVE YOU!!!!!\n" << endl;
			}
		}
	} while (choice != "QUIT");


	cout << "Thank you for playing check back often for more coupons and Motherly Blessing. Have fun y'all!" << endl;
}

int main() 
{
	if (gameStart())
	{
		game();
	}
	
	return 0;
}