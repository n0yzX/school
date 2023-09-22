#include <iostream>
#include <iomanip>

using namespace std;

void aufgabe2(){

    float temp[3] = {1.3, 2.4, 3.5};

    for(const auto & i : temp){
        cout << i << ",";
    }

    string pflane [3] = {"Apfel", "Birne", "Banane"};

}

int main() {
    aufgabe2();
    return 0;
}
