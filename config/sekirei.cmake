# for Intel Compiler
set(CMAKE_C_COMPILER "icc" CACHE STRING "" FORCE)
set(CMAKE_C_FLAGS_RELEASE "-O3 -DNDEBUG -xCORE-AVX2 -mcmodel=large -shared-intel -Wno-unknown-pragmas" CACHE STRING "" FORCE)
set(CMAKE_C_FLAGS_DEBUG "-g -O0 -Wall  -Wformat -Werror=format-security")

set(CMAKE_Fortran_COMPILER "ifort" CACHE STRING "" FORCE)
set(CMAKE_Fortran_FLAGS "-O3 -DNDEBUG -xCORE-AVX2 -mcmodel=large -shared-intel" CACHE STRING "" FORCE)

# for Intel MKL
set(BLA_VENDOR "Intel10_64lp" CACHE STRING "" FORCE)
