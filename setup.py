from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_module = Extension(
    "modify_subs",
    sources=["modify_subs.pyx", "modifysubs.cpp"],
    language="c++",
    extra_compile_args=["-std=c++11"],
    libraries=["ass", "jsoncpp"],  # Replace "your_libass_library" with the actual name of the libass library
    library_dirs=["/home/efrain/Work/Delocalizer/lib/libass/lib", "/home/efrain/Work/Delocalizer/lib/jsoncpp/build/lib"],  # Replace "/path/to/your/libass/library" with the actual path to the libass library directory
    include_dirs=["/home/efrain/Work/Delocalizer/lib/libass/include", "/home/efrain/Work/Delocalizer/lib/jsoncpp/include"],  # Replace "/path/to/your/libass/headers" with the actual path to the libass header files
)

setup(
    name="modify_subs",
    ext_modules=cythonize([ext_module], build_dir="./cyfiles")
)
