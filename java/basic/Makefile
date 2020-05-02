#
# Makefile to compile and run Java applications.
#
# Usage:
#   For each application, add an entry in "Application Names" and "Application Rules"
#   make <app_target> -n
#   make <app_target>
#   make clean
#

JFLAGS = -g
JC = javac
JVM = java
RM = rm -f
.SUFFIXES: .java .class

#---------------------
# Applications Names
#---------------------
HELLO_WORLD = HelloWorld

#-----------------
# General Targets
#-----------------
default: run

# Rule to create class files from Java files
.java.class:
	$(JC) $(JFLAGS) $*.java

# Run all applications
r run: hello


#-------------------
# Application Rules
#-------------------
hello: $(HELLO_WORLD).class
	$(JVM) $(HELLO_WORLD)


#-----------
# Cleaning
#-----------
clean:
	$(RM) *.class


