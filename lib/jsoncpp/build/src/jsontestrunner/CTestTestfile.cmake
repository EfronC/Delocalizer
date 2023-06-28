# CMake generated Testfile for 
# Source directory: /home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner
# Build directory: /home/efrain/Work/Delocalizer/lib/jsoncpp/build/src/jsontestrunner
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(jsoncpp_readerwriter "/home/efrain/Work/environments/Delocalizer/bin/python3.10" "-B" "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/../../test/runjsontests.py" "/home/efrain/Work/Delocalizer/lib/jsoncpp/build/bin/jsontestrunner_exe" "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/../../test/data")
set_tests_properties(jsoncpp_readerwriter PROPERTIES  WORKING_DIRECTORY "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/../../test/data" _BACKTRACE_TRIPLES "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/CMakeLists.txt;43;add_test;/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/CMakeLists.txt;0;")
add_test(jsoncpp_readerwriter_json_checker "/home/efrain/Work/environments/Delocalizer/bin/python3.10" "-B" "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/../../test/runjsontests.py" "--with-json-checker" "/home/efrain/Work/Delocalizer/lib/jsoncpp/build/bin/jsontestrunner_exe" "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/../../test/data")
set_tests_properties(jsoncpp_readerwriter_json_checker PROPERTIES  WORKING_DIRECTORY "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/../../test/data" _BACKTRACE_TRIPLES "/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/CMakeLists.txt;47;add_test;/home/efrain/Work/Delocalizer/lib/jsoncpp/src/jsontestrunner/CMakeLists.txt;0;")
