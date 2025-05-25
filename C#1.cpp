#include <iostream>

int main() {
    int birth_year, current_year, age;
    
    //Ask user for their birth year
    std::cout << "Enter your year of birth: ";
    std::cin >> birth_year;

    //Ask user for the current year
    std::cout << "Enter the current year: ";
    std::cin >> current_year;

    //Calculate age
    age = current_year - birth_year;
    
    //Display the result
    std::cout << " You're " << age << "years old." <<std::endl;
    
    int result = 0;
}
