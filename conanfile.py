from conans import ConanFile, tools, CMake

class OpenCVConan(ConanFile):
    """
    This recipe generates OpenCV with a classical setup that is useful for most of the cases.
    If you want to experiment with additional features use the provided options.

    This recipe requires conan 0.25.1 (At least)
    """
    name = 'OpenCV'
    version = 'master'
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'OpenCV recipe for the opencv repository'
    url = 'https://github.com/damiles/conan-opencv'
    source_url = 'https://github.com/opencv/opencv.git'
    source_contrib_url = 'https://github.com/opencv/opencv_contrib.git'
    license = 'MIT'
    generators = 'cmake'

    options = {
        'opencv_aruco': [True, False],
        'opencv_bgsegm': [True, False],
        'opencv_bioinspired': [True, False],
        'opencv_calib3d': [True, False],
        'opencv_ccalib': [True, False],
        'opencv_core': [True, False],
        'opencv_datasets': [True, False],
        'opencv_dnn': [True, False],
        'opencv_dnn_object': [True, False],
        'opencv_dpm': [True, False],
        'opencv_face': [True, False],
        'opencv_features2d': [True, False],
        'opencv_flann': [True, False],
        'opencv_freetype': [True, False],
        'opencv_fuzzy': [True, False],
        'opencv_hfs': [True, False],
        'opencv_highgui': [True, False],
        'opencv_img_hash': [True, False],
        'opencv_imgcodecs': [True, False],
        'opencv_imgproc': [True, False],
        'opencv_java': [True, False],
        'opencv_java_bindings_gen': [True, False],
        'opencv_js': [True, False],
        'opencv_line_descriptor': [True, False],
        'opencv_ml': [True, False],
        'opencv_objdetect': [True, False],
        'opencv_optflow': [True, False],
        'opencv_unwrapping': [True, False],
        'opencv_photo': [True, False],
        'opencv_plot': [True, False],
        'opencv_python2': [True, False],
        'opencv_python_bindings_g': [True, False],
        'opencv_reg': [True, False],
        'opencv_rgbd': [True, False],
        'opencv_saliency': [True, False],
        'opencv_shape': [True, False],
        'opencv_stereo': [True, False],
        'opencv_stitching': [True, False],
        'opencv_structured_light': [True, False],
        'opencv_superres': [True, False],
        'opencv_surface_matching': [True, False],
        'opencv_text': [True, False],
        'opencv_tracking': [True, False],
        'opencv_video': [True, False],
        'opencv_videoio': [True, False],
        'opencv_videostab': [True, False],
        'opencv_world': [True, False],
        'opencv_xfeatures2d': [True, False],
        'opencv_ximgproc': [True, False],
        'opencv_xobjdetect': [True, False],
        'opencv_xphoto': [True, False],
        'precompiled_headers': [True, False],
        'ffmpeg': [True, False],
        'webcam': [True, False],
        'shared': [True, False],
        'enable_cxx11': [True, False],
	'cuda': [True, False]
    }

    default_options = 'opencv_aruco=False', \
        'opencv_bgsegm=True', \
        'opencv_bioinspired=False', \
        'opencv_calib3d=True', \
        'opencv_ccalib=True', \
        'opencv_core=True', \
        'opencv_datasets=True', \
        'opencv_dnn=True', \
        'opencv_dnn_object=True', \
        'opencv_dpm=True', \
        'opencv_face=False', \
        'opencv_features2d=True', \
        'opencv_flann=True', \
        'opencv_freetype=True', \
        'opencv_fuzzy=True', \
        'opencv_hfs=True', \
        'opencv_highgui=True', \
        'opencv_img_hash=True', \
        'opencv_imgcodecs=True', \
        'opencv_imgproc=True', \
        'opencv_java=False', \
        'opencv_java_bindings_gen=False', \
        'opencv_js=False', \
        'opencv_line_descriptor=True', \
        'opencv_ml=True', \
        'opencv_objdetect=True', \
        'opencv_optflow=True', \
        'opencv_unwrapping=True', \
        'opencv_photo=True', \
        'opencv_plot=True', \
        'opencv_python2=False', \
        'opencv_python_bindings_g=False', \
        'opencv_reg=True', \
        'opencv_rgbd=False', \
        'opencv_saliency=True', \
        'opencv_shape=True', \
        'opencv_stereo=True', \
        'opencv_stitching=True', \
        'opencv_structured_light=True', \
        'opencv_superres=True', \
        'opencv_surface_matching=True', \
        'opencv_text=False', \
        'opencv_tracking=False', \
        'opencv_video=True', \
        'opencv_videoio=True', \
        'opencv_videostab=True', \
        'opencv_world=False', \
        'opencv_xfeatures2d=False', \
        'opencv_ximgproc=False', \
        'opencv_xobjdetect=False', \
        'opencv_xphoto=False', \
        'precompiled_headers=True', \
        'ffmpeg=True', \
        'webcam=True', \
        'shared=True', \
        'enable_cxx11=True', \
	'cuda=False'

    def source(self):
        self.run('git clone --depth 1 --branch %s %s' % (self.version, self.source_url))
        self.run('git clone --depth 1 --branch %s %s' % (self.version, self.source_contrib_url))

    def build(self):
        tools.replace_in_file("opencv/CMakeLists.txt",
            "project(OpenCV CXX C)",
            """project(OpenCV CXX C)
               include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
               conan_basic_setup()""")

        cmake = CMake(self, parallel=True)
        cmake_args = {
            'CMAKE_CONFIGURATION_TYPES' : self.settings.build_type,
            'CMAKE_BUILD_TYPE' : self.settings.build_type,
            'BUILD_PACKAGE' : 'OFF',
            'BUILD_PERF_TESTS' : 'OFF',
            'BUILD_TESTS' : 'OFF',
            'BUILD_DOCS' : 'OFF',
            'BUILD_WITH_DEBUG_INFO' : 'OFF',
            'BUILD_EXAMPLES' : 'OFF',
            'BUILD_SHARED_LIBS' : self.options.shared,

            'BUILD_opencv_apps' : 'OFF',
            'BUILD_opencv_aruco' : self.options.opencv_aruco,
            'BUILD_opencv_bgsegm' : self.options.opencv_bgsegm,
            'BUILD_opencv_bioinspired' : self.options.opencv_bioinspired,
            'BUILD_opencv_calib3d': self.options.opencv_calib3d,
            'BUILD_opencv_ccalib' : self.options.opencv_ccalib,
            'BUILD_opencv_core': self.options.opencv_core,
            'BUILD_opencv_datasets': self.options.opencv_datasets,
            'BUILD_opencv_dnn': self.options.opencv_dnn,
            'BUILD_opencv_dnn_objdetect': self.options.opencv_dnn_object,
            'BUILD_opencv_dpm': self.options.opencv_dpm,
            'BUILD_opencv_face': self.options.opencv_face,
            'BUILD_opencv_features2d': self.options.opencv_features2d,
            'BUILD_opencv_flann': self.options.opencv_flann,
            'BUILD_opencv_freetype': self.options.opencv_freetype,
            'BUILD_opencv_fuzzy': self.options.opencv_fuzzy,
            'BUILD_opencv_hfs': self.options.opencv_hfs,
            'BUILD_opencv_highgui': self.options.opencv_highgui,
            'BUILD_opencv_img_hash': self.options.opencv_img_hash,
            'BUILD_opencv_imgcodecs': self.options.opencv_imgcodecs,
            'BUILD_opencv_imgproc': self.options.opencv_imgproc,
            'BUILD_opencv_java' : self.options.opencv_java,
            'BUILD_opencv_java_bindings_gen': self.options.opencv_java_bindings_gen,
            'BUILD_opencv_js': self.options.opencv_js,
            'BUILD_opencv_line_descriptor': self.options.opencv_line_descriptor,
            'BUILD_opencv_ml': self.options.opencv_ml,
            'BUILD_opencv_objdetect': self.options.opencv_objdetect,
            'BUILD_opencv_optflow': self.options.opencv_optflow,
            'BUILD_opencv_phase_unwrapping': self.options.opencv_unwrapping,
            'BUILD_opencv_photo': self.options.opencv_photo,
            'BUILD_opencv_plot': self.options.opencv_plot,
            'BUILD_opencv_python2' : self.options.opencv_python2,
            'BUILD_opencv_python_bindings_g': self.options.opencv_python_bindings_g,
            'BUILD_opencv_reg': self.options.opencv_reg,
            'BUILD_opencv_rgbd': self.options.opencv_rgbd,
            'BUILD_opencv_saliency': self.options.opencv_saliency,
            'BUILD_opencv_shape': self.options.opencv_shape,
            'BUILD_opencv_stereo': self.options.opencv_stereo,
            'BUILD_opencv_stitching': self.options.opencv_stitching,
            'BUILD_opencv_structured_light': self.options.opencv_structured_light,
            'BUILD_opencv_superres': self.options.opencv_superres,
            'BUILD_opencv_surface_matching': self.options.opencv_surface_matching,
            'BUILD_opencv_text': self.options.opencv_text,
            'BUILD_opencv_tracking' : self.options.opencv_tracking,
            'BUILD_opencv_video': self.options.opencv_video,
            'BUILD_opencv_videoio': self.options.opencv_videoio,
            'BUILD_opencv_videostab' : self.options.opencv_videostab,
            'BUILD_opencv_world' : self.options.opencv_world,
            'BUILD_opencv_xfeatures2d': self.options.opencv_xfeatures2d,
            'BUILD_opencv_ximgproc': self.options.opencv_ximgproc,
            'BUILD_opencv_xobjdetect': self.options.opencv_xobjdetect,
            'BUILD_opencv_xphoto': self.options.opencv_xphoto,
            
            'CMAKE_VERBOSE_MAKEFILE' : 'OFF',

            'BUILD_ZLIB' : 'ON',
            'BUILD_PNG' : 'ON',
            'WITH_PNG' : 'ON',
            'WITH_TIFF' : 'ON',
            'WITH_JPEG' : 'ON',
            'WITH_GTK' : 'ON',
            'WITH_FFMPEG' : self.options.ffmpeg,

            'BUILD_PROTOBUF' : 'OFF',

            'WITH_LAPACK' : 'OFF',
            'WITH_IPP' : 'OFF',
            'WITH_QT' : 'OFF',
            'WITH_OPENMP' : 'OFF',
            'WITH_WEBP' : 'OFF',
            'WITH_OPENEXR' : 'OFF',
            'WITH_TBB' : 'OFF',
            'WITH_1394' : 'OFF',
            'WITH_CUDA' : self.options.cuda,
            'WITH_CUFFT' : 'OFF',
            'WITH_OPENCL' : 'OFF',
            'WITH_OPENCLAMDBLAS' : 'OFF',
            'WITH_OPENCLAMDFFT' : 'OFF',
            'WITH_OPENCL_SVM' : 'OFF',
            'WITH_PVAPI' : 'OFF',
            'WITH_GSTREAMER' : 'OFF',
            'WITH_JASPER' : 'OFF',
            'WITH_GIGEAPI' : 'OFF',
            'WITH_GPHOTO2' : 'OFF',
            'WITH_V4L' : self.options.webcam,
            'WITH_LIBV4L' : self.options.webcam,
            'WITH_MATLAB' : 'OFF',
            'WITH_VTK' : 'OFF',

            'CPU_BASELINE' : 'SSE3;SSE4_1',
            'CPU_DISPATCH' : '',
            #'CPU_DISPATCH' : 'SSE4_2;AVX;AVX2',

            'OPENCV_EXTRA_MODULES_PATH' : '../opencv_contrib/modules/',

            'ENABLE_PRECOMPILED_HEADERS' : 'ON',
            'ENABLE_CXX11': self.options.enable_cxx11,   
        }

        cmake.configure(source_dir='../opencv', build_dir='build', defs=cmake_args)
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        for option, activated in self.options.items():
            if activated == 'True' and option.startswith("opencv_"):
                self.cpp_info.libs.append(option)
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
