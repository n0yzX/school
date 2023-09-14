#include <iostream>

using namespace std;


int aufgabe1() {

    string name;
    int alter;
    string ort;
    float size;
    cout << "Wie ist der Name?";
    cin >> name ;
    cout << "Wie ist das Alter?";
    cin >> alter;
    cout << "Wo wohnt er??";
    cin >> ort;
    cout << "Wie gross ist er?";
    cin >> size;
    cout << name << endl;
    cout << alter << endl;
    cout << ort << endl;
    cout << size;
}


int aufgabe2() {
    float celsius, fahrenheit;
    cout << "Temperatur in Celsius: ";
    cin >> celsius;
    fahrenheit = (celsius * 9/5) + 32;
    cout << "Temperatur in Fahrenheit ist: " << fahrenheit << endl;
}

int aufgabe3(){
    float gewicht, groesse;
    cout << "gebe dein gewicht ein: ";
    cin >> gewicht;
    cout << "gebe deine groesse ein: ";
    cin >> groesse;
    float bmi;
    bmi = (gewicht / (groesse * groesse));
    cout << "dein BMI ist: ";
    cout << bmi;
}

int aufgabe5(){
    int one, two;
    cout << "zahl1: ";
    cin >> one;
    cout << "zahl2: ";
    cin >> two;
    int ergebnis = (one / two);
    cout << "das Ergebnis ist: ";
    cout << ergebnis;
    cout << "der Restwert: " << endl;
    cout << one % two;

}

int aufgabe6() {
    bool one = true;
    int two = 10;
    float three = 17.3;
    string text = "Servus habadere";
    cout << "der Datentyp von variable one: " << typeid(one).name() << endl;
    cout << "der Speicherbedarf von variable one: " << sizeof(one) << " Bytes" << endl;
    cout << "der Datentyp von variable two: " << typeid(two).name() << endl;
    cout << "der Speicherbedarf von variable two: " << sizeof(two) << " Bytes" << endl;
    cout << "der Datentyp von variable three: " << typeid(three).name() << endl;
    cout << "der Speicherbedarf von variable three: " << sizeof(three) << " Bytes" << endl;
    cout << "der Datentyp von variable text: " << typeid(text).name() << endl;
    cout << "der Speicherbedarf von variable text: " << sizeof(text) << " Bytes" << endl;
    return 0;
}


int main()
{
    aufgabe6();
}
