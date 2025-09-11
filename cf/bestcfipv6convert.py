import requests

def convert_data():
    """
    获取原始数据，转换为指定格式，并保存到新文件中。
    """
    raw_url = 'https://raw.githubusercontent.com/ymyuuu/IPDB/main/BestCF/bestcfv6.txt'
    try:
        response = requests.get(raw_url)
        response.raise_for_status()  # 如果请求失败，则引发异常
        lines = response.text.strip().split('\n')
        
        with open('cf/bestcfv6_converted.txt', 'w') as f:
            for i, line in enumerate(lines, 1):
                # 假设原始文件中的每一行都包含了 IP 地址和端口，格式为 IP:PORT
                # 如果格式不同，此处的处理逻辑需要相应调整
                # 这里我们直接将整行作为地址部分
                formatted_line = f"[{line}]:443#cm.v6_{i}\n"
                f.write(formatted_line)
        print("数据转换成功，已保存至 bestcfv6_converted.txt")
    except requests.exceptions.RequestException as e:
        print(f"获取数据失败: {e}")

if __name__ == "__main__":
    convert_data()
