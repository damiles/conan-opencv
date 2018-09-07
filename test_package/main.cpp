#include <opencv2/core/core.hpp>

#include <iostream>
#include <string>

using namespace cv;



int main(int, char **)
{
    cv::Mat mat(3, 3, CV_8U);

    std::stringstream ss_file;
    ss_file << "./config.yaml";
    FileStorage fs(ss_file.str(), FileStorage::WRITE);
    fs << "test" << 100;
    fs << "mat" << mat;
    fs.release();   

    FileStorage fsr;
    fsr.open(ss_file.str(), FileStorage::READ);
    int n= (int) fsr["test"];
    std::cout << "Result of reading test on file: " << n << " value must be 100" << std::endl;
    fsr.release();

    std::cout << "Compile & Link OpenCV test application correctly" << std::endl;

    return EXIT_SUCCESS;

}
