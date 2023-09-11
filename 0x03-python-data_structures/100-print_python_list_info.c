#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PyObject
 */
void print_python_list_info(PyObject *p)
{
	PyObject *element;
	int mem_allocated, i = 0;

	/*size = Py_SIZE(p);*/
	/*printf("[*] Size of the Python List = %d\n", size);*/

	mem_allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", mem_allocated);
}
