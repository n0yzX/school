#include <iostream>
#include <string>

struct Bildschirm {
    std::string art;
    std::string marke;
    int bildwiederholfrequenz;
    int stromverbrauch;
    int max_farbtiefe;
};

struct PC {
    std::string name;
    std::string hersteller;
    int speicherplatz;
    int ram;
    Bildschirm monitor;
};

int main() {
    PC pc01;
    pc01.name = "PC01";
    pc01.hersteller = "Hersteller1";
    pc01.speicherplatz = 512;
    pc01.ram = 8; 
    pc01.monitor.art = "LCD";
    pc01.monitor.marke = "Monitor-Marke";
    pc01.monitor.bildwiederholfrequenz = 60;
    pc01.monitor.stromverbrauch = 50;
    pc01.monitor.max_farbtiefe = 32;

    PC pc02;
    pc02.name = "PC02";
    pc02.hersteller = "Hersteller2";
    pc02.speicherplatz = 1024;
    pc02.ram = 16;
    pc02.monitor.art = "LED";
    pc02.monitor.marke = "Monitor-Marke2";
    pc02.monitor.bildwiederholfrequenz = 120;
    pc02.monitor.stromverbrauch = 75;
    pc02.monitor.max_farbtiefe = 24;

    // Ausgabe der Informationen für pc01 und pc02
    std::cout << "PC01:\n";
    std::cout << "Name: " << pc01.name << "\n";
    std::cout << "Hersteller: " << pc01.hersteller << "\n";
    std::cout << "Speicherplatz: " << pc01.speicherplatz << " GB\n";
    std::cout << "RAM: " << pc01.ram << " GB\n";
    std::cout << "Monitorart: " << pc01.monitor.art << "\n";
    std::cout << "Monitor-Marke: " << pc01.monitor.marke << "\n";
    std::cout << "Bildwiederholfrequenz: " << pc01.monitor.bildwiederholfrequenz << " Hz\n";
    std::cout << "Stromverbrauch: " << pc01.monitor.stromverbrauch << " Watt\n";
    std::cout << "Maximale Farbtiefe: " << pc01.monitor.max_farbtiefe << " Bit\n";

    std::cout << "\nPC02:\n";
    std::cout << "Name: " << pc02.name << "\n";
    std::cout << "Hersteller: " << pc02.hersteller << "\n";
    std::cout << "Speicherplatz: " << pc02.speicherplatz << " GB\n";
    std::cout << "RAM: " << pc02.ram << " GB\n";
    std::cout << "Monitorart: " << pc02.monitor.art << "\n";
    std::cout << "Monitor-Marke: " << pc02.monitor.marke << "\n";
    std::cout << "Bildwiederholfrequenz: " << pc02.monitor.bildwiederholfrequenz << " Hz\n";
    std::cout << "Stromverbrauch: " << pc02.monitor.stromverbrauch << " Watt\n";
    std::cout << "Maximale Farbtiefe: " << pc02.monitor.max_farbtiefe << " Bit\n";

    return 0;
}
