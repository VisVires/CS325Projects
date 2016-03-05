# location of the Python header files
 
PYTHON_VERSION = 2.6
PYTHON_INCLUDE = /usr/include/python2.6
 
# location of the Boost Python include files and library
 
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib
 
# compile mesh classes
TARGET = hello_ext
 
$(TARGET).so: $(TARGET).o
	g++ -shared -Wl,--export-dynamic $(TARGET).o -I $(PYTHON_INCLUDE) -lboost_python -o $(TARGET).so
 
$(TARGET).o: $(TARGET).C
	g++ -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC -c $(TARGET).C
