#!/bin/bash
# Script that sends a DELETE request 
curl -si -X OPTIONS   "${1}" | grep "Allow" | cut -c 8-
