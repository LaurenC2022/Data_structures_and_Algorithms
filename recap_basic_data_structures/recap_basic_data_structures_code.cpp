// usage: g++ -o recap_basic_data_structures_code recap_basic_data_structures_code.cpp && ./recap_basic_data_structures_code

#include <iostream>

// struct is a record data type in C++ that allows to store different types of data types in a single record.
struct MyStruct {
    int a;
    int b;
};

// union is a user-defined data type that allows to store different data types in the same memory location.
union MyUnion {
    int a;
    int b;
};

// enum is a user-defined data type that consists of integral constants.
enum MyEnum {
    A,
    B,
    C
};

// typedef is a keyword in C++ used to give data type a new name.     
typedef int myInt;

// Class is a user-defined data type that is used to define properties and methods.
class MyClass {
    public:
        int a;
        int b;
        void print() {
            std::cout << "a: " << a << ", b: " << b << std::endl;
        }
    private:
        int c;
};

// Array Example
int array[5] = {1, 2, 3, 4, 5};
// Direct Access to a thrid element 
int value = array[2];    // o(1)

// Linked List example
struct Node {
    int data;
    Node* next;
};


int main() {
    std::cout << "Hello, World!" << std::endl;

    // struct
    MyStruct myStruct;
    myStruct.a = 10;
    myStruct.b = 20;
    std::cout << "myStruct.a: " << myStruct.a << ", myStruct.b: " << myStruct.b << std::endl;

    // union
    MyUnion myUnion;
    myUnion.a = 10;
    std::cout << "myUnion.a: " << myUnion.a << std::endl;
    myUnion.b = 20;
    std::cout << "myUnion.b: " << myUnion.b << std::endl;

    // enum
    MyEnum myEnum = A;
    std::cout << "myEnum: " << myEnum << std::endl;

    // typedef
    myInt myIntVar = 10;
    std::cout << "myIntVar: " << myIntVar << std::endl;
    
    // class
    MyClass myClass;
    myClass.a = 10;
    myClass.b = 20;
    myClass.print();

    // Creating a linked list
    Node* head = new Node{1, nullptr};
    Node* second = new Node{2, nullptr};
    Node* third = new Node{3, nullptr};

    head -> next = second;
    second -> next = third;

    // Clean up
    delete head;    
    delete second;
    delete third;

    return 0;
}
