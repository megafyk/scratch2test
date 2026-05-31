# Unit test targets.
#
# To add a test: drop unit/<name>.cpp in place (include "test_utils.hpp") and
# call dsa_add_unit_test(<name>). It links the dsa library plus the dev-only
# warning/sanitizer helpers and registers the executable with CTest.
function(dsa_add_unit_test name)
    add_executable(${name} unit/${name}.cpp)
    target_link_libraries(${name} PRIVATE dsa dsa_warnings dsa_sanitizers)
    target_include_directories(${name} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
    add_test(NAME ${name} COMMAND ${name})
endfunction()

dsa_add_unit_test(hash_table_test)
