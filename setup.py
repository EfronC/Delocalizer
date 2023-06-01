from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_module = Extension(
    "modify_subs",
    sources=["modify_subs.pyx"],
    language="c++",
    extra_compile_args=["-std=c++11"],
    libraries=["your_libass_library"],  # Replace "your_libass_library" with the actual name of the libass library
    library_dirs=["/path/to/your/libass/library"],  # Replace "/path/to/your/libass/library" with the actual path to the libass library directory
    include_dirs=["/path/to/your/libass/headers"],  # Replace "/path/to/your/libass/headers" with the actual path to the libass header files
)

setup(
    name="modify_subs",
    ext_modules=cythonize([ext_module])
)
