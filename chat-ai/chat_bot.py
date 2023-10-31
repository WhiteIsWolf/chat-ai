import requests
import json
import os

API_KEY = "your_key"  
SECRET_KEY = "yoour_password" 

def get_access_token():
    """
    使用 API Key,Secret Key 获取access_token,替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+API_KEY+"&client_secret="+SECRET_KEY
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

def get_reply(content):
    if(content == "clear"):
        os.system('cls' if os.name == 'nt' else 'clear')
        return 0
    if(content == "quit"):
        return -1
    
    print("please wait for a while……\n\n")
    
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # print(response.text)
    data = json.loads(response.text)  
    result = data['result']
    print(result)
    print("\n\n")

    return 1
        
    
    

if __name__ == '__main__':
    print("connecting……")
    content = ""
    # content = "给我推荐一些自驾游路线"
    # content = "要求使用Python获取键盘输入"
    while(content != "quit"):
        print("===========================================================================================================================")
        # 获取用户输入  
        content = input("请输入您的问题: ")
        ret = get_reply(content)
        
    
    