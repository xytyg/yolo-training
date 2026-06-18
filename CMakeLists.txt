cmake_minimum_required(VERSION 3.16)
project(rtsp_recorder_cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(record_video_cpp "src/褰曡棰?cpp")

# Put executable in project bin directory.
set_target_properties(record_video_cpp PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin"
  RUNTIME_OUTPUT_DIRECTORY_DEBUG "${CMAKE_SOURCE_DIR}/bin"
  RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_SOURCE_DIR}/bin"
)

# Allow user/environment to provide OpenCV_DIR, while still giving a useful fallback.
if(NOT OpenCV_DIR)
  if(EXISTS "${CMAKE_SOURCE_DIR}/build/opencv_build/win-install/x64/vc16/lib/OpenCVConfig.cmake")
    set(OpenCV_DIR "${CMAKE_SOURCE_DIR}/build/opencv_build/win-install/x64/vc16/lib")
  elseif(EXISTS "${CMAKE_SOURCE_DIR}/build/opencv_build/win-install")
    set(OpenCV_DIR "${CMAKE_SOURCE_DIR}/build/opencv_build/win-install")
  endif()
endif()

find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui videoio)
target_link_libraries(record_video_cpp PRIVATE ${OpenCV_LIBS})

# Copy runtime DLL dependencies next to the executable.
if(WIN32)
  set(OPENCV_BIN_DIR "${OpenCV_DIR}/../bin")
  set(RUNTIME_DLLS)
  if(EXISTS "${OPENCV_BIN_DIR}")
    file(GLOB OPENCV_RUNTIME_DLLS "${OPENCV_BIN_DIR}/*.dll")
    list(APPEND RUNTIME_DLLS ${OPENCV_RUNTIME_DLLS})
  endif()

  set(LOCAL_FFMPEG_DLL_DIR "${CMAKE_SOURCE_DIR}/dll")
  if(EXISTS "${LOCAL_FFMPEG_DLL_DIR}")
    file(GLOB LOCAL_FFMPEG_DLLS "${LOCAL_FFMPEG_DLL_DIR}/*.dll")
    list(APPEND RUNTIME_DLLS ${LOCAL_FFMPEG_DLLS})
  endif()

  if(RUNTIME_DLLS)
    add_custom_command(TARGET record_video_cpp POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E make_directory "$<TARGET_FILE_DIR:record_video_cpp>"
      COMMAND ${CMAKE_COMMAND} -E copy_if_different
              ${RUNTIME_DLLS}
              "$<TARGET_FILE_DIR:record_video_cpp>"
      COMMENT "Copying OpenCV/FFmpeg runtime DLLs to bin"
      VERBATIM
    )
  endif()
endif()

message(STATUS "OpenCV version: ${OpenCV_VERSION}")
message(STATUS "OpenCV libs: ${OpenCV_LIBS}")
