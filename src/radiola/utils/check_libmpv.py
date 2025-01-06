import ctypes.util
import platform
import os
import subprocess


def check_libmpv():
    # Check if libmpv is available in the usual places
    libmpv_path = ctypes.util.find_library("mpv")

    if not libmpv_path:
        # If libmpv is not found, check the operating system
        if platform.system() == "Darwin":  # macOS
            try:
                # Get Homebrew prefix
                homebrew_prefix = (
                    subprocess.check_output(["brew", "--prefix"]).decode().strip()
                )
                homebrew_lib_path = os.path.join(homebrew_prefix, "lib")
                if os.path.exists(homebrew_lib_path):
                    os.environ["DYLD_LIBRARY_PATH"] = (
                        f"{homebrew_lib_path}:{os.getenv('DYLD_LIBRARY_PATH', '')}"
                    )
                    # Retry finding libmpv after setting the path
                    libmpv_path = ctypes.util.find_library("mpv")
            except subprocess.CalledProcessError:
                pass

    if not libmpv_path:
        raise OSError(
            "Could not find libmpv. Please ensure it is installed and available in your system."
        )

    return libmpv_path
