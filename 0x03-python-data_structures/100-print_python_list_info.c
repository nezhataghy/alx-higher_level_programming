#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PyObject
 */
void print_python_list_info(PyObject *p)
{
	int memory_alloc, size, index = 0;
	PyObject *member;

	memory_alloc = ((PyListObject *)p)->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", memory_alloc);
	while (index < size)
	{
		member = PyList_GetItem(p, index);
		printf("Element %d: %s\n", index, Py_TYPE(member)->tp_name);
		index++;
	}
}
