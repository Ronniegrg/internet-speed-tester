# import speedtest module
import speedtest

speed_test = speedtest.Speedtest()
def bytes_to_mb(bytes):
    KB = 1024 # 1 Kilobyte is equal to 1024 bytes
    MB = 1024 * KB # 1 Megabyte is equal to 1024 Kilobytes
    return int(bytes/MB);

# download speed
download_speed = bytes_to_mb(speed_test.download())
print("Your Download Speed is: ", download_speed, "MB")

# upload speed
upload_speed = bytes_to_mb(speed_test.upload())
print("Your Upload Speed is: ", upload_speed, "MB")

