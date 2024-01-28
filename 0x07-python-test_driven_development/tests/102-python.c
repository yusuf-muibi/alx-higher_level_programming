#define PY_SSIZE_T_CLEAN
#include <Python.h>
/**
* print_python_string - Prints information about Python strings.
* @p: A PyObject string object.
*/

void print_python_string(PyObject *p)
{
if (!PyUnicode_Check(p))
{
fprintf(stderr, "Invalid String Object\n");
return;
}

Py_ssize_t length = PyUnicode_GET_LENGTH(p);
const char *str = PyUnicode_AsUTF8(p);

if (str == NULL)
{
fprintf(stderr, "Error converting Unicode to UTF-8\n");
return;
}

printf("String content: %s\n", str);
printf("Length: %zd\n", length);
printf("Address: %p\n", (void *)p);
}
