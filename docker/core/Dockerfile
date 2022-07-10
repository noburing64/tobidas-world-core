FROM ubuntu:bionic

# OpenMVGのインストール
ENV PATH=$PATH:/opt/openMVG_Build/install/bin
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    coinor-libclp-dev \
    libceres-dev \
    libflann-dev \
    liblemon-dev \
    libjpeg-dev \
    libpng-dev \
    libglu1-mesa-dev \
    libboost-iostreams-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-serialization-dev \
    g++-8 \
    libssl-dev \
    wget \
    libopencv-dev \
    libcgal-dev \
    libcgal-qt5-dev \
    libatlas-base-dev \
    libsuitesparse-dev \
    freeglut3-dev \
    libglew-dev \
    libglfw3-dev \
    python3-pip \
    libtiff-dev; \
    apt-get autoclean && \
    apt-get clean; \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8

RUN pip3 install pip --upgrade --no-cache-dir

# apt-getからのCmakeはOpenMVGのビルドでエラーになる
RUN wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz; \
    tar -zvxf cmake-3.20.0.tar.gz; \
    cd cmake-3.20.0; \
    ./bootstrap; \
    make && make install; \
    cd ../; \
    git clone https://github.com/openMVG/openMVG.git /opt/openMVG && \
    cd /opt/openMVG && git submodule update --init --recursive && \
    mkdir /opt/openMVG_Build; \
    cd /opt/openMVG_Build; \
    cmake -DCMAKE_BUILD_TYPE=RELEASE \
    -DCMAKE_INSTALL_PREFIX="/opt/openMVG_Build/install" \
    -DOpenMVG_BUILD_TESTS=OFF \
    -DOpenMVG_BUILD_EXAMPLES=OFF \
    -DFLANN_INCLUDE_DIR_HINTS=/usr/include/flann \
    -DLEMON_INCLUDE_DIR_HINTS=/usr/include/lemon \
    -DCOINUTILS_INCLUDE_DIR_HINTS=/usr/include \
    -DCLP_INCLUDE_DIR_HINTS=/usr/include \
    -DOSI_INCLUDE_DIR_HINTS=/usr/include \
    ../openMVG/src; \
    make -j4; \
    cd /opt/openMVG_Build && make install;


RUN main_path=`pwd`; \
    git clone https://gitlab.com/libeigen/eigen.git --branch 3.4; \
    mkdir eigen_build && cd eigen_build; \
    cmake . ../eigen; \
    make && make install; \
    cd ../; \
    git clone https://github.com/cdcseacave/VCG.git vcglib; \
    cd vcglib && git checkout 88f12f212a1645d1fa6416592a434c29e63b57f0; \
    cd ../; \
    git clone https://ceres-solver.googlesource.com/ceres-solver ceres-solver; \
    mkdir ceres_build && cd ceres_build; \
    cmake . ../ceres-solver/ \
    -DMININGLOG=ON \
    -DBUILD_TESTING=OFF \
    -DBUILD_EXAMPLES=OFF; \
    make -j2 && make install; \
    cd ../; \
    wget https://github.com/cdcseacave/openMVS/archive/refs/tags/v2.0.tar.gz; \
    tar -zvxf v2.0.tar.gz && mkdir openMVS_build; \
    cd openMVS_build; \
    cmake . ../openMVS-2.0 \
    -DCMAKE_BUILD_TYPE=Release \
    -DVCG_ROOT="$main_path/vcglib"; \
    make -j2 && make install

RUN sed -i -e 's/@OPENMVG_SOFTWARE_SFM_BUILD_DIR@/\/opt\/openMVG_Build\/Linux-x86_64-RELEASE\//g' \
    /opt/openMVG/src/software/SfM/tutorial_demo.py.in; \
    sed -i -e 's/@OPENMVG_SOFTWARE_SFM_SRC_DIR@/\/opt\/openMVG\/src\/software\/SfM\//g' \
    /opt/openMVG/src/software/SfM/tutorial_demo.py.in

WORKDIR /app
ADD ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python3", "run.py"]
