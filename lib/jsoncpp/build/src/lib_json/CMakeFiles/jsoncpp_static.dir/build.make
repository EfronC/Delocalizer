# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/efrain/Work/Delocalizer/lib/jsoncpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/efrain/Work/Delocalizer/lib/jsoncpp/build

# Include any dependencies generated for this target.
include src/lib_json/CMakeFiles/jsoncpp_static.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/lib_json/CMakeFiles/jsoncpp_static.dir/compiler_depend.make

# Include the progress variables for this target.
include src/lib_json/CMakeFiles/jsoncpp_static.dir/progress.make

# Include the compile flags for this target's objects.
include src/lib_json/CMakeFiles/jsoncpp_static.dir/flags.make

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o: src/lib_json/CMakeFiles/jsoncpp_static.dir/flags.make
src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o: ../src/lib_json/json_reader.cpp
src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o: src/lib_json/CMakeFiles/jsoncpp_static.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/efrain/Work/Delocalizer/lib/jsoncpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o -MF CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o.d -o CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o -c /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_reader.cpp

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/jsoncpp_static.dir/json_reader.cpp.i"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_reader.cpp > CMakeFiles/jsoncpp_static.dir/json_reader.cpp.i

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/jsoncpp_static.dir/json_reader.cpp.s"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_reader.cpp -o CMakeFiles/jsoncpp_static.dir/json_reader.cpp.s

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.o: src/lib_json/CMakeFiles/jsoncpp_static.dir/flags.make
src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.o: ../src/lib_json/json_value.cpp
src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.o: src/lib_json/CMakeFiles/jsoncpp_static.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/efrain/Work/Delocalizer/lib/jsoncpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.o"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.o -MF CMakeFiles/jsoncpp_static.dir/json_value.cpp.o.d -o CMakeFiles/jsoncpp_static.dir/json_value.cpp.o -c /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_value.cpp

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/jsoncpp_static.dir/json_value.cpp.i"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_value.cpp > CMakeFiles/jsoncpp_static.dir/json_value.cpp.i

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/jsoncpp_static.dir/json_value.cpp.s"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_value.cpp -o CMakeFiles/jsoncpp_static.dir/json_value.cpp.s

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o: src/lib_json/CMakeFiles/jsoncpp_static.dir/flags.make
src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o: ../src/lib_json/json_writer.cpp
src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o: src/lib_json/CMakeFiles/jsoncpp_static.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/efrain/Work/Delocalizer/lib/jsoncpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o -MF CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o.d -o CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o -c /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_writer.cpp

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/jsoncpp_static.dir/json_writer.cpp.i"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_writer.cpp > CMakeFiles/jsoncpp_static.dir/json_writer.cpp.i

src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/jsoncpp_static.dir/json_writer.cpp.s"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json/json_writer.cpp -o CMakeFiles/jsoncpp_static.dir/json_writer.cpp.s

# Object files for target jsoncpp_static
jsoncpp_static_OBJECTS = \
"CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o" \
"CMakeFiles/jsoncpp_static.dir/json_value.cpp.o" \
"CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o"

# External object files for target jsoncpp_static
jsoncpp_static_EXTERNAL_OBJECTS =

lib/libjsoncpp.a: src/lib_json/CMakeFiles/jsoncpp_static.dir/json_reader.cpp.o
lib/libjsoncpp.a: src/lib_json/CMakeFiles/jsoncpp_static.dir/json_value.cpp.o
lib/libjsoncpp.a: src/lib_json/CMakeFiles/jsoncpp_static.dir/json_writer.cpp.o
lib/libjsoncpp.a: src/lib_json/CMakeFiles/jsoncpp_static.dir/build.make
lib/libjsoncpp.a: src/lib_json/CMakeFiles/jsoncpp_static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/efrain/Work/Delocalizer/lib/jsoncpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX static library ../../lib/libjsoncpp.a"
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && $(CMAKE_COMMAND) -P CMakeFiles/jsoncpp_static.dir/cmake_clean_target.cmake
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/jsoncpp_static.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/lib_json/CMakeFiles/jsoncpp_static.dir/build: lib/libjsoncpp.a
.PHONY : src/lib_json/CMakeFiles/jsoncpp_static.dir/build

src/lib_json/CMakeFiles/jsoncpp_static.dir/clean:
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json && $(CMAKE_COMMAND) -P CMakeFiles/jsoncpp_static.dir/cmake_clean.cmake
.PHONY : src/lib_json/CMakeFiles/jsoncpp_static.dir/clean

src/lib_json/CMakeFiles/jsoncpp_static.dir/depend:
	cd /home/efrain/Work/Delocalizer/lib/jsoncpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/efrain/Work/Delocalizer/lib/jsoncpp /home/efrain/Work/Delocalizer/lib/jsoncpp/src/lib_json /home/efrain/Work/Delocalizer/lib/jsoncpp/build /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/lib_json/CMakeFiles/jsoncpp_static.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/lib_json/CMakeFiles/jsoncpp_static.dir/depend
