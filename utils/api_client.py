import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        """
        初始化API客户端。

        :param base_url: API的基础URL
        :param headers: (可选) 请求头，应该是一个字典
        """
        self.base_url = base_url
        self.headers = headers or {}

    def request(self, endpoint, method="GET", params=None, data=None, headers=None):
        """
        发送一个指定HTTP方法的请求到API并返回响应。

        :param endpoint: API的endpoint，如 '/data'
        :param method: HTTP方法，如 'GET', 'POST', 'PUT', 'DELETE' 等
        :param params: (可选) URL参数，适用于GET请求
        :param data: (可选) 发送的数据，适用于POST/PUT请求，应该是一个字典
        :param headers: (可选) 请求头，应该是一个字典
        :return: 如果请求成功，返回响应的JSON数据；否则，返回None
        """
        url = f"{self.base_url}{endpoint}"
        combined_headers = {**self.headers, **(headers or {})}
        
        try:
            response = requests.request(method=method, url=url, params=params, json=data, headers=combined_headers)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"请求API时发生错误: {e}")
            return None

    def get(self, endpoint, params=None, headers=None):
        return self.request(endpoint, method="GET", params=params, headers=headers)

    def post(self, endpoint, data=None, headers=None):
        return self.request(endpoint, method="POST", data=data, headers=headers)

    def put(self, endpoint, data=None, headers=None):
        return self.request(endpoint, method="PUT", data=data, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.request(endpoint, method="DELETE", headers=headers)
