#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    PyObject *iterator = PyObject_GetIter(p);
    PyObject *item;

    if (!iterator) {
        printf("  [ERROR] Invalid Python List\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PySequence_Size(p));

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    while ((item = PyIter_Next(iterator))) {
        const char *type = item->ob_type->tp_name;
        printf("Element %ld: %s\n", PySequence_Index(p, item), type);
        Py_DECREF(item);
    }

    Py_DECREF(iterator);
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Python Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Size(p);
    printf("[.] bytes object info\n");
    printf("  [.] Size: %ld\n", size);

    printf("  [.] trying string: %s\n", PyUnicode_AsUTF8(PyObject_Repr(p)));

    printf("  [.] first %ld bytes: ", size > 10 ? 10 : size);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx%c", ((char *)PyBytes_AsString(p))[i], i + 1 < size ? ' ' : '\n');
    }
}
