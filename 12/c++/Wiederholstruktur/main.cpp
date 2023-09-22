#include <iostream>
#include <vector>
#include <string>

using namespace std;



int aufgabe1() {
    vector<string> pflanzen = {"Rose", "Tulpe", "Sonnenblume", "Lilie", "Orchidee"};
    for (const string& p : pflanzen) {
        cout << p << endl;
    }

    cout << "------------------------" << endl;

    pflanzen.insert(pflanzen.begin(), "test");

    for (const string& p : pflanzen) {
        cout << p << endl;
    }

    return 0;
}


int main() {
   aufgabe1();
    return 0;
}
