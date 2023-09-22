#include <iostream>

using namespace std;





int aufgabe1()
{
    int x;
    cout << "geben sie eine Note ein: ";
    cin >> x;

    switch (x) {
    case 1:
        cout << "sehr gut";
        break;
    case 2:
        cout << "gut";
        break;
    case 3:
        cout << "befriedigend";
        break;
    case 4:
        cout << "ausreichend";
        break;
    case 5:
        cout << "5er halt";
        break;
    case 6:
        cout << "ungenügend";
        break;

    }

    return 0;
}


int aufgabe2(){
    cout << "geben sie eine Zahl ein ACHTUNG nur die Zahl 1 und 2 sind gueltig: ";
    int zahl;
    cin >> zahl;

    if(zahl == 1 || zahl == 2){
            cout << "gueltige Zahl: " << zahl;

    }
    else{
            cout << "ungueltige Zahl: " << zahl;
    }

}



int main()
{
    aufgabe2();

    return 0;
}
