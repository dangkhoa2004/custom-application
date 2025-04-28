from discoIPC import ipc
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'details': 'Đang xem phim trên Netflix',
    'state': 'Thưởng thức bộ phim yêu thích!',
    'assets': {
        'large_image': 'netflix_image',  # Tên hình ảnh lớn
        'large_text': 'Netflix',           # Văn bản cho hình ảnh lớn
        'small_image': 'movie_icon',       # Tên hình ảnh nhỏ
        'small_text': 'Phim hay'           # Văn bản cho hình ảnh nhỏ
    }
}

def main():
    client = ipc.DiscordIPC(config['CLIENT']['client_id'])
    # Kết nối với Discord Client
    client.connect()

    print('\nBắt đầu hoạt động tùy chỉnh...\n')
    time.sleep(5)

    try:
        client.update_activity(set_activity())  # Cập nhật hoạt động
        while True:
            input('\nĐã kết nối! ')
            # Không làm gì   

    except KeyboardInterrupt:
        print('Ngắt kết nối...\n')
        client.disconnect()

def set_activity():
    # Thiết lập hoạt động cho người chơi.
    activity = base_activity
    return activity

if __name__ == '__main__':
    main()