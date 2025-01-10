import requests
from typing import Dict, Any, Optional

class HttpClient:
    def __init__(self, base_url: str):
        """
        初始化 HTTP 客户端
        :param base_url: 基础 URL
        """
        self.base_url = base_url

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> Dict[str, Any]:
        """
        发送 POST 请求
        :param endpoint: 接口路径
        :param data: 请求体
        :param headers: 请求头
        :param timeout: 超时时间（秒）
        :return: 响应 JSON 数据
        """
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            response = requests.post(url, json=data, headers=headers, timeout=timeout)
            response.raise_for_status()  # 检查 HTTP 响应状态码
            return response.json()  # 返回 JSON 数据
        except requests.exceptions.RequestException as e:
            print(f"HTTP 请求失败: {e}")
            return {"error": str(e)}

# 使用示例
if __name__ == "__main__":
    client = HttpClient(base_url="https://api.example.com")
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    data = {"key1": "value1", "key2": "value2"}
    response = client.post("/v1/endpoint", data=data, headers=headers)
    print(response)
