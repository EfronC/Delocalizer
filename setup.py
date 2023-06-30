from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

libass_lib = [".","lib","libass","lib"]
libass_head = [".","lib","libass","include"]
json_lib = [".","lib","jsoncpp","build","lib"]
json_head = [".","lib","jsoncpp","include"]

libass_lib = os.sep.join(libass_lib)
libass_head = os.sep.join(libass_head)
json_lib = os.sep.join(json_lib)
json_head = os.sep.join(json_head)

ext_module = Extension(
    "modify_subs",
    sources=["modify_subs.pyx", "modifysubs.cpp"],
    language="c++",
    extra_compile_args=["-std=c++11"],
    libraries=["ass", "jsoncpp"],  # Replace "your_libass_library" with the actual name of the libass library
    library_dirs=[libass_lib, json_lib],  # Replace "/path/to/your/libass/library" with the actual path to the libass library directory
    include_dirs=[libass_head, json_head],  # Replace "/path/to/your/libass/headers" with the actual path to the libass header files
)

setup(
    name="modify_subs",
    ext_modules=cythonize([ext_module], build_dir="."+os.sep+"cyfiles")
)
