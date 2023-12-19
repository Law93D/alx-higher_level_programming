#include <stdio.h>
#include <python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t list_size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", list_size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < list_size; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);

        if (PyBytes_Check(item)) {
            printf("bytes\n");
            PyBytesObject *bytes_item = (PyBytesObject *)item;
            printf("[.] bytes object info\n");
            printf("  size: %zd\n", PyBytes_GET_SIZE(bytes_item));

            printf("  trying string: %s\n", PyBytes_AsString(item));

            printf("  first 10 bytes: ");
            Py_ssize_t bytes_length = PyBytes_GET_SIZE(bytes_item);
            Py_ssize_t max_print = bytes_length < 10 ? bytes_length : 10;
            for (Py_ssize_t j = 0; j < max_print; ++j) {
                printf("%02x ", (unsigned char)PyBytes_AS_STRING(bytes_item)[j]);
            }
            printf("\n");
        } else if (PyFloat_Check(item)) {
            printf("float\n");
            printf("[.] float object info\n");
            printf("  value: %.17g\n", PyFloat_AS_DOUBLE(item));
        } else {
            printf("%s\n", Py_TYPE(item)->tp_name);
        }
    }
}
