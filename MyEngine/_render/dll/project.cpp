#include <cmath>

extern "C" {
    void project(double _Camera_x, double _Camera_y, double _Camera_z, double _Camera_width, double _Camera_height, double _Camera_angle_x, double _Camera_angle_y, double point_x, double point_y, double point_z, double* x, double* y) {
        auto rotate2d = [](const std::pair<double, double>& pos, double angle) -> std::pair<double, double> {
            double x = pos.first, y = pos.second;
            double s = sin(angle), c = cos(angle);

            return {x*c - y*s, y*c + x*s};
        };

        double dx = point_x - _Camera_x;
        double dy = point_y - _Camera_y;
        double dz = point_z - _Camera_z;

        auto rotated_xz = rotate2d({dx, dz}, _Camera_angle_x);
        auto rotated_yz = rotate2d({dy, rotated_xz.second},_Camera_angle_y);

        double f = 200 / rotated_yz.second;
        double px = rotated_xz.first * f;
        double py = rotated_yz.first * f;

        *x = static_cast<int>(px + _Camera_width/2);
        *y = static_cast<int>(py + _Camera_height/2);
    }
}
