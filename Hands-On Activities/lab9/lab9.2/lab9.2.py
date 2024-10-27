import os

def read_wav_file(filename):
    """Đọc file WAV và trả về header và data"""
    with open(filename, "rb") as f:
        header = f.read(44)  # Header của file WAV
        data = f.read()      # Phần dữ liệu âm thanh
    return header, data

def split_data(data):
    """Tách dữ liệu âm thanh thành hai luồng"""
    data1 = data[0::2]  # Lấy các byte chẵn
    data2 = data[1::2]  # Lấy các byte lẻ
    return data1, data2

def update_header(header, data_length, sampling_rate=None):
    """Cập nhật header cho file WAV"""
    updated_header = bytearray(header)
    # Cập nhật kích thước file
    file_size = 36 + data_length
    updated_header[4:8] = file_size.to_bytes(4, byteorder="little")
    # Cập nhật kích thước phần dữ liệu
    updated_header[40:44] = data_length.to_bytes(4, byteorder="little")
    # Nếu cần thay đổi tần số mẫu, cập nhật các byte tương ứng
    if sampling_rate:
        updated_header[24:28] = sampling_rate.to_bytes(4, byteorder="little")
        updated_header[28:32] = sampling_rate.to_bytes(4, byteorder="little")
    return updated_header

def write_wav_file(filename, header, data):
    """Ghi file WAV với header và data đã được cập nhật"""
    with open(filename, "wb") as f:
        f.write(header)
        f.write(data)

def split_music_file(input_file, output_file1, output_file2, sampling_rate1=None, sampling_rate2=None):
    """Tách một file WAV thành hai file âm thanh riêng biệt"""
    # Đọc header và dữ liệu từ file gốc
    header, data = read_wav_file(input_file)
    
    # Tách dữ liệu thành hai luồng
    data1, data2 = split_data(data)

    # Cập nhật header cho hai file đầu ra
    header1 = update_header(header, len(data1), sampling_rate1)
    header2 = update_header(header, len(data2), sampling_rate2)

    # Ghi dữ liệu vào hai file đầu ra
    write_wav_file(output_file1, header1, data1)
    write_wav_file(output_file2, header2, data2)

# Tách file music.wav
split_music_file("music.wav", "song1.wav", "song2.wav")

# Tách file audio.wav với tần số mẫu khác nhau
split_music_file("audio.wav", "song1_audio.wav", "song2_audio.wav", sampling_rate1=11025, sampling_rate2=22050)
