include(GoogleTest)

# Example: add tests like this
# add_executable(test_linked_list data_structures/test_linked_list.cpp)
# target_include_directories(test_linked_list PRIVATE ${PROJECT_SOURCE_DIR}/include)
# target_link_libraries(test_linked_list GTest::gtest_main)
# gtest_discover_tests(test_linked_list)

add_executable(test_hash_table data_structures/test_hash_table.cpp)
target_include_directories(test_hash_table PRIVATE ${PROJECT_SOURCE_DIR}/include)
target_link_libraries(test_hash_table GTest::gtest_main)
gtest_discover_tests(test_hash_table)
