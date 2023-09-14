#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
	int size, i, Bytes_to_print;
	char *buffer;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = ((PyVarObject *)(p))->ob_size;
		printf("  size: %ld\n", size);
		buffer = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", buffer);

		if (size < 10)
			Bytes_to_print = size + 1;
		else
			Bytes_to_print = 10;

		printf("  first %d bytes:", Bytes_to_print);

		for (i = 0; i < Bytes_to_print; i++)
			if (string[i] >= 0)
				printf(" %02x", string[i]);
			else
				printf(" %02x", 256 + string[i]);

		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
