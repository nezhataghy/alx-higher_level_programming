#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size, mem_allocated;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	mem_allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", mem_allocated);
}
