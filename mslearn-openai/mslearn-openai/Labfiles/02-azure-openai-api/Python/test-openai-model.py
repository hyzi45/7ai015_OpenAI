import os
from dotenv import load_dotenv

# TODO: Add Azure OpenAI package
from openai import AzureOpenAI

def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        #print(azure_oai_endpoint)
        #print(azure_oai_key)
        #print(azure_oai_deployment)

        # Initialize the Azure OpenAI client...
        client = AzureOpenAI(
            azure_endpoint= azure_oai_endpoint,
            api_key= azure_oai_key,
            api_version="2025-01-01-preview",
        )


        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            
            messages = [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "너는 여행 전문가야. 사용자의 질문에 여행 가이드처럼 답변해주고, 반말로 해줘. 그리고, 액티비티나 맛집 위주로 추천해줘. 만약, 나라를 말하고 여행 계획을 세워달라 하면 최대 3개의 도시까지만 추천해줘."
                        }
                    ]
                },

                # few shots ...
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "일본 여행을 가고 싶어."
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "먼저, 도쿄 (Tokyo)를 추천해줄게!           일본의 수도로 현대와 전통이 공존하는 도시이고 다양한 쇼핑 지역, 맛집, 문화 시설이 있어.                   주요 관광지는 도쿄타워가 있고, 맛집에는 스시다이, 이치란 라멘집이 있어! 두 번째로 추천하는 도시는 오사카 (Osaka)야! 일본의 식도락 도시로 알려져 있으며, 활기찬 분위기와 다양한 요리가 매력이거든.                   주요 관광지는 도톤보리(유명한 음식 거리), 유니버설 스튜디오 일본이 있고, 맛집에는 타코야키 쿠시카츠 다루마 (Daruma)가 있어."
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "스페인 세비야 여행 계획을 세워줘."
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": 
                    [
                        {
                            "type": "text",
                            "text": "1일차에는 세비야 도착 및 주요 명소 탐방해보는 건 어때? 오전에 숙소 체크인을 하고 점심을 바르 엘 푸에르토가서 타파스를 즐겨보는 거야!                오후에는 세비야 대성당과 히랄다 탑을 올라가서 세비야 전경을 감상해봐!  그리고 타파스 바에서 저녁을 먹고 플라자 데 에스파냐에서 야경을 즐겨보는 걸로 마무리 하는 거지."
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": input_text
                }
            ]

            # Add code to send request...
            completion = client.chat.completions.create(
                model= azure_oai_deployment,
                messages= messages,
                max_tokens= 800,
                temperature=0.5,
                top_p= 0.95
            )

            print(completion.choices[0].message.content)
        

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()