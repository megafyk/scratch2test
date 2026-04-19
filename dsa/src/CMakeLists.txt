add_library(dsa INTERFACE)

target_include_directories(
    dsa
    INTERFACE
        ${PROJECT_SOURCE_DIR}/include
)

target_compile_features(dsa INTERFACE cxx_std_20)
