#include <iostream>
#include <vector>
#include <string>
#include <limits>
using namespace std;

struct Student {
    int id;
    string name;
    float marks;
};

class StudentManagement {
private:
    vector<Student> students;

public:
    void addStudent() {
        Student s;
        cout << "Enter ID: ";
        while (!(cin >> s.id)) {
            cout << "Invalid input. Enter numeric ID: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        cin.ignore();
        cout << "Enter Name: ";
        getline(cin, s.name);
        cout << "Enter Marks: ";
        while (!(cin >> s.marks) || s.marks < 0 || s.marks > 100) {
            cout << "Invalid marks. Enter between 0 and 100: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        students.push_back(s);
        cout << "Student added successfully!\n";
    }

    void displayStudents() {
        if (students.empty()) {
            cout << "No students found.\n";
            return;
        }
        cout << "\n--- Student List ---\n";
        for (auto &s : students) {
            cout << "ID: " << s.id << ", Name: " << s.name << ", Marks: " << s.marks << "\n";
        }
    }
};

int main() {
    StudentManagement sm;
    int choice;
    do {
        cout << "\n1. Add Student\n2. Display Students\n3. Exit\nEnter choice: ";
        while (!(cin >> choice) || choice < 1 || choice > 3) {
            cout << "Invalid choice. Enter 1-3: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        switch (choice) {
            case 1: sm.addStudent(); break;
            case 2: sm.displayStudents(); break;
            case 3: cout << "Exiting...\n"; break;
        }
    } while (choice != 3);
    return 0;
}
