% Load latest CSV file manually
filename = 'data_log_20250701_221535.csv'; % Change this to your file name

data = readtable(filename);
time = datetime(data.timestamp, 'InputFormat', 'yyyy-MM-dd HH:mm:ss');

figure;
plot(time, data.temperature, '-o', 'LineWidth', 1.5);
hold on;
plot(time, data.humidity, '-s', 'LineWidth', 1.5);
plot(time, data.gas_level, '-^', 'LineWidth', 1.5);
hold off;

xlabel('Time');
ylabel('Sensor Readings');
title('IoT Sensor Data Logger');
legend('Temperature (°C)', 'Humidity (%)', 'Gas Level (ppm)');
grid on;
