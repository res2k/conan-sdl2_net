from conans import ConanFile, CMake, tools
import os


class SDL2NetConan(ConanFile):
    name = "sdl2_net"
    version = "2.0.1"
    description = "Keep it short"
    topics = ("conan", "sdl2_net", "network")
    url = ""
    homepage = "https://www.libsdl.org/projects/SDL_net/"
    license = "Zlib"
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False],
               "fPIC": [True, False]}
    default_options = {"shared": False,
                       "fPIC": True}
    requires = "sdl2/2.0.12@bincrafters/stable"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"
    _cmake = None

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def requirements(self):
        pass

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = "SDL2_net-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

        tools.rmdir(os.path.join(self._source_subfolder, "external"))

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake 

        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        self._cmake = cmake

        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYING.txt", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["sdl2_net"]
        self.cpp_info.includedirs.append(os.path.join('include', 'SDL2'))
        if self.settings.os == "Windows":
            self.cpp_info.system_libs.extend(["ws2_32", "iphlpapi"])
