#include <iostream>
#include <fstream>

struct Elem
{
    int data;          
    Elem* left;
    Elem* right;
    Elem* parent;
};

Elem* MAKE(int data, Elem* p) //создание дерева
{
    Elem* q = new Elem; 
    q->data = data;
    q->left = nullptr;
    q->right = nullptr;
    q->parent = p;
    return q;
}

void ADD(int data, Elem*& root) //функция добавления
{
    if (root == nullptr) {
        root = MAKE(data, nullptr);
        return;
    }
    Elem* v = root;
    while ((data < v->data && v->left != nullptr) || (data > v->data && v->right != nullptr))
        if (data < v->data)
            v = v->left;
        else
            v = v->right;
    if (data == v->data)
        return;
    Elem* u = MAKE(data, v);
    if (data < v->data)
        v->left = u;
    else
        v->right = u;
}
 
void PASS(Elem* v) //Проход по дереву и его вывод
{
    if (v == nullptr)
        return;
 

    PASS(v->left);

    std::cout << v->data << std::endl;

    PASS(v->right);

}

Elem* SEARCH(int data, Elem* v) 
{
    if (v == nullptr)
        return v;
    if (v->data == data)
        return v;
    if (data < v->data)
        return SEARCH(data, v->left);
    else
        return SEARCH(data, v->right);
}
void SEARCHING(int data,Elem* v, int c) //Функция поиска
{
    if (v == nullptr) 
    {
        std::cout << "n";
        return;
    }
    else if (v->data == data) 
    {
        std::cout << c;
        return;
    }
    else if (data < v->data)
        SEARCHING(data, v->left, c + 1);
    else
        SEARCHING(data, v->right, c + 1);
}

void DELETE(int data, Elem*& root) // Функция удаления
{
    Elem* u = SEARCH(data, root);
    if (u == nullptr)
        return;

    if (u->left == nullptr && u->right == nullptr && u == root)
    {
        root = nullptr;
        return;
    }

    if (u->left != nullptr && u->right != nullptr)
    {
        Elem* t = u->right;
        while (t->left != nullptr)
            t = t->left;
        u->data = t->data;
        u = t;
    }
    Elem* t;
    if (u->left == nullptr)
        t = u->right;
    else
        t = u->left;
    if (u->parent->left == u)
        u->parent->left = t;
    else
        u->parent->right = t;
    if (t != nullptr)
        t->parent = u->parent;
}

int main()
{
    Elem* root = nullptr;
    std::ifstream in("input.txt"); //Чтение файла в котором заданы команды
    char a;
    int b;
    while (!in.eof())
    {
        in >> a;
        in >> b;
        if (a == '+')
        {
            ADD(b, root); //Добавляет значение в дерево
        }
        else if (a == '?')
        {
            SEARCHING(b, root, 1); //Ищет значение в дереве и выделяет его место
            std::cout << '\n';
        }
        else if (a == '-')
        {
            DELETE(b, root); //Удаляет значение в дереве
        }
        else if (a == 'E') //прекращает выполнение команд
        {
            break;
        }
    
    }
    PASS(root);
    return 0;
}