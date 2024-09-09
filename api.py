import requests

arxiv_id = "2403.00825"
url = f"https://api.semanticscholar.org/v1/paper/arXiv:{arxiv_id}"
# 发起请求
response = requests.get(url)
# 检查请求是否成功
if response.status_code == 200:
    # 解析响应的 JSON 数据
    data = response.json()
    
    # 获取并打印 Semantic Scholar 的 ID
    semantic_scholar_id = data.get("paperId")
    print(f"Semantic Scholar ID: {semantic_scholar_id}")
else:
    print(f"请求失败，状态码：{response.status_code}")
